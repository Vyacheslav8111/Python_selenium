from selenium import webdriver
from selenium.webdriver.common.by import By


class Application:
	def __init__(self):
		self.driver = webdriver.Firefox()

	def open_home_page(self):
		driver = self.driver
		driver.get("http://localhost/addressbook/")

	def login(self, username, password):
		driver = self.driver
		self.open_home_page()
		driver.find_element(By.NAME, "user").click()
		driver.find_element(By.NAME, "user").clear()
		driver.find_element(By.NAME, "user").send_keys(username)
		driver.find_element(By.NAME, "pass").click()
		driver.find_element(By.NAME, "pass").clear()
		driver.find_element(By.NAME, "pass").send_keys(password)
		driver.find_element(By.XPATH, "//input[@value='Login']").click()

	def open_groups_page(self):
		driver = self.driver
		driver.find_element(By.LINK_TEXT, "groups").click()

	def group_create(self, group):
		driver = self.driver
		self.open_groups_page()
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
		self.return_to_groups_page()

	def contact_create(self, contact):
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
		#self.return_to_home_page()

	def return_to_groups_page(self):
		driver = self.driver
		driver.find_element(By.LINK_TEXT, "group page").click()

	def logout(self):
		driver = self.driver
		driver.find_element(By.LINK_TEXT, "Logout").click()

	def close_browser(self):
		self.driver.quit()


