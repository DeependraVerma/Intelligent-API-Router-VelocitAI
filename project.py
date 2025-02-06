import os

def create_directory_structure(base_path):
    directories = [
        "agents",
        "tasks",
        "tools"
    ]
    
    files = {
        "README.md": "# Intelligent API Router - Velocitai\n\nThis project is designed to route user requests to appropriate agents based on intent classification.",
        "LICENSE": "MIT License\n\nCopyright (c) 2024",
        "agent_router.py": "# Handles routing of user queries to appropriate agents.",
        "main.py": "# Entry point of the application.",
        "memory_handler.py": "# Manages user memory for context persistence.",
        "project.py": "# Script to initialize project structure.",
        "requirements.txt": "# List dependencies here.",
        "user_memory.json": "{}"
    }
    
    agent_files = [
        "finance_agent.py", "intent_classifier_agent.py", "news_agent.py", 
        "sentiment_agent.py", "translation_agent.py", "weather_agent.py"
    ]
    
    task_files = [
        "finance_task.py", "news_task.py", "tasks.py"
    ]
    
    tool_files = [
        "finance_tools.py", "news_tools.py", "sentiment_tools.py", "translation_tools.py", "weather_tools.py"
    ]
    
    # Create directories
    for directory in directories:
        dir_path = os.path.join(base_path, directory)
        os.makedirs(dir_path, exist_ok=True)
    
    # Create files
    for file_name, content in files.items():
        file_path = os.path.join(base_path, file_name)
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(content)
    
    # Create agent files
    for file_name in agent_files:
        file_path = os.path.join(base_path, "agents", file_name)
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(f"# {file_name} - Implements agent logic\n")
    
    # Create task files
    for file_name in task_files:
        file_path = os.path.join(base_path, "tasks", file_name)
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(f"# {file_name} - Defines tasks for agents\n")
    
    # Create tool files
    for file_name in tool_files:
        file_path = os.path.join(base_path, "tools", file_name)
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(f"# {file_name} - Utility tools for agents\n")

if __name__ == "__main__":
    base_directory = os.path.dirname(os.path.abspath(__file__))
    create_directory_structure(base_directory)
    print("Project structure initialized successfully!")
