# Створіть програму спортивного комплексу, у якій передбачене меню: 1 - перелік видів спорту, 2 - команда тренерів,
# 3 - розклад тренувань, 4 - вартість тренування. Дані зберігати у словниках. Також передбачити пошук по прізвищу тренера,
# яке вводиться з клавіатури у відповідному пункті меню. Якщо ключ не буде знайдений, створити відповідний клас-Exception,
# який буде викликатися в обробнику виключень.


class CoachNotFoundException(Exception):
    def __init__(self, surname):
        self.surname = surname
        super().__init__(f"Тренера з прізвищем '{surname}' не знайдено")

class SportsComplex:
    def __init__(self):
        self.sports = {
            1: "Футбол",
            2: "Баскетбол",
            3: "Теніс",
            4: "Плавання"
        }
        self.coaches = {
            "Сидоренко": "Футбол",
            "Іванов": "Теніс",
            "Шевченко": "Баскетбол"
        }
        self.schedule = {
            "Футбол": "Понеділок і Четвер",
            "Баскетбол": "Вівторок і П'ятниця",
            "Теніс": "Середа і Субота",
            "Плавання": "Понеділок, Середа і П'ятниця"
        }
        self.prices = {
            "Футбол": 200,
            "Баскетбол": 250,
            "Теніс": 300,
            "Плавання": 150
        }

    def show_sports_list(self):
        print("\nПерелік видів спорту:")
        for key, sport in self.sports.items():
            print(f"{key}: {sport}")

    def show_coaches(self):
        print("\nКоманда тренерів:")
        for surname, sport in self.coaches.items():
            print(f"{surname} - {sport}")

    def show_training_schedule(self):
        print("\nРозклад тренувань:")
        for sport, schedule in self.schedule.items():
            print(f"{sport}: {schedule}")

    def show_training_coast(self):
        print("\nВартість тренування:")
        for sport, cost in self.prices.items():
            print(f"{sport}: {cost} грн")

    def search_coach_by_surname(self, surname):
        if surname in self.coaches:
            return self.coaches[surname]
        else:
            raise CoachNotFoundException(surname)

# Основний блок програми
def main():
    complex = SportsComplex()

    while True:
        print("\nМеню:")
        print("1 - Перелік видів спорту")
        print("2 - Команда тренерів")
        print("3 - Розклад тренувань")
        print("4 - Вартість тренування")
        print("5 - Пошук тренера за прізвищем")
        print("6 - Вихід")

        choice = input("Введіть номер пункту меню: ")

        if choice == '1':
            complex.show_sports_list()
        elif choice == '2':
            complex.show_coaches()
        elif choice == '3':
            complex.show_training_schedule()
        elif choice == '4':
            complex.show_training_coast()
        elif choice == '5':
            try:
                surname = input("Введіть прізвище тренера: ")
                sport = complex.search_coach_by_surname(surname)
                print(f"Тренер з прізвищем '{surname}' працює з групою з {sport}")
            except CoachNotFoundException as e:
                print(f"Помилка: {e}")
        elif choice == '6':
            print("До побачення!")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
# Основні особливості програми:

# Клас SportsComplex містить у собі інформацію про види спорту, тренерів, розклад тренувань і вартість тренувань у
# вигляді словників. Методи класу відповідають пунктам меню з доступом до відповідної інформації.
# Використовується власний клас винятку CoachNotFoundException, який успадковується від Exception. Він використовується
# для викидання винятку, якщо тренера з введеним прізвищем не знайдено в словнику тренерів.
# Під час пошуку тренера за прізвищем, програма перехоплює виняток CoachNotFoundException і виводить відповідне повідомлення
# про помилку. Основний блок програми main() керує виконанням програми, дозволяючи користувачеві вибирати пункти меню
# та взаємодіяти з інформацією про спортивний комплекс.