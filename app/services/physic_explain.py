from copy import deepcopy

from utils.chatbot_utils.state import State
from utils.chatbot_utils.chain import get_chat_completion


def explain_physics(state: State):
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
    valid_responses = []
    response_count = 0
    
    for subquestion in subquestions["subquestions"]:
        state.data = data
        state.question = subquestion
        state = answer_question(state)
        print(f"-> {state.response}\n\n")
        data.extend(state.data)
        
        # Chỉ thêm vào kết quả nếu có câu trả lời hợp lệ
        if state.response and state.response.strip() and not state.response.startswith("Không thể tạo câu hỏi con"):
            response_count += 1
            recommendations = state.recommendations or []
            
            # Tạo nội dung câu trả lời
            response_content = f"""{response_count}. Câu hỏi: {subquestion}

Trả lời: {state.response}"""
            
            # Chỉ thêm phần hành động đề xuất nếu có recommendations
            if recommendations:
                response_content += f"""

Hành động đề xuất:
{"\n".join([f"- {item}" for item in recommendations])}"""
            
            valid_responses.append(response_content)

    # response = get_chat_completion(
    #     task="summary",
    #     params={
    #         "context": "\n".join(valid_responses),
    #         "question": state.question
    #     }
    # )
    # state.response = response["response"]
    
    if valid_responses:
        state.response = "\n".join(valid_responses)
    else:
        state.response = "Không thể trả lời câu hỏi này với thông tin hiện có."
    
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
        state.response = response["response"]
        state.recommendations = response.get("recommendations", [])
        if state.response:
            state.data.append(state.response)
        return state

    # Nếu không thể trả lời trực tiếp, tạo câu hỏi con và xử lý
    subquestion = response["subquestion"]
    if not subquestion or subquestion.strip() == "":
        state.response = "Không thể tạo câu hỏi con để trả lời."
        state.recommendations = []
        return state
    
    new_state = deepcopy(state)
    new_state.question = subquestion
    new_state = answer_question(new_state, depth + 1, max_depth)

    # Cập nhật state với kết quả từ câu hỏi con
    state.data.extend([item for item in new_state.data if item not in state.data])
    state.response = new_state.response
    state.recommendations = new_state.recommendations
    return state
