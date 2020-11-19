from selenium.webdriver.support.ui import Select
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/addressbook/") > 0:
            wd.find_element_by_link_text("home").click()

    def open_new_contact_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/edit.php/") > 0:
            wd.find_element_by_link_text("add new").click()

    def fill_forms_contacts(self, contact):
        wd = self.app.wd
        self.open_new_contact_page()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nick)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.mail)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.b_day)
        wd.find_element_by_xpath("//option[@value='8']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.b_mounth)
        wd.find_element_by_xpath("//option[@value='May']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.b_year)

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def delete_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        alert = wd.switch_to.alert
        alert.accept()


    def get_contacts_list(self):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_elements_by_name("entry")
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            firstname = wd.find_element_by_css_selector('#maintable > tbody > tr:last-child > td:nth-child(3)').text
            lastname = wd.find_element_by_css_selector('#maintable > tbody > tr:last-child > td:nth-child(2)').text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(name=firstname, last_name=lastname, id=id))
        return contacts
