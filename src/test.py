#test.py
import numpy as np
from Network import Network 
if __name__ == '__main__':
	inputgen = [0,0]

	network = Network(2,2,5,4,2)
	network.init_children()
	network.status()
	for i in range(100):
		inputgen = np.random.randint(0,2,2)
		inputlist = [ 1-inputgen[0], inputgen[0], 1-inputgen[1], inputgen[1] ]

		for j in range(4):
			network.inputNodeList[j].input = inputlist[j]

		print("==inputList==", inputlist)
		network.fire()
		print("==fire==",i)
#		network.status()
		network.learn()
		network.post_fire()
		print("==post_fire==",i)
#		network.status()

		if network.nodeList3d.get(0,0,4).output + network.nodeList3d.get(0,1,4).output >= 1 :
			print("result 0, count {}".format(i))
			break
		if network.nodeList3d.get(1,0,4).output + network.nodeList3d.get(1,1,4).output >= 1 :
			print("result 1, count {}".format(i))
			break
	for node in network.nodeList:
		print(node)
		for child in node.children:
			print("child{} weight:{}".format(child[0],child[1]))

