
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from serpapi_search_tools import news_search,web_search
from langchain.agents import create_agent

llm=ChatGroq(model="openai/gpt-oss-20b")
agent= create_agent(model=llm,tools=[web_search(),news_search()],
                    system_prompt="You are who uses the tools to search for information if not available")

while True:
    query=input("User: ")
    if query.lower() in ["exit","bye"]:
        print("good bye ! Hope to see u soon")
        break;
    print(query);
    print("\n")
    res=agent.invoke({"messages":[{"role":"user","content":query}]})
    print("Ai: ",res["messages"][-1].content)

    
