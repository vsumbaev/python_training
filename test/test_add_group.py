# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
        app.group.open_groups_page()
        app.wd.find_element_by_name("new").click()
        app.group.fill_forms_groups(Group())
        app.wd.find_element_by_name("submit").click()
        app.group.open_groups_page()
