from crewai import Agent, Task, Crew, Process
from agents.news_agent import news_researcher, news_reporter

news_research_task = Task(
    description="Gather the latest news articles related to {user_query} from credible sources.",
    agent=news_researcher,
    expected_output="A structured dataset containing news headlines, summaries, publication dates, and source links."
)

news_report_task = Task(
    description="Write a well-structured news report based on the collected news articles.",
    agent=news_reporter,
    expected_output="""A concise and well-formatted news report in the following structure:
    
    **Headline:** [News Headline]
    
    **Date:** [Today's Date]
    
    **Time:** [Time and Zone]
    
    **Summary:** [Brief summary of the news]
    
    **Source:** [Credible Source Name and Link]
    
    Do not include additional commentary or opinion."""
)
