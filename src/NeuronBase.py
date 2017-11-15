#NeuronBase.py

class NeuronBase:
	def __init__(self,Network):
		self.Network = Network
		self.children = []
		self.input = 0.0
		self.output = 0.0

	def fire(self):
		self.send()

	def post_fire(self):
		self.output = self.input
		self.input = 0.0

	def init_child(self):
		pass
		

	def receive(self,gain):
		self.input = gain
	
	def send(self):
		for child in self.children:
			child.receive(self.output)
	

	def status(self):
		pass

