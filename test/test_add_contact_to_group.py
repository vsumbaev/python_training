import random
from model.group import Group
from model.contact import Contact

def test_add_to_group(app, db, check_ui):
    if len(db.get_contacts_list()) == 0:
        app.contact.create_contact(
            Contact(name="take", last_name="this", address="data")
        )
    if len(db.get_group_list()) == 0:
        app.group.group_create(Group(name="test", header='this', footer='data'))

    old_groups = db.get_group_list()
    old_contacts = db.get_contacts_list()

    random_group = random.choice(old_groups)
    random_contact = random.choice(old_contacts)
    app.contact.add_to_group(contact_id=random_contact.id, group_id=random_group.id)
    new_contacts = db.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)

#    if check_ui:
#        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)