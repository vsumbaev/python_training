# -*- coding: utf-8 -*-
from model.group import Group
from sys import maxsize

def test_add_group(app):
        old_groups = app.group.get_group_list()
        app.group.open_groups_page()
        app.wd.find_element_by_name("new").click()
        group = Group()
        app.group.fill_forms_groups(group)
        app.wd.find_element_by_name("submit").click()
        app.group.open_groups_page()
        new_groups = app.group.get_group_list()
        assert len(old_groups) + 1 == len(new_groups)
        old_groups.append(group)
        def id_or_max(gr):
                if gr.id:
                        return int(gr.id)
                else:
                        return maxsize
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
