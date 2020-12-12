# -*- coding: utf-8 -*-
from model.group import Group
import random

'''Тест, в котором список групп расположен в базе данных'''
def test_modify_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.wd.find_element_by_name("new").click()
        app.group.fill_forms_groups(Group(name="test", header="test", footer="test"))
        app.wd.find_element_by_name("submit").click()
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    change_name = Group(name="test", header="test", footer="test")
    app.group.modify_group_by_id(group.id, change_name)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

'''Тест, в котором список групп расположен в ui'''
#def test_modify_group(app):
#    if app.group.count() == 0:
#        app.wd.find_element_by_name("new").click()
#        app.group.fill_forms_groups(Group(name="test", header="test", footer="test"))
#        app.wd.find_element_by_name("submit").click()
#    old_groups = app.group.get_group_list()
#    index = randrange(len(old_groups))
#    group = Group(name="group_name", header="header", footer="footer")
#    group.id = old_groups[index].id
#    app.group.modify_group_by_index(index, group)
#    assert len(old_groups) == app.group.count()
#    new_groups = app.group.get_group_list()
#    old_groups[index] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



