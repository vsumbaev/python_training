# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_group(app):
    if app.group.count() == 0:
        app.wd.find_element_by_name("new").click()
        app.group.fill_forms_groups(Group(name="test", header="test", footer="test"))
        app.wd.find_element_by_name("submit").click()
    app.group.open_groups_page()
    app.wd.find_element_by_name("selected[]").click()
    app.wd.find_element_by_name("edit").click()
    app.group.fill_forms_groups(Group(name="new_group", header="header", footer="footer"))
    app.wd.find_element_by_name("update").click()
    app.group.open_groups_page()

