import os
import json
from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, HumanMessage
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

chat = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

intent_labels = ["financial", "news", "sentiment"]
sentiment_labels = ["Very Positive", "Positive", "Neutral", "Negative", "Very Negative"]

response_schemas = [
    ResponseSchema(name="intent", description=f"Classify the text into one of: {intent_labels}."),
    ResponseSchema(name="sentiment", description=f"Classify sentiment into: {sentiment_labels}.")
]

output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

def classify_text(text):
    prompt = f"""
    Classify the following text into:
    1. **Intent:** {intent_labels}.
    2. **Sentiment:** {sentiment_labels}.

    Text: "{text}"

    {output_parser.get_format_instructions()}
    """

    messages = [SystemMessage(content="You are an AI text classifier."), HumanMessage(content=prompt)]

    response = chat.invoke(messages)
    
    try:
        result = output_parser.parse(response.content)
        return result
    except Exception as e:
        return {"error": str(e), "raw_output": response.content}