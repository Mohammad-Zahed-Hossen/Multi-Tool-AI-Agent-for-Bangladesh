from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()


# =========================
# LOAD TAVILY CLIENT
# =========================
client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


# =========================
# WEB SEARCH FUNCTION
# =========================
def web_search(query):

    try:

        response = client.search(
            query=query,
            search_depth="advanced",
            max_results=5
        )

        results = response["results"]

        formatted_results = []

        for item in results:

            formatted_results.append(
                f"""
Title: {item['title']}

Content: {item['content']}

URL: {item['url']}
"""
            )

        return "\n\n".join(formatted_results)

    except Exception as e:
        return f"Web Search Error: {str(e)}"
