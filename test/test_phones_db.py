from model.contact import Contact
import re


def test_contact_check_main_page_and_db(app, db):
    if app.contact.count() == 0:
        app.contact.open_contacts_page()
        app.wd.find_element_by_xpath("/html/body/div/div[3]/ul/li[2]/a").click()
        app.contact.fill_forms_contacts(Contact(name="name", last_name="lastname",
                                        homephone="12345", mobile="12345", workphone="12345",
                                        ))
    contacts_from_home_page = app.contact.get_contacts_list()
    print('home', sorted(contacts_from_home_page, key=Contact.max_or_id))
    contacts_from_db = db.get_contacts_list()
    print('db', sorted(contacts_from_db, key=Contact.max_or_id))
    assert sorted(contacts_from_home_page, key=Contact.max_or_id) == sorted(contacts_from_db, key=Contact.max_or_id)
    def clean(contact):
        return Contact(id=contact.id, name=contact.name.strip(), last_name=contact.last_name.strip(),
                          all_phones_from_home_page=merge_phones_like_on_home_page(contact),
                          all_emails_from_home_page=merge_emails_like_on_home_page(contact))
    db_list = map(clean, db.get_contacts_list())
    assert sorted(contacts_from_home_page, key=Contact.max_or_id) == sorted(db_list, key=Contact.max_or_id)


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




