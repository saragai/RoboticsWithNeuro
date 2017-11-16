#NeuronInput.py
from NeuronBase import NeuronBase
class NeuronInput(NeuronBase):
	def __init__(self,network,n):
		NeuronBase.__init__(self,network)
		self.n = n
		
	def init_children(self):
		self.children.append(self.network.nodeList3d.get(self.n % 2, self.n // 2, 0)) 
	def fire(self):
		self.send()
		NeuronBase.fire(self)
	def post_fire(self):
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
