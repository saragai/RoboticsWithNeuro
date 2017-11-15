#NeuronBrain.py
from NeuronBase import NeuronBase

class NeuronBrain(NeuronBase):
	def __init__(self,Network,x,y,z):
		NeuronBase.__init__(self,Network)
		self.x = x
		self.y = y
		self.z = z
		self.threshold = 1.0


		
	
	def post_fire(self):
		if self.input > self.threshold :
			self.output = self.input
			self.input = 0.0

	def status(self):
		print("""\
BrainNode({}, {}, {})
Children	= {}
input		= {}
output		= {}
threshold	= {}
\n""".format(self.x, self.y, self.z, self.children, self.input, self.output, self.threshold))

