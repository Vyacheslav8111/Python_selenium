from model.contact import Contact


def test_modify_contact_first_name(app):
	if app.contact.count_contact() == 0:
		app.contact.create(Contact(firstname="New_middlename"))
	old_contacts = app.contact.get_contact_list()
	app.contact.modify_first_contact(Contact(firstname="fax_455657"))
	new_contacts = app.contact.get_contact_list()
	assert len(old_contacts) == len(new_contacts)


def test_modify_contact_fax(app):
	if app.contact.count_contact() == 0:
		app.contact.create(Contact(firstname="ryty"))
	old_contacts = app.contact.get_contact_list()
	app.contact.modify_first_contact(Contact(firstname="New title"))
	new_contacts = app.contact.get_contact_list()
	assert len(old_contacts) == len(new_contacts)

