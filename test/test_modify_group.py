# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_group(Group(name="new_group", header="header", footer="footer"))
    app.session.logout()
