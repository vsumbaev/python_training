import re
from model.contact import Contact

def test_phones_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.open_new_contact_page()
        app.wd.find_element_by_xpath("/html/body/div/div[3]/ul/li[2]/a").click()
        app.contact.fill_forms_contacts(Contact(name="name", last_name="lastname",
                                        homephone="12345", mobile="12345", workphone="12345",
                                        ))
        app.wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
    contact_from_home_page = app.contact.get_contacts_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone


def clear(s):
    change = re.sub("[() -]", "", s)
    return change

def merge_phones_like_on_home_page(contact):
    return "\n".join(
        filter(lambda x: x != "",
               filter(lambda x: x is not None,
                      [contact.homephone, contact.mobile, contact.workphone])))