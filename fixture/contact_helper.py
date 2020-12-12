from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re

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
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
#        wd.find_element_by_name("nickname").clear()
#        wd.find_element_by_name("nickname").send_keys(contact.nick)
#        wd.find_element_by_name("company").click()
#        wd.find_element_by_name("company").clear()
#        wd.find_element_by_name("company").send_keys(contact.company)
#        wd.find_element_by_name("mobile").click()
#        wd.find_element_by_name("mobile").clear()
#        wd.find_element_by_name("mobile").send_keys(contact.mobile)
#        wd.find_element_by_name("home").click()
#        wd.find_element_by_name("home").clear()
#        wd.find_element_by_name("home").send_keys(contact.homephone)
#        wd.find_element_by_name("work").click()
#        wd.find_element_by_name("work").clear()
#        wd.find_element_by_name("work").send_keys(contact.workphone)
#        wd.find_element_by_name("email").click()
#        wd.find_element_by_name("email").clear()
#        wd.find_element_by_name("email").send_keys(contact.email)
#        wd.find_element_by_name("email2").click()
#        wd.find_element_by_name("email2").clear()
#        wd.find_element_by_name("email2").send_keys(contact.email2)
#        wd.find_element_by_name("email3").click()
#        wd.find_element_by_name("email3").clear()
#        wd.find_element_by_name("email3").send_keys(contact.email3)
#        wd.find_element_by_name("bday").click()
#        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.b_day)
#        wd.find_element_by_xpath("//option[@value='8']").click()
#        wd.find_element_by_name("bmonth").click()
#        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.b_mounth)
#        wd.find_element_by_xpath("//option[@value='May']").click()
#        wd.find_element_by_name("byear").click()
#        wd.find_element_by_name("byear").clear()
#        wd.find_element_by_name("byear").send_keys(contact.b_year)

    def create_contact(self, contact):
        wd = self.app.wd
        self.open_new_contact_page()
        self.fill_forms_contacts(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.contact_cache = None

    def modify_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()
        self.fill_forms_contacts(contact)
        wd.find_element_by_xpath("/html/body/div/div[4]/form[1]/input[1]").click()
        self.contact_cache = None

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.select_contact_by_index(index)
        choice_contact = wd.find_elements_by_name("entry")[index]
        cells = choice_contact.find_elements_by_tag_name("td")[7]
        cells.find_element_by_tag_name("a").click()
        self.fill_forms_contacts(contact)
        wd.find_element_by_xpath("/html/body/div/div[4]/form[1]/input[1]").click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def delete_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        alert = wd.switch_to.alert
        alert.accept()
        self.contact_cache = None

    def select_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        alert = wd.switch_to.alert
        alert.accept()
        self.contact_cache = None

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name('td')
                name = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                all_emails = cells[4].text
                id = cells[0].find_element_by_tag_name('input').get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(name=name, last_name=lastname, address=address,
                                                  all_emails_from_home_page=all_emails,
                                                  id=id, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone =wd.find_element_by_name("work").get_attribute("value")
        mobile =wd.find_element_by_name("mobile").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(name=name, last_name=last_name, id=id,
                       homephone=homephone, workphone=workphone, mobile=mobile,
                       email=email, email2=email2, email3=email3)


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        return Contact(homephone=homephone, mobile=mobile, workphone=workphone)

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        wd.find_element_by_css_selector("#content > form:nth-child(10) > div:nth-child(8) > input[type=button]").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector('input[value="%s"]' % id).click()


    def modify_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
        self.fill_forms_contacts(contact)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None


    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_xpath("//*[@id='maintable']/tbody").find_element_by_xpath("//*[@href='edit.php?id=%s']" % id).click()