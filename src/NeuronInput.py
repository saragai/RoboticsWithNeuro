#NeuronInput.py
from NeuronBase import NeuronBase
class NeuronInput(NeuronBase):
	def __init__(self,Network,n):
		NeuronBase.__init__(self,Network)
		self.n = n
		
	def init_child(self):
		self.children.append(self.Network.nodeList[0]) 
	def fire(self):
		self.input = 2
		NeuronBase.fire(self)
	def post_fire(self):
		self.output = 2
		NeuronBase.post_fire(self)
	def status(self):
		pass
	
	def status(self):
		print("""\
InputNode({})
Children	= {}
input		= {}
output		= {}
\n""".format(self.n, self.children, self.input, self.output ))
