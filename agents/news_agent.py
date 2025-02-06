from crewai import Agent, LLM
from crewai.tools import tool
from tools.finance_tools import scrape_tool, search_tool
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

news_researcher = Agent(
    role='News Researcher',
    goal='Collect accurate and up-to-date news articles on various topics.',
    backstory='You are an expert in gathering news from multiple sources, ensuring credibility and relevance.',
    tools=[scrape_tool, search_tool],
    verbose=True,
    allow_delegation=True,
    llm=LLM(
        model="gemini/gemini-1.5-flash-8b",
        temperature=0.2
    )
)

news_reporter = Agent(
    role='News Reporter',
    goal="Compile collected news into a structured and engaging news report. The final output should be formatted as: \n\n"
         "**Headline:** [News Headline]\n\n"
         "**Date:** [Today's Date]\n\n"
         "**Time:** [Time and Zone]\n\n"
         "**Summary:** [Brief summary of the news]\n\n"
         "**Source:** [Credible Source Name and Link]",
    backstory='You specialize in writing clear and engaging news reports for a broad audience.',
    llm=LLM(
        model="gemini/gemini-1.5-flash-8b",
        temperature=0.2
    )
)
