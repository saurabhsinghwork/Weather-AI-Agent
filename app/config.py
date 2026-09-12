from pydantic_settings import BaseSettings, SettingsConfigDict

class Setttings(BaseSettings):
    gemini_api_key: str
    gemini_model: str = "gemini-3.5-flash-lite"
    min_forecast_days: int = 7
    max_forecast_days: int = 16

    model_config = SettingsConfigDict(
        env_file= ".env",
        env_file_encoding= "utf-8"
    )

settings = Setttings()    