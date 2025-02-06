import json
import os
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import StreamlitChatMessageHistory

MEMORY_FILE = "user_memory.json"


user_memory_store = {}


if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as file:
        try:
            user_memory_store = json.load(file)
        except json.JSONDecodeError:
            user_memory_store = {}

def save_memory_to_file():
    with open(MEMORY_FILE, "w") as file:
        json.dump(user_memory_store, file, indent=4)

def get_memory(user_id):
    if user_id not in user_memory_store:
        chat_history = StreamlitChatMessageHistory()
        user_memory_store[user_id] = {"history": []}
    else:
        chat_history = StreamlitChatMessageHistory()
        chat_history.messages = user_memory_store[user_id]["history"]

    memory = ConversationBufferMemory(memory_key="history", chat_memory=chat_history)
    return memory

def save_user_message(user_id, user_input, response):
    if user_id in user_memory_store:
        user_memory_store[user_id]["history"].append({"input": user_input, "output": response})
    else:
        user_memory_store[user_id] = {"history": [{"input": user_input, "output": response}]}
    
    save_memory_to_file()
