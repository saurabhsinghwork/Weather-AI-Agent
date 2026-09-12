from langchain_google_genai import ChatGoogleGenerativeAI

from app.config import settings
from app.state import WeatherState
from app.tools import get_weather_forecast


llm = ChatGoogleGenerativeAI(
    model=settings.gemini_model,
    google_api_key=settings.gemini_api_key,
)


def understand_request(state: WeatherState) -> WeatherState:
    prompt = f"""
From this request, return only city and days separated by comma.

Request:
{state["user_input"]}

Example:
Lucknow,7

If days are missing, use 7.
"""

    response = llm.invoke(prompt)

    text = response.text

    city, days = text.strip().split(",")

    return {
        "city": city.strip(),
        "days": int(days.strip()),
    }


def get_weather(state: WeatherState) -> WeatherState:
    data = get_weather_forecast(
        state["city"],
        state["days"],
    )

    return {
        "weather_data": data,
    }


def generate_response(state: WeatherState) -> WeatherState:
    prompt = f"""
Give a simple weather forecast for {state["city"]}.

Weather data:
{state["weather_data"]}
"""

    response = llm.invoke(prompt)

    return {
        "response": response.text,
    }