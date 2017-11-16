#test.py
import numpy as np
from Network import Network 
if __name__ == '__main__':
	inputgen = [0,0]

	network = Network(2,2,5,4,2)
	network.init_children()
	network.status()
	for i in range(2):
		inputgen = np.random.randint(0,2,2)
		inputlist = [ 1-inputgen[0], inputgen[0], 1-inputgen[1], inputgen[1] ]

		for j in range(4):
			network.inputNodeList[j].input = inputlist[j]

		print("==inputList==", inputlist)
		network.fire()
		print("==fire==",i)
		network.status()
		network.post_fire()
		print("==post_fire==",i)
		network.status()
