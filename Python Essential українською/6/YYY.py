# Напиши функцію messange_people, яка примає список імен people, створює і повертає функцію print_messange. Внутрішня функція приймає строку messange , і в жалежності від того чому дорівнює messange (‘hello’ / ‘meeting’ /  ‘bye’) виводить результати, які показані в прикладі, вона не повинна нічого повертати.
# Приклади:
# mes_people = messange_people ([“Alex”, “Robert”, “Tom”])
# mes_people (‘hello’)
# # Hello Alex, Robert, Tom, nice to see you
# mes_people (‘meeting’)
# # Alex, Robert, Tom, we have a meeting in a hour, don`t be late
# mes_people (‘bye’)
# # Bye Alex, Robert, Tom, see you tomorrow


def messange_people(people):
    def print_message(message):
        if message == 'hello':
            print(f"Hello {', '.join(people)}, nice to see you")
        elif message == 'meeting':
            print(f"{', '.join(people)}, we have a meeting in an hour, don't be late")
        elif message == 'bye':
            print(f"Bye {', '.join(people)}, see you tomorrow")
        else:
            print("Invalid message type")

    return print_message


mes_people = messange_people(["Alex", "Robert", "Tom"])

mes_people('hello')
mes_people('meeting')
mes_people('bye')
