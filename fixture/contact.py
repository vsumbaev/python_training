from selenium.webdriver.support.ui import Select

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(group.name)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(group.last_name)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(group.nick)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(group.company)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(group.mobile)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(group.mail)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(group.b_day)
        wd.find_element_by_xpath("//option[@value='8']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(group.b_mounth)
        wd.find_element_by_xpath("//option[@value='May']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(group.b_year)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
