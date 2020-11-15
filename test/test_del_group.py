from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.wd.find_element_by_name("new").click()
        app.group.fill_forms_groups(Group(name="test", header="test", footer="test"))
        app.wd.find_element_by_name("submit").click()
    app.group.delete_first_group()
