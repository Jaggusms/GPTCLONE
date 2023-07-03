import openai
import streamlit as st

openai.api_key="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"

def get_chatgpt_response(messages):
  response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=messages)
  return  response['choices'][0]['message']['content']




st.title("Chatbot")
user_input = st.text_area("Enter the Query")
messages ={"role": "user", "content": user_input}
if st.button("Submit Query"):
    with st.spinner("Generating..."):
        model_response = get_chatgpt_response(messages)
        st.write(model_response)
       
