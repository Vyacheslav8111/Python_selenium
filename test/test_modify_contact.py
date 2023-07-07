from model.contact import Contact


def test_modify_contact_first_name(app):
	app.contact.modify_first_contact(Contact(firstname="New first_name"))


def test_modify_contact_fax(app):
	app.contact.modify_first_contact(Contact(fax="New fax: 333323"))
