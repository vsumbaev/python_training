from model.contact import Contact
import time
import random

def test_delete_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.open_new_contact_page()
        app.wd.find_element_by_xpath("/html/body/div/div[3]/ul/li[2]/a").click()
        app.contact.fill_forms_contacts(Contact())
        app.wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
    old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
#    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_id(contact.id)
    time.sleep(5)
    new_contacts = db.get_contacts_list()
    assert len(old_contacts) - 1 == app.contact.count()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)