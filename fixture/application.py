from selenium import webdriver
from fixture.session import SessionHelper
from fixture.helper import Helper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = Helper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/edit.php")

    def open_page_group(self):
        wd = self.wd
        wd.get("https://localhost/addressbook/group.php?new=New+group")

    def destroy(self):
        self.wd.quit()