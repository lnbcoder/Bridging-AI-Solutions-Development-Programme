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

greet("example text")

#gr.Interface(fn=greet, inputs="textbox", outputs="textbox", flagging_mode="never").launch()
gr.Interface(fn=greet, inputs="textbox", outputs="textbox", flagging_mode="never").launch(share=True)
