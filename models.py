from langchain_huggingface import HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama


def load_model(model):
    if model == 'HuggingFace':
        return model_hf_hub()
    elif model == 'OpenAI':
        return model_openai()
    elif model == 'OLlama':
        return model_ollama()

def model_hf_hub(model='meta-llama/Meta-Llama-3-8B-Instruct', temperature=0.1):
    llm = HuggingFaceEndpoint(repo_id=model,
                              task='text-generation',
                              temperature=temperature,
                              return_full_text=False,
                              max_new_tokens=1024)
    return llm

def model_openai(model='gpt-4o-mini', temperature=0.1):
    llm = ChatOpenAI(model=model, temperature=temperature)
    return llm

def model_ollama(model='phi3', temperature=0.1):
    llm = ChatOllama(model=model, temperature=temperature)
    return llm