#Network.py
import numpy as np

class Network:
	def __init__(self, innum, outnum):
		self.NodeList = np.zeros([5, 5])
		self.addFireList = []
		pass
	def add_node_list(self, node, x, y):
		pass
	def input_init(self):
		pass
	def fire(self):
		for fireNode in self.addFireList:
			fireNode.forward()
		for node in self.nodeLiset:
			node.afterfire()
