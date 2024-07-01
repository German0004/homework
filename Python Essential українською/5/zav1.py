
class Person:
    def my_function_yourname(self, name, surname):
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        print(f"Hello {name} {surname}")

yourname = Person()
yourname.my_function_yourname(name="<NAME>", surname="<NAME>")
print("Where is my usage???")