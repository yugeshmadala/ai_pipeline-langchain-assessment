from langchain_groq import ChatGroq
import os

def process_with_llm(prompt: str):
    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model="compound-beta",
        temperature=0
    )
    return llm.predict(prompt)
