# -*- coding: utf-8 -*-
from model.contact import Contact
import random

def test_modify_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.wd.find_element_by_xpath("/html/body/div/div[3]/ul/li[2]/a").click()
        app.contact.fill_forms_contacts(Contact())
        app.wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
    old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    change_contact = Contact(name="valery", last_name='', address='')
    app.contact.modify_contact_by_id(contact.id, change_contact)
 #   contact.id = old_contacts[index].id
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contacts_list()
 #   old_contacts[index] = contact
 #   assert sorted(old_contacts, key=Contact.max_or_id) == sorted(new_contacts, key=Contact.max_or_id)
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.max_or_id) == sorted(app.contact.get_contacts_list(), key=Contact.max_or_id)