#NeuronBrain.py
from NeuronBase import NeuronBase
import numpy as np

class NeuronBrain(NeuronBase):
	def __init__(self,network,x,y,z):
		NeuronBase.__init__(self,network)
		self.x = x
		self.y = y
		self.z = z
		self.threshold = 1.0
		self.init_weight = 0.5
		self.learn_rate = 1.2
		self.forget_rate = 0.9
		self.useless_rate = 0.95
		self.children_num = 3
		self.distance = []

	def init_distance(self):
		if self.distance != []:
			return
		distance = np.zeros(self.network.size) 
		for ni in range(self.network.size):
			node = self.network.nodeList[ni]
			if (self.x == node.x and self.y == node.y and self.z == node.z):
				distance[ni] = np.inf
			else: 
				distance[ni] = (node.x - self.x)**2 + (node.y - self.y)**2 + (node.z - self.z)**2 

		distance = 1 / distance
		distance = distance / distance.sum()
		self.distance = distance

	def set_child(self):
		rand = np.random.rand()
		for ni in range(self.network.size):
			rand -= self.distance[ni]
			if(rand <= 0.):
				self.children.append([self.network.nodeList[ni], self.init_weight])
				return

	def init_children(self):
		print(self)
		self.init_distance()
		print(self.distance)
		for ci in range(self.children_num):
			self.set_child()

	def learn(self):
		if self.input > self.threshold:
			for child in self.children:
				if child[0].fire_flag:
					child[1] *= self.learn_rate
					if child[1] > 1.0:
						child[1] = 1.0
				else:
					child[1] *= self.forget_rate
		else:
			for child in self.children:
				child[1] *= self.useless_rate

		for ci in range(self.children_num):
			if self.children[ci][1] < 0.1:
				del self.children[ci]
				self.set_child()

	def post_fire(self):
		if self.input > self.threshold:# and self.fire_flag == False:
			self.fire_flag = True
			self.output = 1.0
		else:
			self.fire_flag = False
			self.output = 0.0
		self.input = 0.0

	def status(self):
		print("""
--Brain
BrainNode({}, {}, {})
threshold	= {}\
""".format(self.x, self.y, self.z, self.threshold))
		NeuronBase.status(self)

	def __repr__(self):
		s = "({}, {}, {})".format(self.x, self.y, self.z)
		return s
