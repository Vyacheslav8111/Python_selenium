from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:
	def __init__(self):
		self.driver = webdriver.Chrome()
		self.session = SessionHelper(self)
		self.group = GroupHelper(self)
		self.contact = ContactHelper(self)
		self.driver.maximize_window()
		#self.driver.implicitly_wait(20)



	def is_valid(self):
		try:
			self.driver.current_url
			return True
		except:
			return False

	def open_home_page(self):
		driver = self.driver
		driver.get("http://localhost/addressbook/")

	def close_browser(self):
		self.driver.quit()
