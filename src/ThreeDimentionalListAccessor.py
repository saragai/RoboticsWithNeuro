#ThreeDimentionalListAccessor.py

class ThreeDimentionalListAccessor():
	def __init__(self, _list, x, y, z):
		self.list = _list
		self.x = x
		self.y = y
		self.z = z
	
	def get(self, x=-1, y=-1, z=-1):
		if(x<0 or y<0 or z<0):
			return self.list
		return self.list[x*self.y*self.z + y*self.z + z]

	
	def set(self, item, x=-1, y=-1, z=-1):
		if(x<0 or y<0 or z<0):
			return self.list
		self.list[x*self.y*self.z + y*self.z + z] = item
