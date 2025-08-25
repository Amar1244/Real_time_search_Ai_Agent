# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv
# from langchain.agents import initialize_agent,tool
# from langchain_community.tools.tavily_search import TavilySearchResults
# import datetime

# load_dotenv ()

# llm  = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# search_tools = TavilySearchResults(search_depts="basic")
# @tool
# def get_system_time(format:str = "%Y-%m-%d %H:%M:%S"):
#     """Return the current date and time in specific format """
#     current_time = datetime.datetime.now( )
#     formatted_time = current_time.strftime(format)
#     return formatted_time


# tools = [search_tools,get_system_time]

# agent = initialize_agent(tools=tools,
#                          llm=llm,
#                          agent= "zero-shot-react-description",
#                          verbose = True)

# agent.invoke("when was spacex last lauched nad how many days ago from this instances")

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, tool
from langchain_community.tools.tavily_search import TavilySearchResults
import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Define search tool
search_tool = TavilySearchResults(search_depts="basic")

# Define custom tool to get system time
@tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """Return the current date and time in specific format"""
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime(format)
    return formatted_time

tools = [search_tool, get_system_time]

# Initialize agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

# Streamlit UI
st.title("LangChain + Gemini Agent UI")

st.write("Ask anything related to searches or time:")

user_input = st.text_input("Enter your query:")

if st.button("Ask Agent") and user_input:
    with st.spinner("Thinking..."):
        try:
            response = agent.invoke(user_input)
            st.success("Response received!")
            st.write(response)
        except Exception as e:
            st.error(f"Error: {e}")
