from copy import deepcopy

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
    for idx, subquestion in enumerate(subquestions["subquestions"]):
        state.data = data
        state.question = subquestion
        state = answer_question(state)
        print(f"-> {state.response}\n\n")
        data.extend(state.data)
        responses.append(f"""{idx + 1}. Câu hỏi: {subquestion}
{state.response}
Bạn có thể áp dụng một số hành động sau đây:
{"\n".join(state.recommendations)}
""")

    # response = get_chat_completion(
    #     task="summary",
    #     params={
    #         "context": "\n".join(responses),
    #         "question": state.question
    #     }
    # )
    # state.response = response["response"]
    state.response = "\n".join(responses)
    return state


def answer_question(state: State, depth=0, max_depth=5) -> State:
    print(f"[Depth {depth}] Đang xử lý câu hỏi: {state.question}")
    if depth > max_depth:
        state.response = "Bài toán quá phức tạp, không thể trả lời."
        state.recommendations = []
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
        state.data.append(state.response)
        state.response = response["response"]
        state.recommendations = response["recommendations"]
        return state

    subquestion = response["subquestion"]
    new_state = deepcopy(state)
    new_state.question = subquestion
    new_state = answer_question(new_state, depth, max_depth)

    state.data.extend([item for item in new_state.data if item not in state.data] + [new_state.response])
    state = answer_question(state, depth + 1, max_depth)
    return state
