from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, BaseMessage
from SystemMessage import SYSTEM_MESSAGE_CONTENT

# Load environment variables from .env
load_dotenv()

# Create a ChatGoogleGenerativeAI model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

def get_conversation_response_with_history(chat_history_messages: list):
    """Invokes the Gemini model with the full chat history and returns the AI's content."""
    result = model.invoke(chat_history_messages)
    return result.content

def get_chat_response_for_ui(message, chat_history):
    messages: list[BaseMessage] = [SystemMessage(content=SYSTEM_MESSAGE_CONTENT)]
    for item in chat_history:
        if item["role"] == "user":
            messages.append(HumanMessage(content=item["content"]))
        elif item["role"] == "assistant":
            messages.append(AIMessage(content=item["content"]))
    messages.append(HumanMessage(content=message))

    bot_message = get_conversation_response_with_history(messages)
    return bot_message

if __name__ == "__main__":
    chat_history = []  # Use a list to store messages

    # Set an initial system message (optional)
    system_message = SystemMessage(content=SYSTEM_MESSAGE_CONTENT)
    chat_history.append(system_message)  # Add system message to chat history

    print("Start chatting with the AI. Type 'exit' to quit.")

    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break
        chat_history.append(HumanMessage(content=query))  # Add user message

        # Get AI response using history
        response = get_conversation_response_with_history(chat_history)
        chat_history.append(AIMessage(content=response))  # Add AI message

        print(f"AI: {response}")

    print("---- Message History ----")
    print(chat_history)
