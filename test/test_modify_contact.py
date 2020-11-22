# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

def test_modify_contact(app):
    if app.contact.count() == 0:
        app.wd.find_element_by_xpath("/html/body/div/div[3]/ul/li[2]/a").click()
        app.contact.fill_forms_contacts(Contact())
        app.wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(name="valery")
    index = randrange(len(old_contacts))
    app.contact.modify_contact_by_index(index, contact)
    contact.id = old_contacts[index].id
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.max_or_id) == sorted(new_contacts, key=Contact.max_or_id)