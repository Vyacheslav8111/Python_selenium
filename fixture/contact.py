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
		self.contact_cache = None

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
		self.verify_change_field_value("lastname", contact.lastname)
		self.verify_change_field_value("home", contact.home_phone)
		self.verify_change_field_value("mobile", contact.mobile_phone)
		self.verify_change_field_value("work", contact.work_phone)
		self.verify_change_field_value("phone2", contact.secondary_phone)

	def modify_first_contact(self):
		driver = self.app.driver
		self.modify_contact_by_index(0)

	# def modify_contact_by_index(self, index, new_contact_data):
	# 	driver = self.app.driver
	# 	self.select_contact_by_index(index)
	# 	# open modify_form
	# 	driver.find_element(By.XPATH, ".//tr[2]/td[8]/a/img").click()
	# 	# fill contact form
	# 	self.fill_contact_form(new_contact_data)
	# 	# submit modification
	# 	driver.find_element(By.XPATH, ".//form[1]/input[22]").click()
	# 	self.return_to_home_page()
	# 	self.contact_cache = None

	def modify_contact_by_index(self, index, new_contact_form):
		driver = self.app.driver
		self.app.open_home_page()
		self.open_contact_to_edit_by_index(index)
		self.fill_contact_form(new_contact_form)
		self.submit_contact_modification()
		self.return_to_home_page()
		self.contact_cashe = None

	# def modify_contact_by_id(self, id, new_contact_data):
	# 	driver = self.app.driver
	# 	self.app.open_home_page()
	# 	self.open_contact_to_edit_by_id(id)
	# 	self.fill_contact_form(new_contact_data)
	# 	self.submit_contact_modification()
	# 	self.return_to_home_page()
	# 	self.contact_cashe = None

	def open_contact_to_edit_by_index(self, index):
		driver = self.app.driver
		self.app.open_home_page()
		row = driver.find_elements(By.NAME, "entry")[index]
		cells = row.find_elements(By.TAG_NAME, "td")[7]
		cells.find_element(By.TAG_NAME, "a").click()

	def submit_contact_modification(self):
		driver = self.app.driver
		driver.find_element(By.XPATH, "//form[1]/input[22]").click()

	def open_contact_to_edit_by_id(self, id):
		driver = self.app.driver
		self.app.open_home_page()
		driver.find_element(By.CSS_SELECTOR, "input[value='%s']" % id)
		cells = driver.find_elements(By.TAG_NAME, "td")[7]
		cells.find_element(By.TAG_NAME, "a").click()

	def count_contact(self):
		driver = self.app.driver
		self.app.open_home_page()
		return len(driver.find_elements(By.NAME, "selected[]"))

	def select_first_contact(self):
		driver = self.app.driver
		driver.find_element(By.NAME, "selected[]").click()

	def select_contact_by_index(self, index):
		driver = self.app.driver
		driver.find_elements(By.NAME, "selected[]")[index].click()

	def delete_first_contact(self):
		driver = self.app.driver
		self.delete_contact_by_index(0)

	def delete_contact_by_index(self, index):
		driver = self.app.driver
		self.app.open_home_page()
		self.select_contact_by_index(index)
		# submit modification
		driver.find_element(By.CSS_SELECTOR, ".left:nth-child(8) > input").click()
		assert driver.switch_to.alert.text == "Delete 1 addresses?"
		driver.switch_to.alert.accept()
		self.contact_cache = None

	def return_to_home_page(self):
		driver = self.app.driver
		driver.find_element(By.XPATH, "//div[@id='content']/div/i/a").click()

	def get_contact_info_from_edit_page(self, index):
		driver = self.app.driver
		self.open_contact_to_edit_by_index(index)
		firstname = driver.find_element(By.NAME, "firstname").get_attribute("value")
		lastname = driver.find_element(By.NAME, "lastname").get_attribute("value")
		address = driver.find_element(By.NAME, "address").get_attribute("value")
		id = driver.find_element(By.NAME, "id").get_attribute("value")
		home_phone = driver.find_element(By.NAME, "home").get_attribute("value")
		work_phone = driver.find_element(By.NAME, "work").get_attribute("value")
		mobile_phone = driver.find_element(By.NAME, "mobile").get_attribute("value")
		secondary_phone = driver.find_element(By.NAME, "phone2").get_attribute("value")
		return Contact(firstname=firstname, lastname=lastname, address=address,
					   id=id,
					   home_phone=home_phone, work_phone=work_phone,
					   mobile_phone=mobile_phone, secondary_phone=secondary_phone)

	contact_cache = None

	def get_contact_list(self):
		if self.contact_cache is None:
			driver = self.app.driver
			self.app.open_home_page()
			self.contact_cache = []
			for row in driver.find_elements(By.NAME, "entry"):
				cells = row.find_elements(By.TAG_NAME, "td")
				id = cells[0].find_element(By.TAG_NAME, "input").get_attribute("value")
				lastname = cells[1].text
				firstname = cells[2].text
				address = cells[3].text
				all_phones = cells[5].text
				self.contact_cache.append(Contact
										  (firstname=firstname,
										   lastname=lastname, address=address,
										   id=id,
										   all_phones_from_home_page=all_phones))
		return list(self.contact_cache)
