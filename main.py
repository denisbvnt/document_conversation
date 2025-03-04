import os
import time
import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from tasks import config_rag_chain, config_retriever


load_dotenv()
st.set_page_config(page_title='Converse com documentos 📚', page_icon='📚')
st.markdown(
    """
    <style>
    label {
        color: white !important;
        font-weight: bold;
    }
    .stApp {
        background-color: #f2f2f2;
    }
    .stSidebar {
        background-color: #1ED760;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title('Converse com documentos 📚')
st.divider()

model_options = ['HuggingFace', 'OLlama', 'OpenAI']

if "model_name" not in st.session_state:
    st.session_state.model_name = model_options[0]

model_name = st.sidebar.selectbox('Model', model_options, index=model_options.index(st.session_state.model_name))

if model_name != st.session_state.model_name:
    st.session_state.model_name = model_name

uploads = st.sidebar.file_uploader(label='Enviar arquivos', type=['pdf'],
                                   accept_multiple_files=True)

if not uploads:
    st.info('Por favor, envie um arquivo para continuar')
    st.stop()

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [AIMessage(content='Olá, sou o seu assistente virtual! Como posso ajudá-lo?')]

if 'docs_list' not in st.session_state:
    st.session_state.docs_list = None

if 'retriever' not in st.session_state:
    st.session_state.retriever = None

for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message('AI'):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message('Human'):
            st.write(message.content)

start = time.time()
user_query = st.chat_input('Digite sua mensagem aqui...')
if ('' != user_query is not None) and uploads is not None:
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    with st.chat_message('Human'):
        st.markdown(user_query)
    with st.chat_message('AI'):
        if st.session_state.docs_list != uploads:
            st.session_state.docs_list = uploads
            st.session_state.retriever = config_retriever(uploads)

        rag_chain = config_rag_chain(st.session_state.model_name, st.session_state.retriever)
        result = rag_chain.invoke({'input': user_query, 'chat_history': st.session_state.chat_history})
        resp = result['answer']
        st.write(resp)

        # Sources
        for i, doc in enumerate(result['context']):
            source = doc.metadata['source']
            file = os.path.basename(source)
            page = doc.metadata.get('page', 'Página não especificada')
            ref = f":link: Fonte {i}: *{file} - p. {page}*"
            with st.popover(ref):
                st.caption(doc.page_content)
    
    st.session_state.chat_history.append(AIMessage(content=resp))

end = time.time()
print('Tempo: ', end - start)