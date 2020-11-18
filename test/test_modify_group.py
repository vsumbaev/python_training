# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="new_group", header="header", footer="footer")
    group.id = old_groups[0].id
    if app.group.count() == 0:
        app.wd.find_element_by_name("new").click()
        app.group.fill_forms_groups(Group(name="test", header="test", footer="test"))
        app.wd.find_element_by_name("submit").click()
    app.group.open_groups_page()
    app.wd.find_element_by_name("selected[]").click()
    app.wd.find_element_by_name("edit").click()
    app.group.fill_forms_groups(group)
    app.wd.find_element_by_name("update").click()
    app.group.open_groups_page()
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



