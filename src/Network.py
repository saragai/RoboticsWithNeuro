#Network.py
import numpy as np
from NeuronBrain import NeuronBrain as Neuron
from NeuronInput import NeuronInput
from NeuronOutput import NeuronOutput
from ThreeDimentionalListAccessor import ThreeDimentionalListAccessor

class Network:
	def __init__(self, X, Y, Z, innum, outnum):
		self.X = X
		self.Y = Y
		self.Z = Z
		self.innum = innum
		
		self.nodeList = []
		for x in range(X):
			for y in range(Y):
				for z in range(Z):
					self.nodeList.append(Neuron(self,x,y,z))
		self.nodeList3d = ThreeDimentionalListAccessor(self.nodeList,X,Y,Z)
		
		self.inputNodeList = []
		self.init_input(innum)
		
		self.outputNodeList = []
		self.init_output(outnum)

	def init_input(self, num):
		for i in range(num):
			self.inputNodeList.append(NeuronInput(self, i))

	def init_output(self, num):
		for i in range(num):
			self.outputNodeList.append(NeuronOutput(self,i))


	def init_children(self):
		for node in self.inputNodeList:
			node.init_children()
		for node in self.nodeList:
			node.init_children()

	def fire(self):
		for node in self.inputNodeList:
			node.fire()
		for node in self.nodeList:
			node.fire()
		for node in self.outputNodeList:
			node.fire()

	def post_fire(self):
		for node in self.inputNodeList:
			node.post_fire()
		for node in self.nodeList:
			node.post_fire()
		for node in self.outputNodeList:
			node.post_fire()

	def learn(self):
		for node in self.inputNodeList:
			node.learn()
		for node in self.nodeList:
			node.learn()

	def status(self):
		for node in self.nodeList:
			node.status()
		for node in self.inputNodeList:
			node.status()

if __name__ == '__main__':
	network = Network(2,2,5,4,2)
	network.init_children()
	network.status()
#	for i in range(2):
#		network.fire()
#		print("==fire==",i)
#		network.status()
#		network.post_fire()
#		print("==post_fire==",i)
#		network.status()
