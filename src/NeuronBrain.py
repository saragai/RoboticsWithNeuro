#NeuronBrain.py
from NeuronBase import NeuronBase
import numpy as np

class NeuronBrain(NeuronBase):
	def __init__(self,network,x,y,z):
		NeuronBase.__init__(self,network)
		self.x = x
		self.y = y
		self.z = z
		self.threshold = 0.7


	def init_children(self):
		distance = np.array([ np.inf if (self.x == node.x and self.y == node.y and self.z == node.z) else (node.x-self.x)**2 + (node.y-self.y)**2 + (node.z-self.z)**2 for node in self.network.nodeList ])
		distance = 1 / (distance)
		distance = distance / distance.sum()
		#print("distance = {}".format(distance))
		for ci in range(3):
			rand = np.random.rand()
			#print("rand = {}".format(rand))
			for ni in range(self.network.X * self.network.Y * self.network.Z):
				#print("({}) distance = {}".format(ni, distance[ni]))
				rand -= distance[ni]
				if(rand <= 0.):
					self.children.append(self.network.nodeList[ni])
					break
	
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

	def __repr__(self):
		s = "({}, {}, {})".format(self.x, self.y, self.z)
		return s
