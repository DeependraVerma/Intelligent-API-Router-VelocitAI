import streamlit as st
import os
import ast
from crewai import Crew, Task, Process
from agents.intent_classifier_agent import classify_text
from agent_router import route_to_agent
import google.generativeai as genai

def process_query(user_input):
    output_str = classify_text(user_input)

    response = None

    try:
        if isinstance(output_str, str):
            output_dict = ast.literal_eval(output_str)
        elif isinstance(output_str, dict):
            output_dict = output_str
        else:
            raise ValueError("Invalid input format. Expected a dictionary or string.")

        intent = output_dict.get("intent", "").lower()
        sentiment = output_dict.get("sentiment", "").lower()
        valid_intents = ["financial", "news", "sentiment"]

        if intent in valid_intents:
            st.write(f"{intent.capitalize()} Intent - {sentiment.capitalize()} Sentiment")
            response = route_to_agent(intent=intent, sentiment=sentiment, user_query=user_input)
        else:
            st.write(f"Unrecognized intent: {intent}")
    except Exception as e:
        st.error(f"Error processing query: {str(e)}")

    return response, intent, sentiment

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 0.2,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)


st.title("Intent-Based Query Router")
st.write("Enter your query below, and our AI agent will classify and process it.")

user_input = st.text_input("Enter your query:")
if st.button("Submit"):
    if user_input:
        response, intent, sentiment = process_query(user_input)
        
        if response:
            chat_session = model.start_chat(history=[])
            
            if intent == "financial":
                prompt = (
                    f"Extract only the current stock price from the provided financial data in plain text. "
                    f"User query: {user_input}. "
                    f"Response Data: {response}. "
                    f"Only return the stock price value with its currency symbol. Do not include any extra text, metadata, or formatting."
                    f"Example - The Stock Price for NVIDIA is - 50.00 USD"
                )

            elif intent == "news":
                prompt = (
                    f"Summarize the key highlights from the news data provided in plain text. "
                    f"User query: {user_input}. "
                    f"Response Data: {response}. "
                    f"Extract the top 3 key points relevant to the news topic without any metadata or extra formatting."
                    f"Example - 1. [Key news point 1]\n2. [Key news point 2]\n3. [Key news point 3]"
                )

            elif intent == "sentiment":
                prompt = (
                    f"Analyze and summarize the sentiment of the provided text in one sentence. "
                    f"User query: {user_input}. "
                    f"Response Data: {response}. "
                    f"Provide a short and precise sentiment summary such as: 'The overall sentiment is Positive with strong optimism about [topic].'"
                )

            else:
                prompt = "Unexpected intent. Please refine the query."

            response = chat_session.send_message(prompt)

            st.success("Response:")
            st.write(response.text)
        else:
            st.warning("No response generated.")
    else:
        st.error("Please enter a query.")
