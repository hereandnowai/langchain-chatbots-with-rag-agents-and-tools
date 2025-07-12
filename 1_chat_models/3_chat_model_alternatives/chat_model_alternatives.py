from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

# Setup environment variables
load_dotenv()

# ---- Google Chat Model Example ----

# https://console.cloud.google.com/gen-app-builder/engines
# https://ai.google.dev/gemini-api/docs/models/gemini
_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

def get_google_gemini_response(message: str) -> str:
    messages = [
        SystemMessage(content="You are a helpful AI assistant."),
        HumanMessage(content=message),
    ]
    result = _model.invoke(messages)
    return result.content

if __name__ == "__main__":
    # Example usage when run directly
    response = get_google_gemini_response("What is 81 divided by 9?")
    print(f"Answer from Google: {response}")
