import os


subdirs = ["agents", "tools"]
for subdir in subdirs:
    path = os.path.join(subdir)
    if not os.path.exists(path):
        os.makedirs(path)

files = {
    "main.py": "",
    "intent_classifier.py": "",
    "agent_router.py": "",
    "agents/finance_agent.py": "",
    "agents/weather_agent.py": "",
    "agents/news_agent.py": "",
    "agents/sentiment_agent.py": "",
    "agents/translation_agent.py": "",
    "tools/finance_tools.py": "",
    "tools/weather_tools.py": "",
    "tools/news_tools.py": "",
    "tools/sentiment_tools.py": "",
    "tools/translation_tools.py": "",
    "requirements.txt": ""
}

for file_path, content in files.items():
    full_path = os.path.join(file_path)
    with open(full_path, "w") as f:
        f.write(content)


main_py_content = """
from intent_classifier import IntentClassifier
from agent_router import AgentRouter

def main():
    # ... (Your main logic here)
    print("AI Agent Router started.")

if __name__ == "__main__":
    main()
"""

with open(os.path.join("main.py"), "w") as f:
    f.write(main_py_content)


requirements_content = """
transformers
yfinance
pyowm
# Add other dependencies as needed
"""

with open(os.path.join("requirements.txt"), "w") as f:
    f.write(requirements_content)
