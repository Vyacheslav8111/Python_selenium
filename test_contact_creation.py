# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from contact import Contact


class TestContactCreation(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.verificationErrors = []
		self.accept_next_alert = True

	def test_add_contact(self):
		self.login()
		self.create(Contact(firstname="q", middlename="w", lastname="e", nickname="r", title="t", company="y",
							address="u", home="67767-8778", mobile="56565-325", work="6688", fax="5657678",
							email="test@test.test", email2="test123@test.test", email3="test78@test1.test",
							homepage="www.testUI.test", address2="test", notes="test"))
		self.logout()

	def test_add_empty_contact(self):
		self.login()
		self.create(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
							address="", home="", mobile="", work="", fax="",
							email="", email2="", email3="",
							homepage="", address2="", notes=""))
		self.logout()

	def logout(self):
		driver = self.driver
		driver.find_element(By.LINK_TEXT, "Logout").click()

	def return_to_home_page(self):
		driver = self.driver
		driver.find_element(By.LINK_TEXT, "home page").click()

	def create(self, contact):
		driver = self.driver
		# init contact creation
		driver.find_element(By.LINK_TEXT, "add new").click()
		# fill contact form
		driver.find_element(By.NAME, "firstname").click()
		driver.find_element(By.NAME, "firstname").clear()
		driver.find_element(By.NAME, "firstname").send_keys(contact.firstname)
		driver.find_element(By.NAME, "middlename").click()
		driver.find_element(By.NAME, "middlename").clear()
		driver.find_element(By.NAME, "middlename").send_keys(contact.middlename)
		driver.find_element(By.NAME, "lastname").click()
		driver.find_element(By.NAME, "lastname").clear()
		driver.find_element(By.NAME, "lastname").send_keys(contact.lastname)
		driver.find_element(By.NAME, "nickname").click()
		driver.find_element(By.NAME, "nickname").clear()
		driver.find_element(By.NAME, "nickname").send_keys(contact.nickname)
		driver.find_element(By.NAME, "title").click()
		driver.find_element(By.NAME, "title").clear()
		driver.find_element(By.NAME, "title").send_keys(contact.title)
		driver.find_element(By.NAME, "company").click()
		driver.find_element(By.NAME, "company").clear()
		driver.find_element(By.NAME, "company").send_keys(contact.company)
		driver.find_element(By.NAME, "address").click()
		driver.find_element(By.NAME, "address").clear()
		driver.find_element(By.NAME, "address").send_keys(contact.address)
		driver.find_element(By.NAME, "home").click()
		driver.find_element(By.NAME, "home").clear()
		driver.find_element(By.NAME, "home").send_keys(contact.home)
		driver.find_element(By.NAME, "mobile").click()
		driver.find_element(By.NAME, "mobile").clear()
		driver.find_element(By.NAME, "mobile").send_keys(contact.mobile)
		driver.find_element(By.NAME, "work").click()
		driver.find_element(By.NAME, "work").clear()
		driver.find_element(By.NAME, "work").send_keys(contact.work)
		driver.find_element(By.NAME, "fax").click()
		driver.find_element(By.NAME, "fax").clear()
		driver.find_element(By.NAME, "fax").send_keys(contact.fax)
		driver.find_element(By.NAME, "email").click()
		driver.find_element(By.NAME, "email").clear()
		driver.find_element(By.NAME, "email").send_keys(contact.email)
		driver.find_element(By.NAME, "email2").click()
		driver.find_element(By.NAME, "email2").clear()
		driver.find_element(By.NAME, "email2").send_keys(contact.email2)
		driver.find_element(By.NAME, "email3").click()
		driver.find_element(By.NAME, "email3").clear()
		driver.find_element(By.NAME, "email3").send_keys(contact.email3)
		driver.find_element(By.NAME, "homepage").click()
		driver.find_element(By.NAME, "homepage").clear()
		driver.find_element(By.NAME, "homepage").send_keys(contact.homepage)
		driver.find_element(By.NAME, "address2").click()
		driver.find_element(By.NAME, "address2").clear()
		driver.find_element(By.NAME, "address2").send_keys(contact.address2)
		driver.find_element(By.NAME, "notes").click()
		driver.find_element(By.NAME, "notes").clear()
		driver.find_element(By.NAME, "notes").send_keys(contact.notes)
		# submit contact creation
		driver.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
		self.return_to_home_page()

	def login(self):
		driver = self.driver
		self.open_home_page()
		driver.find_element(By.NAME, "user").click()
		driver.find_element(By.NAME, "user").clear()
		driver.find_element(By.NAME, "user").send_keys("Admin")
		driver.find_element(By.NAME, "pass").click()
		driver.find_element(By.NAME, "pass").clear()
		driver.find_element(By.NAME, "pass").send_keys("secret")
		driver.find_element(By.XPATH, "//input[@value='Login']").click()

	def open_home_page(self):
		driver = self.driver
		driver.get("http://localhost/addressbook/")

	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
	unittest.main()
