# -*- coding: utf-8 -*-
from model.contact import Contact
from model.change_contact import ChangeContact

def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_contacts(
        Contact(name="valera", last_name="1_sumbaev",
                nick="1_python_training", company="1_s-terra", mobile="1_+79999999999",
                mail="1_universal310@yandex.ru", b_day="13", b_mounth="May", b_year="1995")
                       )
    app.session.logout()