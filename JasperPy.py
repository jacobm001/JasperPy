import requests

class JasperPy:
	def __init__(self, url, username, password):
		self.base_url = url
		self.username = username
		self.password = password

		self.headers = {
			'content-type': 'application/x-www-form-urlencoded'
			, 'accept': 'application/json'
		}
		self.session = requests.session()

	def login(self):
		url     = base_url + "/login"
		payload = {
			"j_username"   : self.username
			, "j_password" : self.password
		}

		r = self.session.post(url, headers=headers, data=payload)

		if r.status_code = "200":
			return True
		