from dotenv import load_dotenv
import os
from openai import OpenAI
import gradio as gr

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def greet(text):
    print(f"Shout has been called with input {text}")
    return text.upper()
  
message_input = gr.Textbox(label="Your message:", info="Enter a message to be greeted", lines=7)
message_output = gr.Textbox(label="Response:", lines=8)

view = gr.Interface(
    fn=greet,
    title="Greet", 
    inputs=[message_input], 
    outputs=[message_output], 
    examples=["hello", "howdy"], 
    flagging_mode="never"
    )
view.launch()
