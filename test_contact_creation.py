# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class TestContactCreation(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.base_url = "https://www.google.com/"
		self.verificationErrors = []
		self.accept_next_alert = True

	def test_contact_creation(self):
		driver = self.driver
		driver.get("http://localhost/addressbook/")
		driver.find_element(By.NAME, "user").click()
		driver.find_element(By.NAME, "user").clear()
		driver.find_element(By.NAME, "user").send_keys("Admin")
		driver.find_element(By.NAME, "pass").click()
		driver.find_element(By.NAME, "pass").clear()
		driver.find_element(By.NAME, "pass").send_keys("secret")
		driver.find_element(By.XPATH, "//input[@value='Login']").click()
		driver.find_element(By.LINK_TEXT, "add new").click()
		driver.find_element(By.NAME, "firstname").click()
		driver.find_element(By.NAME, "firstname").clear()
		driver.find_element(By.NAME, "firstname").send_keys("q")
		driver.find_element(By.NAME, "middlename").click()
		driver.find_element(By.NAME, "middlename").clear()
		driver.find_element(By.NAME, "middlename").send_keys("w")
		driver.find_element(By.NAME, "lastname").click()
		driver.find_element(By.NAME, "lastname").clear()
		driver.find_element(By.NAME, "lastname").send_keys("e")
		driver.find_element(By.NAME, "nickname").click()
		driver.find_element(By.NAME, "nickname").clear()
		driver.find_element(By.NAME, "nickname").send_keys("r")
		driver.find_element(By.NAME, "title").click()
		driver.find_element(By.NAME, "title").clear()
		driver.find_element(By.NAME, "title").send_keys("t")
		driver.find_element(By.NAME, "company").click()
		driver.find_element(By.NAME, "company").clear()
		driver.find_element(By.NAME, "company").send_keys("y")
		driver.find_element(By.NAME, "address").click()
		driver.find_element(By.NAME, "address").clear()
		driver.find_element(By.NAME, "address").send_keys("u")
		driver.find_element(By.NAME, "home").click()
		driver.find_element(By.NAME, "home").clear()
		driver.find_element(By.NAME, "home").send_keys("67767-8778")
		driver.find_element(By.NAME, "mobile").click()
		driver.find_element(By.NAME, "mobile").clear()
		driver.find_element(By.NAME, "mobile").send_keys("56565-325")
		driver.find_element(By.NAME, "work").click()
		driver.find_element(By.NAME, "work").clear()
		driver.find_element(By.NAME, "work").send_keys("6688")
		driver.find_element(By.NAME, "fax").click()
		driver.find_element(By.NAME, "fax").clear()
		driver.find_element(By.NAME, "fax").send_keys("5657678")
		driver.find_element(By.NAME, "email").click()
		driver.find_element(By.NAME, "email").clear()
		driver.find_element(By.NAME, "email").send_keys("test@test.test")
		driver.find_element(By.NAME, "email2").click()
		driver.find_element(By.NAME, "email2").clear()
		driver.find_element(By.NAME, "email2").send_keys("test123@test.test")
		driver.find_element(By.NAME, "email3").click()
		driver.find_element(By.NAME, "email3").clear()
		driver.find_element(By.NAME, "email3").send_keys("test78@test1.test")
		driver.find_element(By.NAME, "homepage").click()
		driver.find_element(By.NAME, "homepage").clear()
		driver.find_element(By.NAME, "homepage").send_keys("www.testUI.test")
		driver.find_element(By.NAME, "address2").click()
		driver.find_element(By.NAME, "address2").clear()
		driver.find_element(By.NAME, "address2").send_keys("test")
		driver.find_element(By.NAME, "notes").click()
		driver.find_element(By.NAME, "notes").clear()
		driver.find_element(By.NAME, "notes").send_keys("test")
		driver.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
		driver.find_element(By.LINK_TEXT, "home page").click()
		driver.find_element(By.LINK_TEXT, "Logout").click()

	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
	unittest.main()