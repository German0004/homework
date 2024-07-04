# filename = 'my_text'
#
# text_file = open(filename, 'r')
# txt = text_file.read()
# text_file.close()
# print(txt)
#
# with open(filename, 'r') as text_file:
#     text = text_file.read()
# print(text)

filename2 = 'my_text_3'

# text_file = open(filename2, 'w')
# txt = 'Hello world ! 12345'
# text_file.write(txt)
# text_file.close()

with open(filename2, 'w') as text_file:
    text = 'Hello world ! 12345'
    text_file.write(text)
