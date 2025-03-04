import tempfile
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from templates import define_prompt_template
from models import load_model
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain


def config_retriever(uploads):
    docs = []
    temp_dir = tempfile.TemporaryDirectory()
    for file in uploads:
        temp_file_path = os.path.join(temp_dir.name, file.name)
        with open(temp_file_path, 'wb') as f:
            f.write(file.getvalue())
        loader = PyPDFLoader(temp_file_path)
        docs.extend(loader.load())

    # Split
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    # Embedding
    embeddings = HuggingFaceEmbeddings(model_name='BAAI/bge-m3')
    # Docs storage
    vector_store = FAISS.from_documents(splits, embeddings)
    vector_store.save_local('vectorstore/db_faiss')
    # Retriever config
    retriever = vector_store.as_retriever(search_type='mmr',
                                          search_kwargs={
                                              'k': 3,
                                              'fetch_k': 4
                                          })
    return retriever

def config_rag_chain(model_name, retriever):
    llm = load_model(model_name)
    context_q_prompt, qa_prompt = define_prompt_template(llm)
    history_aware_retriever = create_history_aware_retriever(llm=llm,
                                                             retriever=retriever,
                                                             prompt=context_q_prompt)
    qa_chain = create_stuff_documents_chain(llm, qa_prompt)
    rag_chain = create_retrieval_chain(history_aware_retriever, qa_chain)
    return rag_chain
   