#NeuronBase.py

class NeuronBase:
	def __init__(self,network):
		self.network = network
		self.children = []
		self.input = 0.0
		self.output = 0.0

	def fire(self):
		self.send()
		if(self.output>0):
			print("children {}.input = {}".format(self.children[0],self.children[0].input))

	def post_fire(self):
		self.output = self.input
		self.input = 0.0

	def init_children(self):
		pass
		

	def receive(self,gain):
		self.input = gain
	
	def send(self):
		for child in self.children:
			child.receive(self.output)
	

	def status(self):
		pass

