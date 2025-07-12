# Example Source: https://python.langchain.com/v0.2/docs/integrations/memory/google_firestore/

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, BaseMessage
from SystemMessage import SYSTEM_MESSAGE_CONTENT

load_dotenv()

# Initialize Chat Model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

def get_model_response_no_memory(messages_list: list):
    """Invokes the Gemini model with a list of messages and returns the AI's content.
    This function does NOT integrate with any persistent memory (MySQL/Firestore).
    """
    result = model.invoke(messages_list)
    return result.content

def get_chat_response_for_ui(message, chat_history):
    # Note: This function does NOT integrate with the MySQL history saving from the original file.
    # It provides a basic chat interface with the Gemini model.
    messages: list[BaseMessage] = [SystemMessage(content=SYSTEM_MESSAGE_CONTENT)]
    for item in chat_history:
        if item["role"] == "user":
            messages.append(HumanMessage(content=item["content"]))
        elif item["role"] == "assistant":
            messages.append(AIMessage(content=item["content"]))
    messages.append(HumanMessage(content=message))

    response = get_model_response_no_memory(messages)
    return response

if __name__ == "__main__":
    # The original memory integration logic is removed for this example.
    # This block demonstrates basic model invocation without memory.
    print("This script now only demonstrates basic model invocation without memory.")
    print("To use memory, you would need to integrate with a database like MySQL or Firestore.")

    messages = [
        SystemMessage(content=SYSTEM_MESSAGE_CONTENT),
        HumanMessage(content="Hello, how are you?")
    ]
    response = get_model_response_no_memory(messages)
    print(f"AI: {response}")
