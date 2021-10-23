from sqlite3.dbapi2 import connect
import xml.etree.ElementTree as et
import sqlite3

tree = et.ElementTree(file='1510/menu.xml')
root = tree.getroot()
root.tag
connection = sqlite3.connect("./2210/rootTag.db")
cursor = connection.cursor()
for child in root:
    price = (*child[0].attrib,)[0];
    #cursor.execute("CREATE TABLE " + child.tag +" (name TEXT, "+ price +" TEXT);")
    print('tag:', child.tag, 'attributes:', child.attrib)
    for grandchild in child:
        print('/tag:', grandchild.tag, 'attributes:', grandchild.attrib)
        cursor.execute("INSERT INTO " + child.tag + " VALUES(\"" + grandchild.text + "\", \"" + grandchild.attrib['price'] + "\");")
connection.commit()
cursor.close()
connection.close()