#NeuronBase.py
import numpy as np

class NeuronBase:
    def __init__(self,network):
        self.network = network
        self.children = []
        self.input = 0.0
        self.output = 0.0
        self.fireFlag = False

    def fire(self):
        self.send()

    def post_fire(self):
        self.output = self.input
        self.input = 0.0

    def learn(self):
        pass

    def init_children(self):
        pass
        

    def receive(self,gain):
        self.input += gain
    
    def send(self):
        for child in self.children:
            weight = 1.0
            if(child[1]<5):
                weight = 1/(1+np.exp(-child[1]))
            child[0].receive(self.output*weight)

    def status(self):
        print("""\
--Base
Children    = {}
input       = {}
output      = {}
fire_flag   = {}\
""".format(self.children, self.input, self.output, self.fire_flag))
