from xml.etree import ElementTree
import csv

with open('users_data_12;05;21.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    data = [row for row in reader]

columns = data[0]
users = data[1:]

xml_data = ElementTree.Element('data')
items_holder = ElementTree.SubElement(xml_data, 'users')
items = [ElementTree.SubElement(items_holder, 'user') for i in range(len(users))]
for j in range(len(users)):
    item = items[j]
    for k in range(len(columns)):
        item.set(columns[k], users[j][k])

xml_file = ElementTree.tostring(xml_data)
with open('users.xml', 'wb') as file:
    file.write(xml_file)
