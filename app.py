import streamlit as st
from langchain_community.llms import Ollama

@st.cache_resource
def load_model():
    return Ollama(model="llama3")

llm = load_model()

st.title("LangChain + Ollama Chatbot")

user_input = st.text_input("Ask something")

if st.button("Send"):
    if user_input:
        try:
            with st.spinner("Thinking..."):
                response = llm.invoke(user_input)
            st.success("Answer:")
            st.write(response)
        except Exception as e:
            st.error(f"Error: {e}")