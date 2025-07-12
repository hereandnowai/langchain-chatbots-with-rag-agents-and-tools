# Example Source: https://python.langchain.com/v0.2/docs/integrations/memory/google_firestore/

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

load_dotenv()

# Initialize Chat Model
_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

def get_model_response_no_memory(messages_list: list) -> str:
    """Invokes the Gemini model with a list of messages and returns the AI's content.
    This function does NOT integrate with any persistent memory (Firebase/Firestore).
    """
    result = _model.invoke(messages_list)
    return result.content

def get_chat_response_for_ui(message, chat_history):
    # Note: This function does NOT integrate with the Firebase history saving from the original file.
    # It provides a basic chat interface with the Gemini model.
    messages = [SystemMessage(content="You are a helpful AI assistant.")]
    for human, ai in chat_history:
        messages.append(HumanMessage(content=human))
        messages.append(AIMessage(content=ai))
    messages.append(HumanMessage(content=message))

    response = get_model_response_no_memory(messages)
    return response

if __name__ == "__main__":
    # The original memory integration logic is removed for this example.
    # This block demonstrates basic model invocation without memory.
    print("This script now only demonstrates basic model invocation without memory.")
    print("To use memory, you would need to integrate with a database like Firebase/Firestore.")

    messages = [
        SystemMessage(content="You are a helpful AI assistant."),
        HumanMessage(content="Hello, how are you?")
    ]
    response = get_model_response_no_memory(messages)
    print(f"AI: {response}")
