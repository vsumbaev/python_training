# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.wd.find_element_by_name("new").click()
    app.group.fill_forms_groups(Group(name="group_name", header="group_header", footer="group_footer"))
    app.wd.find_element_by_name("submit").click()
    app.group.return_to_groups_page()
    app.session.logout()
