# ai_pipeline-langchain-assessment
This Repositoy consists of my work related to langchain  end to end pipeline of an AI assited weather information app
Set up project structure: app.py, pipeline.py, nodes/, utils/, tests/, data/.

Created a virtual environment and installed dependencies (streamlit, requests, python-dotenv, langchain, faiss-cpu, langchain-groq).

Created .env file for API keys: GROQ_API_KEY and OPENWEATHERMAP_API_KEY.

Built app.py with Streamlit UI:

st.text_input for user query

st.button("Submit") to trigger pipeline

st.write() to display results

Integrated pipeline (pipeline.py) to decide between weather API or PDF RAG retrieval.

Weather queries handled by nodes/weather_node.py.

PDF queries handled by nodes/rag_node.py with embeddings and FAISS vector store.

Responses processed using Groq LLM in nodes/llm_node.py.

Ran the app using: streamlit run app.py to test queries and display output.
