from model.contact import Contact


def test_modify_contact_first_name(app):
	if app.contact.count_contact() == 0:
		app.contact.create(Contact(firstname="New_middlename"))
	old_contacts = app.contact.get_contact_list()
	contact = Contact(firstname="fax_455657")
	contact.id = old_contacts[0].id
	app.contact.modify_first_contact(contact)
	new_contacts = app.contact.get_contact_list()
	assert len(old_contacts) == len(new_contacts)
	old_contacts[0] = contact
	assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_modify_contact_fax(app):
# 	if app.contact.count_contact() == 0:
# 		app.contact.create(Contact(firstname="ryty"))
# 	old_contacts = app.contact.get_contact_list()
# 	app.contact.modify_first_contact(Contact(firstname="New title"))
# 	new_contacts = app.contact.get_contact_list()
# 	assert len(old_contacts) == len(new_contacts)

