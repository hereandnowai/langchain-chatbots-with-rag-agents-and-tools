from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_community.chat_models import ChatOllama # For local/open-source models via Ollama
from langchain_core.messages import HumanMessage, SystemMessage, BaseMessage
from SystemMessage import SYSTEM_MESSAGE_CONTENT
from typing import Optional

# Setup environment variables
load_dotenv()

# --- Helper function to create messages for models ---
def create_messages(user_message: str) -> list[BaseMessage]:
    return [
        SystemMessage(content=SYSTEM_MESSAGE_CONTENT),
        HumanMessage(content=user_message),
    ]

# ---- Google Gemini Chat Model Example ----

# https://console.cloud.google.com/gen-app-builder/engines
# https://ai.google.dev/gemini-api/docs/models/gemini
gemini_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

def get_gemini_response(user_message: str):
    messages = create_messages(user_message)
    result = gemini_model.invoke(messages)
    return result.content

# ---- OpenAI Chat Model Example ----

# Requires OPENAI_API_KEY environment variable
# Models: gpt-4o, gpt-4-turbo, gpt-3.5-turbo, etc.
openai_model = ChatOpenAI(model="gpt-4o")

def get_openai_response(user_message: str):
    messages = create_messages(user_message)
    result = openai_model.invoke(messages)
    return result.content

# ---- Anthropic Chat Model Example ----

# Requires ANTHROPIC_API_KEY environment variable
# Models: claude-3-opus-20240229, claude-3-sonnet-20240229, claude-3-haiku-20240307, etc.
# Uncomment the line below and set your model if you have an Anthropic API key
anthropic_model: Optional[ChatAnthropic] = None # Initialize to None to satisfy Pylance
# _anthropic_model = ChatAnthropic(model="claude-3-sonnet-20240229")

def get_anthropic_response(user_message: str):
    # Check if Anthropic model is initialized
    if 'anthropic_model' not in globals():
        return "Anthropic model not initialized. Please uncomment and configure it if you have an API key."
    messages = create_messages(user_message)
    # result = anthropic_model.invoke(messages)
    # return result.content

# ---- Open-source Models via Ollama Example ----

# Requires Ollama to be installed and running locally.
# Download Ollama: https://ollama.com/
# Pull models: ollama pull mistral, ollama pull llama2, ollama pull qwen, ollama pull deepseek-coder
# Example models: mistral, llama2, qwen, deepseek-coder

def get_ollama_response(user_message: str, model_name: str = "llama2"):
    try:
        ollama_model = ChatOllama(model=model_name)
        messages = create_messages(user_message)
        result = ollama_model.invoke(messages)
        return result.content
    except Exception as e:
        return f"Error with Ollama model '{model_name}': {e}. Make sure Ollama is running and the model is pulled."

if __name__ == "__main__":
    test_query = "What is the capital of France?"

    print("\n--- Testing Google Gemini ---")
    gemini_response = get_gemini_response(test_query)
    print(f"Gemini: {gemini_response}")

    print("\n--- Testing OpenAI ---")
    try:
        openai_response = get_openai_response(test_query)
        print(f"OpenAI: {openai_response}")
    except Exception as e:
        print(f"OpenAI Error: {e}. Make sure OPENAI_API_KEY is set in your .env file.")

    print("\n--- Testing Anthropic ---")
    anthropic_response = get_anthropic_response(test_query)
    print(f"Anthropic: {anthropic_response}")

    print("\n--- Testing Ollama (Llama2) ---")
    ollama_llama_response = get_ollama_response(test_query, model_name="llama2")
    print(f"Ollama (Llama2): {ollama_llama_response}")

    print("\n--- Testing Ollama (Mistral) ---")
    ollama_mistral_response = get_ollama_response(test_query, model_name="mistral")
    print(f"Ollama (Mistral): {ollama_mistral_response}")

    print("\n--- Testing Ollama (Qwen) ---")
    ollama_qwen_response = get_ollama_response(test_query, model_name="qwen")
    print(f"Ollama (Qwen): {ollama_qwen_response}")

    print("\n--- Testing Ollama (Deepseek) ---")
    ollama_deepseek_response = get_ollama_response(test_query, model_name="deepseek-coder")
    print(f"Ollama (Deepseek): {ollama_deepseek_response}")