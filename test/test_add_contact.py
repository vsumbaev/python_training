# -*- coding: utf-8 -*-
from model.contact import Contact

def test_python_training_task3(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(name="name", last_name="lastname",
                      homephone="12345", mobile="12345", workphone="12345",
                      nick='me', company='top', b_day='8', address='tankovaya',
                      b_mounth='May', b_year='1998',
                      email='@1', email2='@2', email3='@3'
                      )
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.max_or_id) == sorted(new_contacts, key=Contact.max_or_id)