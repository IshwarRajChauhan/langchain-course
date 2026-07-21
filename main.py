from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_core.messages import SystemMessage
from langchain_groq import ChatGroq
from tavily import TavilyClient
from langchain_tavily import TavilySearch

load_dotenv()


#### -------Using Tavily to search over the internet.-------

# tavily = TavilyClient()

# @tool
# def search(query: str) -> str:
#     """
#     Tool that searches over internet

#     Args:
#         query: The query to search for

#     Returns:
#         The search results
#     """
#     print(f"Searching for: {query}")
#     return tavily.search(query=query)
# tools = [search]

llm = ChatGroq(model="openai/gpt-oss-120b")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke({
    "messages": [
        SystemMessage(content=(
    "You only have access to one tool: `search`. "
    "You must call `search` AT MOST 3 times total, no more. "
    "After your 3rd search, you must stop searching and give your final answer "
    "using only the information you already have, even if incomplete."
    )),
        HumanMessage(content="Search for 3 job posting for AI Engineer internship in India on linkedin and provide detail with the links")
        ]
    })
    print(result)

if __name__ == "__main__":
    main()
