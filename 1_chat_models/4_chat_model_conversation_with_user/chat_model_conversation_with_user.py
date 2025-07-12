from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, BaseMessage
import sys
import os

# Add the project root to sys.path to allow importing SystemMessage
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from SystemMessage import SYSTEM_MESSAGE_CONTENT

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

def get_chat_response_for_ui(message, chat_history):
    messages: list[BaseMessage] = [SystemMessage(content=SYSTEM_MESSAGE_CONTENT)]
    for item in chat_history:
        if item["role"] == "user":
            messages.append(HumanMessage(content=item["content"]))
        elif item["role"] == "assistant":
            messages.append(AIMessage(content=item["content"]))
    messages.append(HumanMessage(content=message))
    result = model.invoke(messages)
    return result.content

if __name__ == "__main__":
    chat_history_console = []
    print("Start chatting with the AI. Type 'exit' to quit.")
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break
        response = get_chat_response_for_ui(query, chat_history_console)
        chat_history_console.append({"role": "user", "content": query})
        chat_history_console.append({"role": "assistant", "content": response})
        print(f"AI: {response}")
    print("---- Message History ----")
    print(chat_history_console)