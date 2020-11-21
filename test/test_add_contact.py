# -*- coding: utf-8 -*-
from model.contact import Contact

def test_python_training_task3(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact()
    app.contact.open_new_contact_page()
    app.contact.fill_forms_contacts(contact)
    app.wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts) - 1
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)