from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate


def define_prompt_template(model):
    if 'huggingface' in str(model.__class__).lower():
        token_s, token_e = "<|begin_of_text|><|start_header_id|>system<|end_header_id|>", "<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
    else:
        token_s, token_e = "", ""

    context_q_system_prompt = token_s + "Given the following chat history and the follow-up question which might reference context in the chat history, formulate a standalone question which can be understood without the chat history. Do NOT answer the question, just reformulate it if needed and otherwise return it as is."
    context_q_user_prompt = "Question: {input}" + token_e
    context_q_prompt = ChatPromptTemplate.from_messages([
        ('system', context_q_system_prompt),
        MessagesPlaceholder('chat_history'),
        ('human', context_q_user_prompt)
    ])
     # Q&A prompt
    qa_prompt_template = """Você é um assistente virtual prestativo e está respondendo perguntas gerais. 
    Use os seguintes pedaços de contexto recuperado para responder à pergunta. 
    Se você não sabe a resposta, apenas diga que não sabe. Mantenha a resposta concisa. 
    Responda em português. \n\n
    Pergunta: {input} \n
    Contexto: {context}"""
    qa_prompt = PromptTemplate.from_template(token_s + qa_prompt_template + token_e)

    return context_q_prompt, qa_prompt
