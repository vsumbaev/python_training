# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_group(app):
    app.group.open_groups_page()
    app.wd.find_element_by_name("selected[]").click()
    app.wd.find_element_by_name("edit").click()
    app.group.fill_forms_groups(Group(name="new_group", header="header", footer="footer"))
    app.wd.find_element_by_name("update").click()
    app.group.return_to_groups_page()

