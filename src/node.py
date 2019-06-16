class Node(object):
	def __init__(self, city_name, g, h=0, parent=None):
		self.parent = parent
		self.children = []
		self.city_name = city_name
		self.h = h
		self.g = g
		self.f = self.h + self.g
	def __str__(self):
		return "City {}, the f value is: {}. ".format(self.city_name,str(self.f))
	def add_child(self, obj):
		self.children.append(obj)