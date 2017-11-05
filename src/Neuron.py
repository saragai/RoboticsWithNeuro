#Neuron.py
import Network as net

class Neuron:
	def __init__(self):
		self.children = []
		self.hub = 0
		self.threshold = 1
		self.flag = False

	def hub(self, gain):
		self.hub += gain
		if self.hub > self.threshold and flag == True:
			net.addFireList(self) # definded in another script

	def forward(self):
		for child in self.children:
			child.hub(self.hub)
	

