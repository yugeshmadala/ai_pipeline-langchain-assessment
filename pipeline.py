from nodes.decision_node import decide
from nodes.weather_node import fetch_weather
from nodes.rag_node import rag_query
from nodes.llm_node import process_with_llm

def run_pipeline(query: str):
    choice = decide(query)
    if choice == "weather":
        result = fetch_weather(query)  # <-- pass the query here
    else:
        result = rag_query(query)
    final = process_with_llm(result)
    return final
