# -*- coding: utf-8 -*-
from model.contact import Contact


def test_python_training_task3(app, json_contacts, db, check_ui):
    contact = json_contacts
    old_contacts = db.get_contacts_list()
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = db.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.max_or_id) == sorted(new_contacts, key=Contact.max_or_id)
    if check_ui:
        assert sorted(new_contacts, key=Contact.max_or_id) == sorted(app.contact.get_contacts_list(), key=Contact.max_or_id)