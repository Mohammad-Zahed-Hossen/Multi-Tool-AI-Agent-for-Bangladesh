import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dotenv import load_dotenv
import json

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import Tool
from langchain_core.messages import HumanMessage

from tools.institutions_tool import query_institutions
from tools.hospitals_tool import query_hospitals
from tools.restaurants_tool import query_restaurants
from tools.web_search_tool import web_search

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

tools = [
    Tool(
        name="InstitutionsDBTool",
        func=query_institutions,
        description="""
MANDATORY tool for ANY query related to:
- colleges
- schools
- universities
- madrasas
- educational institutions
- EIIN
- MPO
- institution counts
- institutions in districts/divisions
- education statistics

DO NOT answer from general knowledge.
ALWAYS use this tool for institution-related questions.
"""
    ),
    Tool(
        name="HospitalsDBTool",
        func=query_hospitals,
        description="""
MANDATORY tool for ANY query related to:
- hospitals
- clinics
- healthcare facilities
- private hospitals
- government hospitals
- hospitals in districts/divisions
- healthcare statistics

DO NOT answer from general knowledge.
ALWAYS use this tool for hospital-related questions.
"""
    ),
    Tool(
        name="RestaurantsDBTool",
        func=query_restaurants,
        description="""
MANDATORY tool for ANY query related to:
- restaurants
- food places
- restaurant ratings
- restaurant reviews
- top restaurants
- restaurant locations

DO NOT answer from general knowledge.
ALWAYS use this tool for restaurant-related questions.
"""
    ),
    Tool(
        name="WebSearchTool",
        func=web_search,
        description="""
Use ONLY for:
- general knowledge
- Bangladesh policies
- DGHS
- definitions
- cultural context
- topics NOT present in databases

DO NOT use for institution/hospital/restaurant statistics.
"""
    )
]

tool_dict = {tool.name: tool for tool in tools}

def process_input(user_input):
    try:
        response = llm.invoke([HumanMessage(content=user_input)])
        return response.content
    except Exception as e:
        return f"Error: {str(e)}"

print("\nMulti-Tool AI Agent for Bangladesh")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    try:
        response = process_input(user_input)
        print("\nAI Agent:")
        print(response)
    except Exception as e:
        print(f"\nError: {str(e)}")


