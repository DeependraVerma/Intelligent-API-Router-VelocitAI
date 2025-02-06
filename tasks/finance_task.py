from crewai import Agent, Task, Crew, Process
from agents.finance_agent import data_collector, report_writer

data_collector_task = Task(
    description='Collect stock price data for {user_query}',
    agent=data_collector,
    expected_output="A structured dataset containing stock prices of the company asked by user."
)



report_writer_task = Task(
    description='Write the brief report for the stock price asked by the user',
    agent=report_writer,
    expected_output="""A well-structured financial report summarizing the analysis in the format - 
    Compile findings into a brief report and give final output in  - 
    'Response: **Financial Analysis Report - Company Name (Company Symbol)**"

        f"**Stock Symbol:** Stock Symbol"

        f"**Current Stock Price:** in respective currency'"""
)
