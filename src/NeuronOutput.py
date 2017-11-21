#NeuronOutput.py
from NeuronBase import NeuronBase
class NeuronOutput(NeuronBase):
	def __init__(self,network,n):
		NeuronBase.__init__(self,network)
		self.n = n
		self.parents = []
		self.threshold = 2.0
		self.init_parent()

	def init_parent(self):
		self.parents = [self.network.nodeList3d.get( self.n, 0, 4 ), self.network.nodeList3d.get( self.n, 1, 4 )] 
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
		print("""\
InputNode({})
Parents		= {}
input		= {}
output		= {}
\n""".format(self.n, self.parents, self.input, self.output ))

	def __repr__(self):
		s = "input({})".format(self.n)
		return s
