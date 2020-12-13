import pymysql
from fixture.db import DbFixture

db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

#connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    contacts = db.get_contacts_list()
#    groups = db.get_group_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))
#    cursor = connection.cursor()
#    cursor.execute("select * from group_list")
#    for row in cursor.fetchall():
#        print(row)
finally:
    db.destroy()
#    connection.close()