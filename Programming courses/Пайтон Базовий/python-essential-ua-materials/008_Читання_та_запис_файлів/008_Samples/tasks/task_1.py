import random

letters = "abcdefghijklmnopqrstuvwxyz"

random_letters = ""
random_count = 25

while len(random_letters) < random_count:
    random_letter = letters[random.randint(0, len(letters)-1)]
    random_letters += random_letter

print(random_letters)
with open('random_string', 'w') as text_file:
    text_file.write(random_letters)

