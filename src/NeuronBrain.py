#NeuronBrain.py
from NeuronBase import NeuronBase
import numpy as np

class NeuronBrain(NeuronBase):
	def __init__(self,network,x,y,z):
		NeuronBase.__init__(self,network)
		self.x = x
		self.y = y
		self.z = z
		self.threshold = 0.01
		self.init_weight = 1.0


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
					self.children.append([self.network.nodeList[ni], self.init_weight])
					break
	
	def learn(self):
		if self.input > self.threshold :
			for child in self.children:
				if child[0].fire_flag :
					child[1] *= 1.1
				else:
					child[1] *= 0.99

	def post_fire(self):
		if self.input > self.threshold :
			self.fire_flag = True
			self.output = self.init_weight/(1.0+np.exp(-self.input))
		else:
			self.fire_flag = False
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
