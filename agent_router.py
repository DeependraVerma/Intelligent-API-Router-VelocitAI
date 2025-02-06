
from crewai import Crew, Task, Process
from agents.intent_classifier_agent import classify_text
from agents.finance_agent import data_collector,report_writer
from tasks.finance_task import data_collector_task,report_writer_task
from agents.news_agent import news_reporter,news_researcher
from tasks.news_task import news_report_task,news_research_task
import ast

def route_to_agent(intent, sentiment, user_query, history=None):
    if str(intent) == "financial":
        print("Routing to Financial Agent")
        financial_crew = Crew(
            agents=[data_collector, report_writer],
            tasks=[data_collector_task, report_writer_task],
            process=Process.sequential
        )
        financial_crew_report = financial_crew.kickoff(inputs={'user_query': user_query, 'history': history})
        return f"The user sentiment for this text is: {sentiment}. The Financial Report: \n\n {financial_crew_report}"
    
    elif str(intent) == "news":
        print("Routing to News Agent")
        news_crew = Crew(
            agents=[news_reporter, news_researcher],
            tasks=[news_report_task, news_research_task],
            process=Process.sequential
        )
        news_crew_report = news_crew.kickoff(inputs={'user_query': user_query, 'history': history})
        return f"The user sentiment for this text is: {sentiment}. The News Report: \n\n {news_crew_report}"
    
    elif str(sentiment) in ["very positive", "positive", "neutral", "negative", "very negative"]:
        print("Routing to Sentiment Agent")
        return f"The sentiment of this text is: {sentiment}"
    
    else:
        print(f"Unknown intent: {intent}. No agent available.")
        return None
