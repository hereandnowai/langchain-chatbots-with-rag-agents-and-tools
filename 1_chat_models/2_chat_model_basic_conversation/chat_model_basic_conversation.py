# Three types of messages to know:
# 1. System Messages - broad context for the conversation.
# 2. human messages
# 3. ai messages

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, BaseMessage
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env
load_dotenv()

# Create a ChatGoogleGenerativeAI model
_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

def get_conversation_response(messages_list):
    """Invokes the Gemini model with a list of messages and returns the AI's content."""
    result = _model.invoke(messages_list)
    return result.content

def get_chat_response_for_ui(message, chat_history):
    messages = []
    messages.append(SystemMessage(content="You are a helpful AI assistant."))
    for human, ai in chat_history:
        messages.append(HumanMessage(content=human))
        messages.append(AIMessage(content=ai))
    messages.append(HumanMessage(content=message))

    bot_message = get_conversation_response(messages)
    chat_history.append((message, bot_message))
    return bot_message

if __name__ == "__main__":
    messages = [
        SystemMessage(content="Solve the following math problems"),
        HumanMessage(content="What is 81 divided by 9?"),
    ]
    print(f"Answer from AI: {get_conversation_response(messages)}")

    messages.extend([
        AIMessage(content="81 divided by 9 is 9."),
        HumanMessage(content="What is 10 times 5?"),
    ])
    print(f"Answer from AI: {get_conversation_response(messages)}")