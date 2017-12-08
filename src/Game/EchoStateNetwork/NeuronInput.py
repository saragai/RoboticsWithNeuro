#NeuronInput.py
from NeuronBase import NeuronBase
class NeuronInput(NeuronBase):
    def __init__(self,network,n):
        NeuronBase.__init__(self,network)
        self.n = n
        self.initWeight = 1.0
    def set_child(self, x, y, z):
        self.children.append([self.network.nodeList3d.get(x, y, z), self.initWeight])
    def fire(self):
        NeuronBase.fire(self)
    def post_fire(self):
        NeuronBase.post_fire(self)
    
    def status(self):
        print("""
--Input
InputNode({})\
""".format(self.n))
        NeuronBase.status(self)

    def __repr__(self):
        s = "input({})".format(self.n)
        return s
