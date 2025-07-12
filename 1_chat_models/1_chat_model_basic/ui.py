import gradio as gr
import json
import os
from chat_model_basic import invoke_gemini_model

# Get the absolute path to the branding.json file relative to the current script
branding_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'branding.json')

with open(branding_file_path, "r") as f:
    branding_data = json.load(f)

chatbot_title = branding_data["brand"]["chatbot"]["title"]
chatbot_description = branding_data["brand"]["chatbot"]["description"]

# Create the Gradio interface
iface = gr.Interface(
    fn=invoke_gemini_model,
    inputs=gr.Textbox(lines=2, placeholder="Type your message here..."),
    outputs="text",
    title=chatbot_title,
    description=chatbot_description
)

# Launch the interface
iface.launch()