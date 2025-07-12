import gradio as gr
import json
import os
from chat_model_basic_conversation import get_chat_response_for_ui

# Get the absolute path to the branding.json file relative to the current script
branding_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'branding.json')

with open(branding_file_path, "r") as f:
    branding_data = json.load(f)

chatbot_title = branding_data["brand"]["chatbot"]["title"]
chatbot_description = branding_data["brand"]["chatbot"]["description"]
chatbot_avatar = branding_data["brand"]["chatbot"]["avatar"]

iface = gr.ChatInterface(
    fn=get_chat_response_for_ui,
    title=chatbot_title,
    description=chatbot_description).launch()