from dotenv import load_dotenv
import os

load_dotenv()


import streamlit as st
from pipeline import run_pipeline

st.title("AI Assistant - Weather + RAG")

query = st.text_input("Ask me something:")

if st.button("Submit") and query:
    result = run_pipeline(query)  # <-- pass query
    st.write(result)
