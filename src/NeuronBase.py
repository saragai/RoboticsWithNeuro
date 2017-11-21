#NeuronBase.py

class NeuronBase:
	def __init__(self,network):
		self.network = network
		self.children = []
		self.input = 0.0
		self.output = 0.0
		self.fire_flag = False

	def fire(self):
		self.send()
		if(self.output>0):
			for child in self.children:
				#print("{} -> {} val:{} chi:{}".format(self, child[0], self.output, child[0].input))
				pass

	def post_fire(self):
		self.output = self.input
		self.input = 0.0

	def learn(self):
		pass

	def init_children(self):
		pass
		

	def receive(self,gain):
		self.input += gain
	
	def send(self):
		for child in self.children:
			child[0].receive(self.output*child[1])
	

	def status(self):
		pass

