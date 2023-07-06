from model.contact import Contact


def test_modify_contact_first_name(app):
	app.session.login(username="Admin", password="secret")
	app.contact.modify_first_contact(Contact(firstname="New first_name"))
	app.session.logout()


def test_modify_contact_fax(app):
	app.session.login(username="Admin", password="secret")
	app.contact.modify_first_contact(Contact(fax="New fax: 333323"))
	app.session.logout()