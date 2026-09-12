from langgraph.graph import END, START, StateGraph

from app.nodes import understand_request, get_weather, generate_response
from app.state import WeatherState


def check_error(state: WeatherState) -> str:
    if state.get("error"):
        return "error"

    return "continue"


builder = StateGraph(WeatherState)

builder.add_node("understand_request", understand_request)
builder.add_node("get_weather", get_weather)
builder.add_node("generate_response", generate_response)

builder.add_edge(START, "understand_request")

builder.add_conditional_edges(
    "understand_request",
    check_error,
    {
        "continue": "get_weather",
        "error": END,
    },
)

builder.add_conditional_edges(
    "get_weather",
    check_error,
    {
        "continue": "generate_response",
        "error": END,
    },
)

builder.add_edge("generate_response", END)

weather_graph = builder.compile()