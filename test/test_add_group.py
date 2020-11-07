# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create_groups(Group(name="group_name", header="group_header", footer="group_footer"))
    app.session.logout()
