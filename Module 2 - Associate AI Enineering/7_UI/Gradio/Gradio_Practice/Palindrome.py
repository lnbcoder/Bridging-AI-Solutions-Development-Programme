import gradio as gr

def is_palindrome(word):
    word_reversed = word[::-1]
    print(word_reversed)

    if word.lower() == word_reversed.lower():
        return f"The word {word} is palindrome"
    else: 
        return f"The word {word} is not palindrome"
    
gr.Interface(fn=is_palindrome, inputs="textbox", outputs="textbox",flagging_mode="never").launch(inbrowser=True, share=True)

