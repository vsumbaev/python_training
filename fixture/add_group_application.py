from selenium import webdriver
from fixture.group_session import SessionHelper1
from fixture.group import GroupHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper1(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://localhost/addressbook/group.php?new=New+group")

    def destroy(self):
        self.wd.quit()
