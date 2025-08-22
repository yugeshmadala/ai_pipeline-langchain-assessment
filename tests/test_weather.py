from nodes.weather_node import fetch_weather

def test_weather():
    result = fetch_weather("London")
    assert isinstance(result, str)