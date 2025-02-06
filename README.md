# Intent-Based Query Router

This application demonstrates an intent-based query routing system using Streamlit, CrewAI, and Google Gemini.  It takes user input, classifies the intent and sentiment, routes the query to the appropriate agent, and then uses Google Gemini to refine and present the response.

## Features

* **Intent Classification:** Classifies user queries into predefined intents (currently financial, news, sentiment) using a custom agent (`intent_classifier_agent`).
* **Sentiment Analysis:** Determines the sentiment (positive, negative, neutral) associated with the query.
* **Agent Routing:** Routes the query to a specific agent based on the classified intent and sentiment.  This allows for specialized processing and responses.
* **Google Gemini Integration:** Leverages the power of Google Gemini to further process the agent's response, providing concise and relevant information to the user.  This includes extracting key information (financial data), summarizing news, and providing sentiment summaries.
* **Streamlit UI:** Provides a user-friendly interface for inputting queries and viewing responses.


## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
content_copy
download
Use code with caution.
Markdown

Navigate to the project directory:

cd <project_directory>
content_copy
download
Use code with caution.
Bash

Install required libraries:

pip install -r requirements.txt
content_copy
download
Use code with caution.
Bash

Set up environment variables:

Create a .env file in the project directory.

Add your Gemini API key:

GEMINI_API_KEY=<your_gemini_api_key>
content_copy
download
Use code with caution.
Usage

Run the Streamlit app:

streamlit run app.py
content_copy
download
Use code with caution.
Bash

Enter your query in the text input field.

Click the "Submit" button.

The app will classify the intent and sentiment, route the query, and display the processed response.

Examples

Financial: "What's the current price of NVIDIA stock?"

News: "Give me the latest news on Apple."

Sentiment: "I'm so excited about the new iPhone!"

Architecture

User Input: The user enters a query via the Streamlit interface.

Intent and Sentiment Classification: The intent_classifier_agent classifies the intent and sentiment of the query.

Agent Routing: The agent_router directs the query to the appropriate agent based on the classified intent and sentiment. (Placeholder agents are assumed in this example; you'll need to implement your own.)

Agent Response: The selected agent processes the query and returns a response.

Gemini Processing: The response is passed to Google Gemini with a tailored prompt based on the intent. Gemini refines the response to extract key information, summarize, or provide a sentiment overview.

Output: The processed response from Gemini is displayed in the Streamlit app.

Further Development

Implement Agents: Develop specific agents for each intent (financial, news, sentiment) to handle queries and retrieve relevant data.

Error Handling: Enhance error handling to provide more informative messages to the user.

Expand Intents: Add more intents to support a wider range of queries.

Improve Prompt Engineering: Refine the prompts used with Google Gemini to optimize the quality and relevance of the responses.

Integration with CrewAI: Integrate more deeply with CrewAI for task management and process automation.

Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.

content_copy
download
Use code with caution.