from dotenv import load_dotenv
import os
from openai import OpenAI
import gradio as gr

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

system_message = "You are a helpful assistant that responds in markdown without code blocks"

client = OpenAI(api_key=api_key)


def message_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


message_input = gr.Textbox(label="Your message:", info="Enter a message for GPT-4.1-mini", lines=7)
message_output = gr.Markdown(label="Response:")


view = gr.Interface(
    fn=message_gpt,
    title="GPT", 
    inputs=[message_input], 
    outputs=[message_output], 
    examples=[
        "Explain the Transformer architecture to a layperson",
        "Explain the Transformer architecture to an aspiring AI engineer",
        ], 
    flagging_mode="never"
    )

view.launch(inbrowser=True)
