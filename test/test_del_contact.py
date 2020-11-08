from model.del_contact import DeleteContact


def test_delete_contact(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_contact(DeleteContact(name="valery"))
    app.session.logout()