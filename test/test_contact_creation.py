# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
	app.contact.create(Contact(firstname="q", middlename="w", lastname="e", nickname="r", title="t",
					   company="y",
					   address="u", home="67767-8778", mobile="56565-325", work="6688", fax="5657678",
					   email="test@test.test", email2="test123@test.test", email3="test78@test1.test",
					   homepage="www.testUI.test", address2="test", notes="test"))


def test_add_empty_contact(app):
	app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
					   address="", home="", mobile="", work="", fax="",
					   email="", email2="", email3="",
					   homepage="", address2="", notes=""))
