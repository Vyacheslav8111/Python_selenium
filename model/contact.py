from sys import maxsize


class Contact:
	def __init__(self, id=None, firstname=None, lastname=None, address=None, address2=None, home_phone=None, \
				 mobile_phone=None, \
				 work_phone=None,
				 secondary_phone=None, all_phones_from_home_page=None, all_phones_from_view_page=None,
				 all_emails_from_home_page=None, all_main_info_from_home_page=None):
		self.id = id
		self.firstname = firstname
		self.lastname = lastname
		self.address = address
		self.address2 = address2
		self.home_phone = home_phone
		self.mobile_phone = mobile_phone
		self.work_phone = work_phone
		self.secondary_phone = secondary_phone
		self.all_phones_from_home_page = all_phones_from_home_page
		self.all_phones_from_view_page = all_phones_from_view_page
		self.all_emails_from_home_page = all_emails_from_home_page
		self.all_main_info_from_home_page = all_main_info_from_home_page

	def __repr__(self):
		return "%s:%s:%s:%s:%s:%s:%s:%s" % (self.id, self.lastname, self.firstname, self.address, self.home_phone,
											self.mobile_phone,
											self.work_phone, self.secondary_phone)

	def __eq__(self, other):
		return (self.id is None or other.id is None or self.id == other.id) and \
			self.lastname == other.lastname and self.firstname == other.firstname and self.address == other.address and self.all_phones_from_home_page == other.all_phones_from_home_page and self.all_emails_from_home_page == other.all_emails_from_home_page

	def id_or_max(self):
		if self.id:
			return int(self.id)
		else:
			return maxsize
