import random
from model.group import Group
from model.contact import Contact

def test_add_to_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create_contact(
            Contact(name="take", last_name="this", address="data")
        )
    if len(orm.get_group_list()) == 0:
        app.group.group_create(Group(name="test", header='this', footer='data'))

    '''поиск группы без случайно-выбранного контакта и добавление контакта в эту группу'''
    old_contacts = orm.get_contact_list()
    random_contact = random.choice(old_contacts)
    #находим группу в которой нет выбранного контакта
    group_without_contacts = orm.get_groups_without_contacts(random_contact)
    #если таковой нет, то создаем ее
    if len(group_without_contacts) == 0:
        app.group.group_create(Group(name="nn", header="nn", footer='nn'))
        contact = orm.get_contact_list()
        random_contact = random.choice(contact)
        new_group_without_contacts = orm.get_groups_without_contacts(random_contact)
        group = random.choice(new_group_without_contacts)
        app.contact.add_to_group(random_contact.id, group.id)
        contacts_in_group = orm.get_contacts_in_group(group)
        assert random_contact in contacts_in_group
    else:
        # групп может быть больше 1, поэтому случайным образом выбираем группу
        group = random.choice(group_without_contacts)
        #после чего добавляем случайный контакт в нее
        app.contact.add_to_group(random_contact.id, group.id)
        contacts_in_group = orm.get_contacts_in_group(group)
        assert random_contact in contacts_in_group


