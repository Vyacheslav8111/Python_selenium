from model.contact import Contact
import random


def test_modify_contact_first_name(app):
	if app.contact.count_contact() == 0:
		app.contact.create(Contact(firstname="New", lastname="123"))
	old_contacts = app.contact.get_contact_list()
	contact = random.choice(old_contacts)
	modify_contact = Contact(firstname="qwer", lastname="tyyuyi")
	app.contact.modify_contact_by_id(contact.id, modify_contact)
	new_contacts = app.contact.get_contact_list()
	assert len(old_contacts) == len(new_contacts)
	assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



# def test_modify_contact_fax(app):
# 	if app.contact.count_contact() == 0:
# 		app.contact.create(Contact(firstname="ryty"))
# 	old_contacts = app.contact.get_contact_list()
# 	app.contact.modify_first_contact(Contact(firstname="New title"))
# 	new_contacts = app.contact.get_contact_list()
# 	assert len(old_contacts) == len(new_contacts)