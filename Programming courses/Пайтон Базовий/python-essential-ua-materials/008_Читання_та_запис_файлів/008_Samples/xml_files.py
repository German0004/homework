from xml.dom import minidom
from xml.etree import ElementTree

# my_doc = minidom.parse('my_file.xml')
#
# items = my_doc.getElementsByTagName('item')
# print(items)

data = ElementTree.Element('data')
items = ElementTree.SubElement(data, 'items')
item1 = ElementTree.SubElement(items, 'item')
item2 = ElementTree.SubElement(items, 'item')
item1.set('name', 'item1')
item2.set('name', 'item2')
item1.text = 'item1abc'
item2.text = 'item2abc'

my_data = ElementTree.tostring(data)
with open('items2.xml', 'wb') as my_file:
    my_file.write(my_data)
