from model.contact import Contact


def test_modify_contact_first_name(app):
	if app.contact.count_contact() == 0:
		app.contact.create(Contact(firstname="New_middlename"))
	app.contact.modify_first_contact(Contact(firstname="fax_455657"))


def test_modify_contact_fax(app):
	if app.contact.count_contact() == 0:
		app.contact.create(Contact(firstname="ryty"))
	app.contact.modify_first_contact(Contact(firstname="New title"))
