# console_interface
import logic

def main():
    links = logic.load_links()

    exit_choice = "1"
    while exit_choice != "0":
        value = input("Enter your link: ")
        key = input("Enter short name of the link: ")
        links = logic.add_link(links, key, value)
        exit_choice = input("Enter 0 to exit or something else to continue: ")

    logic.save_links(links)

    search_name = input("Enter search link name: ")
    print(logic.get_link(links, search_name))

if __name__ == "__main__":
    main()
