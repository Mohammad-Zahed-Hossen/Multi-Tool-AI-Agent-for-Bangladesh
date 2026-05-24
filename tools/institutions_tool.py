from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

db = SQLDatabase.from_uri(
    "sqlite:///databases/institutions.db"
)

institutions_chain = SQLDatabaseChain.from_llm(
    llm=llm,
    db=db,
    verbose=True,
    return_direct = False,
    use_query_checker=True
)

def query_institutions(question):

    try:
        response = institutions_chain.invoke({
            "query": question
        })

        return response["result"]

    except Exception as e:
        return f"Error: {str(e)}"


