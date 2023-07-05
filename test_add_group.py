# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest, time, re
from group import Group
from application import Application


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.app = Application()
        self.driver = webdriver.Firefox()
    
    def test_add_group(self):
        self.app.login(username="Admin", password="secret")
        self.app.create(Group(name="s", header="a", footer="f"))
        self.app.logout()

    def test_add_empty_group(self):
        self.app.login(username="Admin", password="secret")
        self.app.create(Group(name="", header="", footer=""))
        self.app.logout()

    def tearDown(self):
        self.app.close_browser()
