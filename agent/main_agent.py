import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import Tool
from langchain.agents.agent import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain import hub

from tools.institutions_tool import query_institutions
from tools.hospitals_tool import query_hospitals
from tools.restaurants_tool import query_restaurants
from tools.web_search_tool import web_search

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

tools = [

    Tool(
        name="InstitutionsDBTool",
        func=query_institutions,
        description="""
Useful for questions about:
- schools
- colleges
- universities
- madrasas
- educational institutions
- EIIN
- MPO status
- institutional statistics
- educational divisions/districts
"""
    ),

    Tool(
        name="HospitalsDBTool",
        func=query_hospitals,
        description="""
Useful for questions about:
- hospitals
- clinics
- healthcare facilities
- private hospitals
- government hospitals
- hospitals in districts/divisions
"""
    ),

    Tool(
        name="RestaurantsDBTool",
        func=query_restaurants,
        description="""
Useful for questions about:
- restaurants
- food places
- ratings
- restaurant locations
- restaurant reviews
- top rated restaurants
"""
    ),

    Tool(
        name="WebSearchTool",
        func=web_search,
        description="""
Useful for:
- general knowledge
- Bangladesh healthcare policy
- DGHS
- cultural context
- definitions
- government policies
- topics NOT available in databases
"""
    )
]

prompt = hub.pull("hwchase17/react")

agent = create_react_agent(llm, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

print("\nMulti-Tool AI Agent for Bangladesh")
print("Type 'exit' to quit.\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    try:

        response = agent_executor.invoke({"input": user_input})

        print("\nAI Agent:")
        print(response["output"])

    except Exception as e:

        print(f"\nError: {str(e)}")

