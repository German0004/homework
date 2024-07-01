# Опишіть класи графічного об'єкта, прямокутника та об'єкта, який може обробляти натискання миші. Опишіть клас кнопки. Створіть
# об'єкт кнопки та звичайного прямокутника. Викличте метод натискання на кнопку

# кдас графічний об'кт
class GraphicObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        raise NotImplementedError("Subclasses should implement this method")


# Клас Rectangle (прямокутник)
class Rectangle(GraphicObject):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def draw(self):
        print(f"Drawing rectangle at ({self.x}, {self.y}) with width {self.width} and height {self.height}")


# Клас MouseClickable (об'єкт, що обробляє натискання миші)
class MouseClickable(GraphicObject):
    def __init__(self, x, y):
        super().__init__(x, y)

    def click(self):
        print(f"Mouse click processed at ({self.x}, {self.y})")


# Клас Button (кнопка)
class Button(MouseClickable):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def draw(self):
        print(f"Drawing button at ({self.x}, {self.y}) with width {self.width} and height {self.height}")

    # Метод, який буде викликатися при натисканні кнопки
    def click(self):
        print(f"Button clicked at ({self.x}, {self.y})")


# Створення об'єктів і виклик методу натискання на кнопку
def main():
    rectangle = Rectangle(10, 20, 100, 50)
    button = Button(50, 100, 80, 30)

    rectangle.draw()
    button.draw()

    button.click()


if __name__ == "__main__":
    main()
