# Weather Agent

A beginner-friendly AI weather agent built with LangGraph and Gemini.

## Features

- User-selected city
- 7 to 16 day forecast
- Gemini-powered request understanding and response generation
- Open-Meteo geocoding and weather forecast
- LangGraph conditional workflow
- Docker support

## Run with Docker

1. Add your Gemini API key to `.env`.
2. Build and start:

```bash
docker compose up --build
```

3. Enter a request such as:

```text
Weather in Lucknow for 10 days
```

Type `exit` to stop the application.
