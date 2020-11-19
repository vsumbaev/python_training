# -*- coding: utf-8 -*-
from model.contact import Contact

def test_python_training_task3(app):
    old_contacts = app.contact.get_contacts_list()
    app.contact.fill_forms_contacts(Contact())
    app.wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)


