from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
llm = GoogleGenerativeAI(model="gemini-3.8-flash")


st.title("Ai chat-bot")

st.markdown("First chat bot using langchain and gemini")
for message in st.session_state.messages:
    role=message["role"]
    content=message["content"]
    st.chat_message(role).markdown(content)


if "messages" not in st.session_state:
    st.session_state.messages=[]


query =st.chat_input("Ask anything baccha")
if query : 
    st.chat_message("user").markdown(query)
    st.session_state.messages.append({"role":"user","content":query})
    result=llm.invoke(query)
    st.chat_message("ai").markdown(result)
    st.session_state.messages.append({"role":"ai","content":result})





