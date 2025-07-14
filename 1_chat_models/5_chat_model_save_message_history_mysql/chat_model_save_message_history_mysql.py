# chat_model_save_message_history_mysql.py - Concise version
import os, sys, json
from dotenv import load_dotenv
import mysql.connector
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, BaseMessage
from typing import cast, Dict, Any

# Setup path for SystemMessage.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from sm import ai_teacher

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Database Configuration
DB_CONFIG = {
    "host": os.getenv("MYSQL_HOST"),
    "user": os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "database": os.getenv("MYSQL_DATABASE")
}
print(f"DEBUG: DB_CONFIG loaded: {DB_CONFIG}") # Temporary debug print

def get_db_connection(): return mysql.connector.connect(**DB_CONFIG) # Establishes DB connection

def save_message(session_id: str, role: str, content: str): # Saves message to DB
    try:
        with get_db_connection() as conn, conn.cursor() as cursor:
            cursor.execute("INSERT INTO chat_history (session_id, role, content) VALUES (%s, %s, %s)", (session_id, role, content))
            conn.commit()
    except mysql.connector.Error as err: print(f"Error saving: {err}")

def load_messages(session_id: str) -> list[BaseMessage]: # Loads messages from DB
    messages: list[BaseMessage] = []
    try:
        with get_db_connection() as conn, conn.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT role, content FROM chat_history WHERE session_id = %s ORDER BY timestamp", (session_id,))
            for row_untyped in cursor.fetchall():
                row = cast(Dict[str, Any], row_untyped)
                messages.append(HumanMessage(content=cast(str, row["content"])) if row["role"] == "user" else AIMessage(content=cast(str, row["content"])))
    except mysql.connector.Error as err: print(f"Error loading: {err}")
    return messages

def get_chat_response_for_ui(message, chat_history, session_id="default_session"): # Main chat function
    full_messages: list[BaseMessage] = [SystemMessage(content=ai_teacher)]
    full_messages.extend(load_messages(session_id))
    full_messages.append(HumanMessage(content=message))
    bot_message = model.invoke(full_messages).content
    save_message(session_id, "user", cast(str, message))
    save_message(session_id, "assistant", cast(str, bot_message))
    return bot_message

if __name__ == "__main__": # Console test example
    session_id = "console_test_session"
    print(f"Chat for session: {session_id}. Type 'exit' to quit.")
    for msg in load_messages(session_id): print(f"{os.linesep}You: {msg.content}" if isinstance(msg, HumanMessage) else f"{os.linesep}AI: {msg.content}")
    while True:
        query = input("You: ")
        if query.lower() == "exit": break
        response = get_chat_response_for_ui(query, [], session_id=session_id)
        print(f"AI: {response}")
    print("Chat ended. History saved.")