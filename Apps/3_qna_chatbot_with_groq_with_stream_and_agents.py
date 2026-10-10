from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from serpapi_search_tools import news_search,web_search
from langchain.agents import create_agent
import streamlit as st
from langgraph.checkpoint.memory import MemorySaver

llm=ChatGroq(model="openai/gpt-oss-20b",streaming=True)
tools=[web_search(),news_search()]
if "memory" not in st.session_state :
    st.session_state.memory=MemorySaver()
    st.session_state.history=[]

agent=create_agent(
    model=llm,
    tools=tools,
    checkpointer=st.session_state.memory,
    system_prompt="You are the fastest chat agent"
)
## Streamlit
st.subheader("Ai chatbot")
st.markdown("Replying at the blink of eyes")
query=st.chat_input("Ask anything you love !")
if query:
    for message in st.session_state.history:
        role=message["role"]
        content=message["content"]
        st.chat_message(role).markdown(content)
    st.chat_message("User").markdown(query)
    st.session_state.history.append({"role":"user","content":query})
    res=agent.stream(
        {"messages":[{"role":"user","content":query}]},
        {"configurable":{"thread_id":"1"}},
        stream_mode="messages"
    )
    ai_container = st.chat_message("Ai")
    with ai_container:
        space= st.empty()
        message=""
        for chunk in res :
            message=message+chunk[0].content
            space.write(message)
    
        st.session_state.history.append({"role":"ai","content":message})

    