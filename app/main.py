from app.graph import weather_graph


def main() -> None:
    print("Weather Agent")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            break

        if not user_input:
            continue

        result = weather_graph.invoke({
            "user_input": user_input
        })

        if result.get("error"):
            print(f"Agent: {result['error']}\n")
        else:
            print(f"Agent:\n{result['response']}\n")


if __name__ == "__main__":
    main()