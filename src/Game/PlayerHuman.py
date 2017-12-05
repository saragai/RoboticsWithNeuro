#PlayerHuman.py
import numpy as np
import PlayerBase

class PlayerHuman(PlayerBase):
	def __init__(self):
		PlayerBase.__init__(self)
	
	def move(self, board):
		x,y = np.array(input('x y = ').split(),dtype = int)
		return x,y
