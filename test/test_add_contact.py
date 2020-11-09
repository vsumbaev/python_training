# -*- coding: utf-8 -*-
from model.contact import Contact

def test_python_training_task3(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contacts(
        Contact(name="valery", last_name="sumbaev",
                nick="python_training", company="s-terra", mobile="+79999999999",
                mail="universal310@yandex.ru", b_day="8", b_mounth="May", b_year="1998")
                       )
    app.session.logout()

