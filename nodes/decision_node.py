def decide(query: str):
    if "weather" in query.lower() or "temperature" in query.lower():
        return "weather"
    return "rag"
