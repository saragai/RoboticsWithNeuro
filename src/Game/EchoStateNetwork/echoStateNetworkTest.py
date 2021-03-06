#test.py
import numpy as np
from Network import Network 

def judge(network):
    out0 = network.outputNodeList[0].output
    out1 = network.outputNodeList[1].output
    if out0 < 1.0 and out1 < 1.0:
        return -1

    print("output 0: {}, 1: {}".format(out0, out1))

    if out0 > out1:
        return 0
    else: 
        return 1

def set_input(network):
    ni = 0
    for node in network.inputNodeList:
        node.set_child(ni%2, ni//2, 0)
        ni += 1

def set_output(network):
    ni = 0
    for node in network.outputNodeList:
        node.set_parent(ni,0,1)
        node.set_parent(ni,1,1)
        ni += 1

inputgen = [0,0]

network = Network(2,2,2)
network.init_input(4)
network.init_output(2)

set_input(network)
set_output(network)

test_result = np.zeros(1000)
for test_num in range (1000):
    inputgen = np.random.randint(0,2,2)
    inputlist = [ 1-inputgen[0], inputgen[0], 1-inputgen[1], inputgen[1] ]
    answer = 1 if inputgen.sum() == 2 else 0
        
    print("==================== no.{} =========================".format(test_num))
    #network.status()
    for i in range(100):

        for j in range(4):
            if i == 0:
                network.inputNodeList[j].input = inputlist[j]
            else:
                network.inputNodeList[j].input = 0
        

        network.fire()
        network.learn()
        network.post_fire()
        
        out = judge(network)
        if out == -1:
            if i == 99:
                print("test_num = {}, NO OUTPUT".format(test_num))
                for node in network.nodeList:
                    del node.children[0]
                    node.set_child()
            continue

        if i == 0:
            print("test_num = {}, 1st step".format(test_num))
            for node in network.nodeList:
                del node.children[0]
                node.set_child()
                
        print("(testnum. i) = ({}. {}), (ans, out) = ({}, {})".format(test_num, i, answer, out)) 
        test_result[test_num] = (out == answer)
        if not test_result[test_num]:
            for node in network.nodeList:
                maxweight=-5
                maxarg=0
                for arg in range(node.childrenNum):
                    child = node.children[arg]
                    if child[1] > maxweight:
                        maxweight = child[1]
                        maxarg = arg
                del node.children[arg]
                node.set_child()
                
        """
        for rest in range(20):
            for j in range(4):
                network.inputNodeList[j].input = 0
            for z in range(0,2):
                for y in range(2):
                    for x in range(2):
                        network.nodeList3d.get(x,y,z).output = test_result[test_num]

            #network.fire()
            #network.learn()
            #network.post_fire()
        """
        break


    for node in network.nodeList:
        #print(node)
        for child in node.children:
            #print("child{} weight:{}".format(child[0],child[1]))
            pass
test_result.shape = [10,100]
print(test_result.sum(axis=1))
