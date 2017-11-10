#Network.py
import numpy as np

class Network:
	def __init__(self, innum, outnum):
		self.nodeList = np.zeros([5, 5])
		self.fireNodeList = [] 
		pass
	def add_node_list(self, node, x, y):
		self.nodeList[x,y] = node
		pass
	def input_init(self):


		pass
	def fire(self):
		for fireNode in self.addFireList:
			fireNode.forward()
		for node in self.nodeLiset:
			node.afterfire()
