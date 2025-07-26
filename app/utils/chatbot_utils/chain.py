from typing import Dict, Any, Tuple

from langchain.prompts import ChatPromptTemplate

from app.core.llm import llm
from app.utils.chatbot_utils.prompts import intent_classify, simplify, break_down
from app.utils.chatbot_utils.parsers import (
    intent_classify as intent_classify_parser,
    simplify as simplify_parser,
    break_down as break_down_parser
)

def get_chat_completion(task: str, params: Dict[str, Any] = {}):
    """
    Get chat completion from the LLM for a given task with optional parameters.
    
    Args:
        task (str): The task description for which to get the chat completion.
        params (Dict[str, Any], optional): Additional parameters for the LLM request.
        
    Returns:
        Dict[str, Any]: The response from the LLM containing the chat completion.
    """
    prompt, parser = get_prompt_template(task)
    chain = prompt | llm | parser

    response = chain.invoke(params)
    if not isinstance(response, dict):
        response = dict(response)
    
    return response


def get_prompt_template(task: str):
    """
    Get the prompt template and parser for a given task.
    
    Args:
        task (str): The task description for which to get the prompt template.
        
    Returns:
        Tuple[str, Any]: A tuple containing the prompt template and the parser.
    """
    if task == "simplify":
        prompt = simplify.prompt
        parser = simplify_parser.simplify_parser
    
    elif task == "intent_classify":
        prompt = intent_classify.prompt
        parser = intent_classify_parser.intent_classify_parser
    
    elif task == "break_down":
        prompt = break_down.prompt
        parser = break_down_parser.break_down_parser

    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", prompt + """{format_instructions}"""),
            ("human", "{question}"),
        ]
    ).partial(format_instructions=parser.get_format_instructions())
    return prompt_template, parser