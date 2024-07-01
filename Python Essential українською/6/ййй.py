def message_people(people: list) -> callable:
    def print_message(message: str) -> None:
        if message == "hello":
            print(f"Hello, {', '.join(people)}, nice to see you!")
        elif message == "meeting":
            print(f"{', '.join(people)}, we have a meeting in an hour, don't be late!")
        elif message == "bye":
            print(f"Bye {', '.join(people)}, see you tomorrow!")
        else:
            print("Invalid message type")

    return print_message
