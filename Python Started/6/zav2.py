# Є два списки, які наповнюються користувачем з клавіатури. Сформувати список, в якому будуть міститися
# унікальні значення першого відносно другого списку та навпаки без повторень.
# Роздрукувати підсумковий об'єкт на екран в прямій послідовності, зворотній,
# а також виконати сортування за зростанням та спаданням.

words = [str(input("Введіть символи для списків: ")) for _ in range(10)]
row_words_first, row_words_second = words[:5], words[5:]

unique_words_first = [item for item in row_words_first if item not in row_words_second]
print(
    f"base list: {unique_words_first}"
    f"\nrevers list: {unique_words_first[::-1]}"
    f"\nascending list: {sorted(unique_words_first)}"
    f"\ndescending list: {sorted(unique_words_first, reverse=True)}"
)
