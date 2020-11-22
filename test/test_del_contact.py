from model.contact import Contact
import time

def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.open_new_contact_page()
        app.wd.find_element_by_xpath("/html/body/div/div[3]/ul/li[2]/a").click()
        app.contact.fill_forms_contacts(Contact())
        app.wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
    old_contacts = app.contact.get_contacts_list()
    app.contact.delete_contact()
    time.sleep(5)
    new_contact = app.contact.get_contacts_list()
    assert len(old_contacts) - 1 == app.contact.count()
    old_contacts[0:1] = []
    assert old_contacts == new_contact