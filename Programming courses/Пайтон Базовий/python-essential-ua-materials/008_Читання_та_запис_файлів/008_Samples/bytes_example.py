text = "hello world"
print(text)
print(type(text))
b_text = text.encode(encoding='utf-8')
print(b_text)
print(type(b_text))

with open("test", "wb") as file:
    file.write(b_text)

with open("test", "rb") as file:
    t = file.read()
    print(t)
    print(type(t))
