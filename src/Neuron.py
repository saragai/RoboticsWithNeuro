#Neuron.py
import Network as net

class Neuron:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.children = []
		self.input = 0.0
		self.output = 0.0
		self.threshold = 1.0

	def recieve(self, gain):
		self.input += gain

	def send(self):
		for child in self.children:
			child.recieve(self.output)
	
	def afterfire(self):
		if self.input > self.threshold :
			net.addFireList(self)
			self.output = self.input
			self.input = 0.0

	def status(self):
		print("""\
Node({}, {})
Children	= {}
input		= {}
output		= {}
threshold	= {}
\n""".format(self.x, self.y, self.children, self.input, self.output, self.threshold))

