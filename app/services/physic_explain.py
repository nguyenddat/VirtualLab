from copy import deepcopy

from app.utils.chatbot_utils.state import State
from app.utils.chatbot_utils.chain import get_chat_completion, get_chat_completion_stream
from app.core.llm import llm

def explain_physics(state: State):
    state = rewrite_graph(state)

    bf_summary = []
    subquestions = break_down_question(state)
    for question in subquestions:
        response = answer_question(State(question=question, graph=state.graph, data=state.data))
        sub_response = f"Câu hỏi: {question}\nTrả lời: {response}\n"
        print(sub_response)
        bf_summary.append(sub_response)
    
    full_response = ""
    for chunk in get_chat_completion_stream(
        task="summary",
        params={"question": state.question, "context": "\n".join(bf_summary)}
    ):
        if not isinstance(chunk, str):
            chunk = chunk.response
        
        yield chunk
        full_response = chunk
    
    yield full_response
    
def answer_question(state: State, max_depth: int = 3, current_depth: int = 0):
    if current_depth == max_depth:
        return "Tôi không thể trả lời câu hỏi này!"
    
    intent_classify = get_chat_completion(
        task="intent_classify",
        params={"question": state.question, "context": state.graph, "data": state.data}
    )
    
    if intent_classify["can_answer"]:
        return intent_classify["response"]
    else:
        copy_state = deepcopy(state)
        copy_state.question = intent_classify["subquestion"]
        return answer_question(copy_state, max_depth, current_depth + 1)
    
def break_down_question(state: State):
    subquestions = get_chat_completion(
        task="break_down",
        params={"question": state.question}
    )
    return subquestions["subquestions"]


def rewrite_graph(state: State):
    simplified_graph = get_chat_completion(
        task="simplify",
        params={"question": state.graph}
    )
    state.graph = simplified_graph["description"]
    return state
