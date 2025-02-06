# Intent-Based Query Router

## Overview
This project is an AI-powered intent classification and query routing system built using Streamlit, CrewAI, and Google's Gemini 1.5 Pro model. It classifies user queries into predefined intents (Financial, News, Sentiment) and processes them accordingly to generate relevant responses.

## Features
- Classifies user queries into three intents: **Financial**, **News**, and **Sentiment**.
- Uses **CrewAI** for routing queries to appropriate agents.
- Utilizes **Google Gemini 1.5 Pro** for response generation.
- Implements **Streamlit** for an interactive UI.
- Ensures structured output for stock prices, news summaries, and sentiment analysis.

## Tech Stack
- **Python**
- **Streamlit**
- **CrewAI**
- **Google Generative AI SDK (Gemini 1.5 Pro)**
- **AST (Abstract Syntax Trees)**
- **OS (Environment Variable Handling)**

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/DeependraVerma/Intelligent-API-Router-VelocitAI.git
   cd intent-query-router
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the Google Generative AI API key:
   ```bash
   export GEMINI_API_KEY='your_api_key_here'  # On Windows: set GEMINI_API_KEY=your_api_key_here
   ```

## Usage
1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Enter a query in the text box and click **Submit**.
3. The system classifies the intent and generates a relevant response.

## File Structure
```
Directory structure:
└── deependraverma-intelligent-api-router-velocitai/
    ├── README.md
    ├── LICENSE
    ├── agent_router.py
    ├── main.py
    ├── memory_handler.py
    ├── project.py
    ├── requirements.txt
    ├── user_memory.json
    ├── agents/
    │   ├── finance_agent.py
    │   ├── intent_classifier_agent.py
    │   ├── news_agent.py
    │   ├── sentiment_agent.py
    │   ├── translation_agent.py
    │   └── weather_agent.py
    ├── tasks/
    │   ├── finance_task.py
    │   ├── news_task.py
    │   └── tasks.py
    └── tools/
        ├── finance_tools.py
        ├── news_tools.py
        ├── sentiment_tools.py
        ├── translation_tools.py
        └── weather_tools.py

```

## Example Queries
- **Financial:** "What is the stock price of NVIDIA today?"
- **News:** "What are the latest updates on the tech industry?"
- **Sentiment:** "How are people reacting to Apple's latest iPhone release?"

## Contributing
Feel free to open issues or submit pull requests for enhancements.

## License
This project is licensed under the MIT License.

## Contact
For any questions, reach out at [your_email@example.com](mailto:deependra.verma00@gmail.com).

