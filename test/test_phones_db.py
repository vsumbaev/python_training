from model.contact import Contact
import re

def test_contact_check_main_page_and_edit_page_by_index(app, db):
    if app.contact.count() == 0:
        app.contact.open_contacts_page()
        app.wd.find_element_by_xpath("/html/body/div/div[3]/ul/li[2]/a").click()
        app.contact.fill_forms_contacts(Contact(name="name", last_name="lastname",
                                        homephone="12345", mobile="12345", workphone="12345",
                                        ))
    old_contacts = db.get_contacts_list()
    number_groups = len(old_contacts)
    for i in range(0, number_groups):
        contact_from_home_page = app.contact.get_contacts_list()[i]
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(i)
        assert contact_from_home_page.name == contact_from_edit_page.name
        assert contact_from_home_page.last_name == contact_from_edit_page.last_name
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
        assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

def merge_phones_like_on_home_page(contact):
    return "\n".join(
        filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobile, contact.workphone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(
        filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))

def clear(s):
    return re.sub("[() -]", "", s)