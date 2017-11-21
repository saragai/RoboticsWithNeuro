#test.py
import numpy as np
from Network import Network 
if __name__ == '__main__':
	inputgen = [0,0]

	network = Network(2,2,5,4,2)
	network.init_children()
	network.status()

	test_result = np.zeros(1000)
	for test_num in range (1000):
		inputgen = np.random.randint(0,2,2)
		inputlist = [ 1-inputgen[0], inputgen[0], 1-inputgen[1], inputgen[1] ]
		answer = 1 if inputgen.sum() == 2 else 0
		for i in range(100):

			for j in range(4):
				network.inputNodeList[j].input = inputlist[j]

			#print("==inputList==", inputlist)
			network.fire()
			#print("==fire==",i)
#		network.status()
			network.learn()
			network.post_fire()
			#print("==post_fire==",i)
#		network.status()

			if network.outputNodeList[0].output < 1.0 and network.outputNodeList[1].output < 1.0:
				continue
			print("output 0: {}, 1: {}".format(network.outputNodeList[0].output, network.outputNodeList[1].output))

			if network.outputNodeList[0].output > network.outputNodeList[1].output:
				print("input : {}".format(inputgen))
				print("testnum {},i {}, result 0, answer {}, output {}".format(test_num, i, answer, network.outputNodeList[0].output))
				if answer == 0:
					test_result[test_num] = 1
			else: 
				print("input : {}".format(inputgen))
				print("testnum {},i {}, result 1, answer {}, output {}".format(test_num, i, answer, network.outputNodeList[1].output))
				if answer == 1:
					test_result[test_num] = 1

			for rest in range(20):
				for j in range(4):
					network.inputNodeList[j].input = 0
				if test_result[test_num] == 1:
					for z in range(0,2):
						for y in range(2):
							for x in range(2):
								network.nodeList3d.get(x,y,z).output = 1.0
				else:
					for z in range(0,2):
						for y in range(2):
							for x in range(2):
								network.nodeList3d.get(x,y,z).output = 0.0

				network.fire()
				network.learn()
				network.post_fire()
			break


		for node in network.nodeList:
			#print(node)
			for child in node.children:
				#print("child{} weight:{}".format(child[0],child[1]))
				pass
	test_result.shape = [10,100]
	print(test_result.sum(axis=1))
