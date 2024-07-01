# logic.py
def save_links(links, filename="links_database.txt"):
    with open(filename, "w") as file:
        for key, value in links.items():
            file.write(f"{key}: {value}\n")


def load_links(filename="links_database.txt"):
    try:
        with open(filename, "r") as file:
            links = {}
            for line in file:
                key, value = line.strip().split(": ")
                links[key] = value
            return links
    except FileNotFoundError:
        return {}


def add_link(links, key, value):
    links[key] = value
    return links


def get_link(links, key):
    return links.get(key, "Name is not found")
