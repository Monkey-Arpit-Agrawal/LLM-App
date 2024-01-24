from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=os.getenv("Google_API_KEY"))

# Function to get responses
model = genai.GenerativeModel('gemini-pro')

def get_response(question):
    response = model.generate_content(question)
    return response.text

# Streamlit Application

st.set_page_config(page_title="Q and A App")

st.header("Ask a Question")

input = st.text_input("Input : " , key=input)
submit = st.button("Ask the Question")

# When Submit is clicked 

if submit :
    response = get_response(input)
    st.subheader("The Response is ")
    st.write(response)