from selenium.webdriver.common.by import By
from model.contact import Contact


class ContactHelper:
	def __init__(self, app):
		self.app = app

	def create(self, contact):
		driver = self.app.driver
		# init contact creation
		driver.find_element(By.LINK_TEXT, "add new").click()
		self.fill_contact_form(contact)
		# submit contact creation
		driver.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()

	def verify_change_field_value(self, field_name, text):
		driver = self.app.driver
		if text is not None:
			driver.find_element(By.NAME, field_name).click()
			driver.find_element(By.NAME, field_name).clear()
			driver.find_element(By.NAME, field_name).send_keys(text)

	def fill_contact_form(self, contact):
		driver = self.app.driver
		# fill contact form
		self.verify_change_field_value("firstname", contact.firstname)
		self.verify_change_field_value("middlename", contact.middlename)
		self.verify_change_field_value("lastname", contact.lastname)
		self.verify_change_field_value("nickname", contact.nickname)
		self.verify_change_field_value("title", contact.title)
		self.verify_change_field_value("company", contact.company)
		self.verify_change_field_value("address", contact.address)
		self.verify_change_field_value("home", contact.home)
		self.verify_change_field_value("mobile", contact.mobile)
		self.verify_change_field_value("work", contact.work)
		self.verify_change_field_value("work", contact.work)
		self.verify_change_field_value("fax", contact.fax)
		self.verify_change_field_value("email", contact.email)
		self.verify_change_field_value("email2", contact.email2)
		self.verify_change_field_value("email3", contact.email3)
		self.verify_change_field_value("homepage", contact.homepage)
		self.verify_change_field_value("address2", contact.address2)
		self.verify_change_field_value("notes", contact.notes)

	def modify_first_contact(self, new_contact_data):
		driver = self.app.driver
		self.select_first_contact()
		# open modify_form
		driver.find_element(By.XPATH, "//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
		# fill contact form
		self.fill_contact_form(new_contact_data)
		# submit modification
		driver.find_element(By.NAME, "update").click()
		self.return_to_home_page()

	def count_contact(self):
		driver = self.app.driver
		self.app.open_home_page()
		return len(driver.find_elements(By.NAME, "selected[]"))

	def select_first_contact(self):
		driver = self.app.driver
		driver.find_element(By.NAME, "selected[]").click()

	def delete_first_contact(self):
		driver = self.app.driver
		self.app.open_home_page()
		self.select_first_contact()
		# submit modification
		driver.find_element(By.CSS_SELECTOR, ".left:nth-child(8) > input").click()
		assert driver.switch_to.alert.text == "Delete 1 addresses?"
		driver.switch_to.alert.accept()

	def return_to_home_page(self):
		driver = self.app.driver
		driver.find_element(By.XPATH, "//div[@id='content']/div/i/a").click()

	def get_contact_list(self):
		driver = self.app.driver
		self.app.open_home_page()
		list_contacts = []
		for element in driver.find_elements(By.XPATH, ".//tr[@name='entry']"):
			text = element.text
			id = element.find_element(By.NAME, "selected[]").get_attribute("value")
			list_contacts.append(Contact(firstname=text, id=id))
		return list_contacts


