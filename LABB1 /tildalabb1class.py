class Location(object):
	"""Klass för "plats". Innehåller attributerna name,
    ge_description, latitud, longitid, uppdateringsdatum"""

	def __init__(self, name, geo_desc, latitude, longitude, date):
		self.name = name
		self.geo_desc = geo_desc
		self.latitude = latitude
		self.longitude = longitude
		self.date = date

	def get_name(self):
		return self.name

	def get_geo_desc(self):
		return geo_description

	def get_latitude(self):
		return latitude
	def get_longitude(self):
		return longitude
	def get_date(self):
		return date

	def __str__(self):
		return self.name + "\n" + self.geo_desc + "\n"+ self.latitude+ "\n"+self.longitude+ "\n"+self.date
