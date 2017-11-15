#Network.py
import numpy as np
from NeuronBrain import NeuronBrain as Neuron
from NeuronInput import NeuronInput
class Network:
    def __init__(self, X, Y, Z, innum, outnum):
        self.X = X
        self.Y = Y
        self.z = Z
        self.innum = innum

        self.nodeList = []
        for x in range(X):
            for y in range(Y):
                for z in range(Z):
                    self.nodeList.append(Neuron(self,x,y,z)) 
        self.inputNodeList = []
        self.init_input(innum)


    def init_input(self, num):
        for i in range(num):
            self.inputNodeList.append(NeuronInput(self, i))
        for node in self.inputNodeList:
            node.init_child()


    def fire(self):
        for node in self.inputNodeList:
            node.fire()
        for node in self.nodeList:
            node.fire()

    def post_fire(self):
        for node in self.inputNodeList:
            node.post_fire()
        for node in self.nodeList:
            node.post_fire()
    
    def status(self):
        for node in self.nodeList:
            node.status()
        for node in self.inputNodeList:
            node.status()
            
if __name__ == '__main__':
    network = Network(2,1,1,1,1)
    network.status()
    for i in range(2):
        network.fire()
        print("==fire==",i)
        network.status()
        network.post_fire()
        print("==post_fire==",i)
        network.status()