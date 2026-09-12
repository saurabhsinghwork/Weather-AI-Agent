import httpx


def get_weather_forecast(city: str, days: int) -> dict:
    geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"

    location_response = httpx.get(
        geocoding_url,
        params={
            "name": city,
            "count": 1,
        },
        timeout=20,
    )

    location_response.raise_for_status()

    location = location_response.json()["results"][0]

    forecast_url = "https://api.open-meteo.com/v1/forecast"

    weather_response = httpx.get(
        forecast_url,
        params={
            "latitude": location["latitude"],
            "longitude": location["longitude"],
            "daily": (
                "weather_code,"
                "temperature_2m_max,"
                "temperature_2m_min,"
                "precipitation_probability_max,"
                "wind_speed_10m_max"
            ),
            "timezone": "auto",
            "forecast_days": days,
        },
        timeout=20,
    )

    weather_response.raise_for_status()

    return {
        "city": location["name"],
        "country": location.get("country", ""),
        "weather": weather_response.json(),
    }