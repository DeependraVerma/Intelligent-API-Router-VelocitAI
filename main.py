import streamlit as st
import os
import ast
from crewai import Crew, Task, Process
from agents.intent_classifier_agent import classify_text
from agent_router import route_to_agent
import google.generativeai as genai
from memory_handler import get_memory


genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
    "temperature": 0.2,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)


st.title("Intent-Based Query Router")
st.write("Enter your query below, and our AI agent will classify and process it.")


user_id = st.text_input("Enter your User ID:", value="user_123")
memory = get_memory(user_id)


def process_query(user_input, user_id):
    memory = get_memory(user_id)  # Load user-specific memory
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
            st.write(f"**{intent.capitalize()} Intent - {sentiment.capitalize()} Sentiment**")

            history = memory.load_memory_variables({}).get("chat_history", "")

            if isinstance(history, str):
                try:
                    history = ast.literal_eval(history)
                except Exception:
                    history = []
            if not isinstance(history, list):
                history = []

            response = route_to_agent(intent=intent, sentiment=sentiment, user_query=user_input, history=history)

            memory.save_context({"input": user_input}, {"output": response})

        else:
            st.write(f"Unrecognized intent: {intent}")
    except Exception as e:
        st.error(f"Error processing query: {str(e)}")

    return response, intent, sentiment

st.subheader("Chat History")
history = memory.load_memory_variables({}).get("chat_history", [])

if isinstance(history, str):
    try:
        history = ast.literal_eval(history)
    except Exception:
        history = []
if not isinstance(history, list):
    history = []

for chat in history:
    if isinstance(chat, dict):
        st.write(f"**You:** {chat.get('input', 'N/A')}")
        st.write(f"**Bot:** {chat.get('output', 'N/A')}")
        st.write("---")


user_input = st.text_input("Enter your query:")
if st.button("Submit"):
    if user_input:
        response, intent, sentiment = process_query(user_input, user_id)

        if response:
            chat_session = model.start_chat(history=[])

            if intent == "financial":
                prompt = (
                    f"Extract only the current stock price from the provided financial data in plain text. "
                    f"User query: {user_input}. "
                    f"Response Data: {response}. "
                    f"Only return the stock price value with its currency symbol."
                    f"Example - The Stock Price for NVIDIA is - 50.00 USD"
                )
            elif intent == "news":
                prompt = (
                    f"Summarize the key highlights from the news data provided in plain text. "
                    f"User query: {user_input}. "
                    f"Response Data: {response}. "
                    f"Extract the top 3 key points relevant to the news topic."
                )
            elif intent == "sentiment":
                prompt = (
                    f"Analyze and summarize the sentiment of the provided text in one sentence. "
                    f"User query: {user_input}. "
                    f"Response Data: {response}. "
                    f"Provide a short and precise sentiment summary."
                )
            else:
                prompt = "Unexpected intent. Please refine the query."

            ai_response = chat_session.send_message(prompt)

            st.success("Response:")
            st.write(ai_response.text)
        else:
            st.warning("No response generated.")
    else:
        st.error("Please enter a query.")
