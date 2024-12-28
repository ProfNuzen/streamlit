import streamlit as st
import ollama
import time

"""
    Description: Demo of ollama model using stream\n
    Output:
        webpage: similar to chatgpt\n
    instructions:
        ollama run llama3; 
        streamlit run st_ollama.py\n
    Reference:
    https://docs.streamlit.io/develop/api-reference/chat
"""
def stream_lines(text,delay:float=0.09):
    """
    _description_: break up data stream from model 
    Args:
        text (str): raw text
        delay (float, optional):Defaults to 0.09.

    Yields:
        str: return line word at a time
    """
    for line in text.split("\n"):
        yield line + "\n"
        time.sleep(delay)
def stream_words(text,delay:float=0.02):
    for word in text.split(" "):
        yield (word + " ")
        time.sleep(delay)

def main():     
    #input for the prompt
    prompt = st.chat_input("Ask a question")
    if prompt:          
        # if the prompt is not empty
        # display input prompt from user
        with st.chat_message("user"):
            st.write(prompt)
        # processing
        # find out which model to use
        # st.write(ollama.list())
        chat_model = "llama3"
        with st.spinner("Thinking ..."):
            result = ollama.chat(model=chat_model, messages=[{
                "role": "user",
                "content": prompt,
            }])
            # display the raw result
            # st.write(result)
            response = result["message"]["content"]
            #st.write(response)
            st.write_stream(stream_lines(response))

if __name__ == "__main__":
    main()
