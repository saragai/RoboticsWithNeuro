#PlayerRandom.py
from PlayerBase import PlayerBase
import numpy as np

class PlayerRandom(PlayerBase):
	def __init__(self):
		PlayerBase.__init__(self)

	def move(self, board):
		gamerange = board.shape[0]
		empty = (board == -1)
		xarg = list(range(gamerange))
		yarg = list(range(gamerange))
		np.random.shuffle(xarg)
		np.random.shuffle(yarg)
		for x in xarg:
			for y in yarg:
				if empty[x,y] == True:
					return x,y
		print("Error, random move")
		return None
