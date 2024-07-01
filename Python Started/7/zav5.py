# Є рядок, в якому зберігаються 1000 слів. Створіть словник із ключами - унікальними словами та значеннями - кількістю
# повторів кожного слова у послідовності.


def count_word_frequencies(text):
    # Розбиваємо рядок на слова, видаляючи пробіли і неалфавітні символи
    words = text.split()

    # Створюємо порожній словник для зберігання кількості повторів
    word_count = {}

    # Проходимо по кожному слову в списку слів
    for word in words:
        # Видаляємо неалфавітні символи і перетворюємо слово в нижній регістр
        cleaned_word = "".join(filter(str.isalnum, word)).lower()

        # Якщо слово вже є в словнику, збільшуємо його значення
        if cleaned_word in word_count:
            word_count[cleaned_word] += 1
        # Інакше додаємо слово в словник з початковим значенням 1
        else:
            word_count[cleaned_word] = 1

    return word_count


# Приклад використання
text = """
MR. ROBERT MONTGOMERY wa^ seated at his desk, his head upon his hands, in a state of the blackest despondency. Before 
him was the open ledger with the long columns of Dr. Olclacre's prescriptions. >' t his elbow lay the wooden tray witn 
the labels in various partitions, the cork box, the lumps of twisted sealing-wax, while in front a rank of empty bottles
 waited to be filled. But his spirits were too low for work. He sat in silence, with his fine shoulders bowed and his 
 head upon his hands.
Outside, through the grimy surgery window over a foreground of blackened bricV d slate, a line of enormous chimneys
 like C/clopean pillars upheld the lowering, dun-coloured cloudbank. For six days in the week they spouted smoke, but 
 to-day the furnace fires were banked, for it was Sunday. Sordid and polluting gloom hung over a district blighted and 
 blasted by the greed of man. There was nothing in the sur-
"""
word_frequencies = count_word_frequencies(text)
print(word_frequencies)
