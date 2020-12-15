import random

def test_delete_contact_from_group(app, orm):
    all_groups = orm.get_group_list()
    all_contacts = orm.get_contact_list()
    random_contact = random.choice(all_contacts)
    random_group = random.choice(all_groups)
    groups_with_contact = orm.get_groups_with_contacts(random_contact)
    if len(groups_with_contact) == 0:
        app.contact.add_to_group(random_contact.id, random_group.id)
    group_with_contact = orm.get_groups_with_contacts(random_contact)
    random_group = random.choice(group_with_contact)
    app.contact.delete_contact_from_group(random_group.id, random_contact.id)
    contacts_not_in_group = orm.get_contacts_not_in_group(random_group)
    assert random_contact in contacts_not_in_group