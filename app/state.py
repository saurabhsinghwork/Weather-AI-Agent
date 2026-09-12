from typing import Any, TypedDict

class WeatherState(TypedDict,total=False):
    user_input: str
    city: str
    days: int
    weather_data: Any
    response: str
    error: str