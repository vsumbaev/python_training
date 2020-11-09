from model.change_contact import ChangeContact


def test_delete_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_contact(ChangeContact(name="valery"))
    app.session.logout()