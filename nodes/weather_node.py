import requests, os

def fetch_weather(query: str):
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    
    if "in " in query.lower():
        city = query.lower().split("in ")[-1].strip()
    else:
        city = query.strip()

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()

    if "weather" not in response:
        return f"Could not fetch weather for {city}. Error: {response.get('message', 'Unknown error')}"

    desc = response['weather'][0]['description']
    temp = response['main']['temp']
    return f"The weather in {city.title()} is currently {desc} with a temperature of {temp}°C."