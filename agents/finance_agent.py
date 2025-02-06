from crewai import Agent, LLM
from crewai.tools import tool
from tools.finance_tools import scrape_tool,search_tool
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")



data_collector = Agent(
    role='Stock Price Data Collector',
    goal="Collect accurate and today's stock price",
    backstory="You are an expert in gathering today's stock price from various sources.",
    tools=[scrape_tool, search_tool],
    verbose=True,
    allow_delegation=True,
    llm=LLM(
        model="gemini/gemini-1.5-flash-8b",
        temperature=0.2
    )
)


report_writer = Agent(
    role='Finance Report Writer',
    goal=f"Compile findings into a brief report and give final output in  - 'Response: **Financial Analysis Report - Company Name (Company Symbol)**"

        f"**Stock Symbol:** Stock Symbol"

        f"**Current Stock Price:** in respective currency'",
    backstory='You are skilled at creating clear and concise financial reports.',
    llm=LLM(
        model="gemini/gemini-1.5-flash-8b",
        temperature=0.2
    )
)