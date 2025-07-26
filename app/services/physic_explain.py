from copy import deepcopy
from typing import Set
from app.utils.chatbot_utils.state import State
from app.utils.chatbot_utils.chain import get_chat_completion


def explain_physics(state: State):
    responses = []
    data = []

    """Đơn giản hóa sơ đồ điện"""
    simplified_graph = get_chat_completion(
        task="simplify",
        params={"question": state.graph}
    )
    state.graph = simplified_graph["description"]
    print(f"[DEBUG] Tóm tắt sơ đồ điện: \n{state.graph}\n")

    """Tách câu hỏi lớn thành nhiều câu hỏi nhỏ hơn"""
    subquestions = get_chat_completion(
        task="break_down",
        params={"question": state.question}
    )

    """Xử lý từng câu hỏi nhỏ"""
    if len(subquestions["subquestions"]) == 1:
        question = subquestions["subquestions"][0]
        print(f"\tCâu hỏi: {question}")
        state.question = question
        state.data = data
        state = answer_question(state)
        print(f"-> {state.response}\n")
        responses.append(f"Câu hỏi: {question}\n{state.response}")
        data.extend(state.data)

    else:
        for idx, subquestion in enumerate(subquestions["subquestions"]):
            print(f"\tCâu hỏi: {subquestion}\n")
            state.question = subquestion
            state.data = data
            state = answer_question(state)
            print(f"-> {state.response}\n\n")
            responses.append(f"{idx + 1}. Câu hỏi: {subquestion}\n{state.response}")
            data.extend(state.data)

    state.response = "\n".join(responses)
    return state


def answer_question(state: State, depth=0, max_depth=5) -> State:
    if depth > max_depth:
        state.response = "Bài toán quá phức tạp, không thể trả lời."
        return state

    response = get_chat_completion(
        task="intent_classify",
        params={
            "question": state.question,
            "context": state.graph,
            "data": "\n".join([f"- {item}" for item in state.data] if state.data else []),
        }
    )

    if response["can_answer"]:
        state.response = response["response"]
        state.data.append(state.response)
        return state

    subquestion = response["subquestion"]
    new_state = deepcopy(state)
    new_state.question = subquestion
    new_state = answer_question(new_state, depth, max_depth)

    state.data.extend([item for item in new_state.data if item not in state.data])

    if new_state.response:
        retry_state = answer_question(state, depth + 1, max_depth)
        return retry_state
    else:
        state.response = "Không thể trả lời sau khi phân tích thêm."
        return state
