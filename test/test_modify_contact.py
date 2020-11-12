# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    app.contact.open_contacts_page()
    app.wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()
    app.contact.fill_forms_contacts(
        Contact(name="valera", last_name="1_sumbaev",
                nick="1_python_training", company="1_s-terra", mobile="1_+79999999999",
                mail="1_universal310@yandex.ru", b_day="13", b_mounth="May", b_year="1995")
                       )
    app.wd.find_element_by_xpath("/html/body/div/div[4]/form[1]/input[1]").click()
