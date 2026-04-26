import gradio as gr

def divisible_by_num(number):
    num_list = []
    if number.isdigit():
        for i in range(1,int(number) + 1):
            if int(number) % i == 0:
                num_list.append(i)
        return f"The number {number} is divisible by {num_list}"
    else:
        return f"The input '{number}' is not a digit"


gr.Interface(fn=divisible_by_num, inputs="textbox", outputs="textbox", flagging_mode="never").launch(inbrowser=True)



## My notes:
#launch(inbrowser=True) -> used to launch the interface in the default web browser.
#launch(share=True) -> used to share the interface with others by generating a public URL.
#launch(auth=("Loveness", "love123")) -> used to authenticate users before they can accessing interface.
