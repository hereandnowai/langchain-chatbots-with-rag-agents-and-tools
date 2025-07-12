# Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/
# OpenAI Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/openai/

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env
load_dotenv()

# Initialize the ChatGoogleGenerativeAI model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

def invoke_gemini_model(message):
    """Invokes the Gemini model with the given message and returns the content."""
    result = model.invoke(message)
    return result.content

if __name__ == "__main__":
    # Example usage when run directly
    result_content = invoke_gemini_model("What is 25 divided by 5?")
    print("Content only:")
    print(result_content)