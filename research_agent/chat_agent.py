from agno.agent import Agent 
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools import tool
from agno.models.groq import Groq 
from dotenv import load_dotenv

load_dotenv()

agent=Agent(
    name='Research Agent',
    model=Groq(id='llama-3.1-8b-instant'),
    tools=[DuckDuckGoTools()],
    description="""
    Always run the search tool first for the query.

    Return 3-5 relevant links with titles and URLs.

    Summarize findings in concise bullet-point format with inline sources.

    """,
    markdown=True)

agent.print_response("Research three recent articles about Agentic AI, list titles + links and then summarize them")

if __name__=="__main__":
    agent.print_response(
        "Research three recent articles about Agentic AI"
    )