# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
	old_contacts = app.contact.get_contact_list()
	contact = Contact(firstname="new_f_n", lastname="new_l_n", home_phone="123")
	app.contact.create(contact)
	assert len(old_contacts) + 1 == app.contact.count_contact()  # .count - хеш-функция
	new_contacts = app.contact.get_contact_list()
	old_contacts.append(contact)
	assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
