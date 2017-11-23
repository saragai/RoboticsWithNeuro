#NeuronOutput.py
from NeuronBase import NeuronBase
class NeuronOutput(NeuronBase):
	def __init__(self,network,n):
		NeuronBase.__init__(self,network)
		self.n = n
		self.parents = []
		self.threshold = 1.0

	def set_parent(self, x, y, z):
		self.parents.append(self.network.nodeList3d.get(x, y, z)) 

	def fire(self):
		for parent in self.parents:
			self.input += parent.output

	def post_fire(self):
		if self.threshold < self.input:
			self.output = self.input
		else:
			self.output = 0.0
		self.input = 0.0

	def status(self):
		print("""
InputNode({})
Parents		= {}
input		= {}
output		= {}\
""".format(self.n, self.parents, self.input, self.output ))
		NeuronBase.status(self)

	def __repr__(self):
		s = "input({})".format(self.n)
		return s
