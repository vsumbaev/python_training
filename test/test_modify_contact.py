# -*- coding: utf-8 -*-
from model.contact import Contact
import time

def test_modify_contact(app):
    if app.contact.count() == 0:
        app.wd.find_element_by_xpath("/html/body/div/div[3]/ul/li[2]/a").click()
        app.contact.fill_forms_contacts(Contact())
        app.wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(name="valery")
    contact.id = old_contacts[0].id
    app.wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()
    app.contact.fill_forms_contacts(contact)
    app.wd.find_element_by_xpath("/html/body/div/div[4]/form[1]/input[1]").click()
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)