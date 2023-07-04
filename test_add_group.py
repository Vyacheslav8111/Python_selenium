# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest, time, re
from group import Group


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_group(self):
        self.open_home_page()
        self.login(username="Admin", password="secret")
        self.open_groups_page()
        self.create(Group(name="s", header="a", footer="f"))
        self.return_to_groups_page()
        self.logout()

    def test_add_empty_group(self):
        self.open_home_page()
        self.login(username="Admin", password="secret")
        self.open_groups_page()
        self.create(Group(name="", header="", footer=""))
        self.return_to_groups_page()
        self.logout()

    def logout(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_groups_page(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "group page").click()

    def create(self, group):
        driver = self.driver
        # init group creation
        driver.find_element(By.NAME, "new").click()
        # fill group form
        driver.find_element(By.NAME, "group_name").click()
        driver.find_element(By.NAME, "group_name").clear()
        driver.find_element(By.NAME, "group_name").send_keys(group.name)
        driver.find_element(By.NAME, "group_header").click()
        driver.find_element(By.NAME, "group_header").clear()
        driver.find_element(By.NAME, "group_header").send_keys(group.header)
        driver.find_element(By.NAME, "group_footer").click()
        driver.find_element(By.NAME, "group_footer").clear()
        driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        driver.find_element(By.NAME, "submit").click()

    def open_groups_page(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "groups").click()

    def login(self, username, password):
        driver = self.driver
        driver.find_element(By.NAME, "user").click()
        driver.find_element(By.NAME, "user").clear()
        driver.find_element(By.NAME, "user").send_keys(username)
        driver.find_element(By.NAME, "pass").click()
        driver.find_element(By.NAME, "pass").clear()
        driver.find_element(By.NAME, "pass").send_keys(password)
        driver.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()