import JasperError
import json, requests

class JasperPy(object):
	def __init__(self, url, username, password):
		self.base_url = url + "/"
		self.rest_url = url + "/rest/"
		self.r_v2_url = url + "/rest_v2/"
		self.username = username
		self.password = password

		self.headers = {
			'content-type': 'application/x-www-form-urlencoded'
			, 'accept': 'application/json'
		}
		self.session = requests.session()

	def login(self):
		url     = self.rest_url + "login"
		payload = {
			"j_username"   : self.username
			, "j_password" : self.password
		}

		r = self.session.post(url, headers=self.headers, data=payload)

		if r.status_code == 200:
			return True
		else:
			raise JasperError.JasperError("Could not login")

	def logout(self):
		url = self.base_url + "logout.html"

		r = self.session.get(url, headers=self.headers)

		print(r.url)
		print(r.status_code)

	def search(self, folderURI="", q=""):
		url = self.r_v2_url + "resources"

		payload = {
			"recursive"   : "true"
			, "sortBy"    : "accessTime"
		}

		if q != "":
			payload['q'] = q

		if folderURI != "":
			payload['folderURI'] = folderURI

		r = self.session.get(url, headers=self.headers, data=payload)

		if r.status_code == 200:
			parsed = json.loads(r.text)
			output = json.dumps(parsed, indent=4, sort_keys=True)
			print(output)
		else:
			raise JapserError.JasperError("Could not complete search")