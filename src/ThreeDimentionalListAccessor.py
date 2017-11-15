#ThreeDimentionalListAccessor.py

class ThreeDimentionalListAccessor():
	def __init__(self, _list, x, y, z):
		self.list = _list
		self.x = x
		self.y = y
		self.z = z
	
	def get(self):
		return self.list

	def get(self, x, y, z):
		return self.list[x*self.y*self.z + y*self.z + z]

	def set(self, _list):
		self.list = _list
	
	def set(self, x, y, z, item):
		self.list[x*self.y*self.z + y*self.z + z] = item
