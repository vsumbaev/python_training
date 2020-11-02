# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application_add_contact import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_python_training_task3(app):
    app.open_page()
    app.login(user="admin", password="secret")
    app.create_contact(
        Contact(name="valery", last_name="sumbaev",
                nick="python_training", company="s-terra", mobile="+79999999999",
                mail="universal310@yandex.ru", b_day="8", b_mounth="May", b_year="1998")
                       )
    app.logout()

