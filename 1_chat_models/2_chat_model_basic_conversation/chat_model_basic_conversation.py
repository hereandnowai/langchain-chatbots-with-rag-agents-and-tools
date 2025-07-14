from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, BaseMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import sys
import os

# Add the project root to sys.path to allow importing SystemMessage
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from sm import ai_teacher

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

def get_chat_response_for_ui(message, chat_history):
    messages: list[BaseMessage] = [SystemMessage(content=ai_teacher)]
    for item in chat_history:
        if item["role"] == "user":
            messages.append(HumanMessage(content=item["content"]))
        elif item["role"] == "assistant":
            messages.append(AIMessage(content=item["content"]))
    messages.append(HumanMessage(content=message))
    result = model.invoke(messages)
    return result.content

if __name__ == "__main__":
    print(f"Answer 1: {model.invoke([SystemMessage(content=ai_teacher), HumanMessage(content='What does GPT stand for?')]).content}")
    print(f"Answer 2: {model.invoke([SystemMessage(content=ai_teacher), HumanMessage(content='Explain deep learning in a single line')]).content}")