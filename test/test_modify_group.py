# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange

def test_modify_group(app):
    if app.group.count() == 0:
        app.wd.find_element_by_name("new").click()
        app.group.fill_forms_groups(Group(name="test", header="test", footer="test"))
        app.wd.find_element_by_name("submit").click()
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="group_name", header="header", footer="footer")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



