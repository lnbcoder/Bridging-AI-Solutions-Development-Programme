from dotenv import load_dotenv
import os
from openai import OpenAI
import gradio as gr

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

system_message = "You are a helpful assistant that responds in markdown without code blocks"

client = OpenAI(api_key=api_key)


def stream_claude(prompt):
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
      ]
    stream = anthropic.chat.completions.create(
        model='claude-sonnet-4-5-20250929',
        messages=messages,
        stream=True
    )
    result = ""
    for chunk in stream:
        result += chunk.choices[0].delta.content or ""
        yield result


message_input = gr.Textbox(label="Your message:", info="Enter a message for Claude 4.5 Sonnet", lines=7)
message_output = gr.Markdown(label="Response:")

view = gr.Interface(
    fn=stream_claude,
    title="Claude", 
    inputs=[message_input], 
    outputs=[message_output], 
    examples=[
        "Explain the LLM",
        "Explain the AI engineer",
        ], 
    flagging_mode="never"
    )
view.launch()(inbrowser=True)
