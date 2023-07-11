from model.contact import Contact


def test_delete_first_contact(app):
	if app.contact.count_contact() == 0:
		app.contact.create(Contact(firstname="New_middlename"))
	old_contacts = app.contact.get_contact_list()
	app.contact.delete_first_contact()
	new_contacts = app.contact.get_contact_list()
	assert len(old_contacts) - 1 == len(new_contacts)
