#Game.py

import numpy as np
class Game:
	gamerange = 3
	def __init__(self):
		self.game_init()
		self.playerList = []
	
	def set_player(self, pl1, pl2):
		# call once
		self.playerList.append(pl1)
		self.playerList.append(pl2)
	
	def game_init(self):
		self.board = -1 * np.ones([Game.gamerange,Game.gamerange])
		self.turn = 0
		self.flag = True
		
	def game_main(self, display = True):
		result = None
		self.game_init()
		while(self.flag):
			x,y = self.game_input()
			self.game_update(x,y)
			result = self.game_judge()
			if(True):
				print("Player{}, ({},{})".format(self.turn,x,y))
				self.game_display()
			self.turn = 1-self.turn
		return result
	
	def game_input(self):
		x, y = self.playerList[self.turn].move(self.board)
		return x,y

	def game_update(self, x, y):
		if(self.board[x,y] == -1):
			self.board[x,y] = self.turn
		else:
			print("update x,y = {},{}".format(x,y))
			self.game_end(1-self.turn)
	
	def game_judge(self):
		result = None
		if (self.board == -1).sum() == 0:
			self.game_end(None)
		diag1 = np.zeros(Game.gamerange)
		diag2 = np.zeros(Game.gamerange)
		for r in range(Game.gamerange):
			s = max((self.board[r,:]==self.turn).sum(), (self.board[:,r]==self.turn).sum())
			if s == Game.gamerange:
				self.game_end(self.turn)
				print("s: {}".format(s))######
				return self.turn
			diag1[r] = self.board[r,r]
			diag2[r] = self.board[r,Game.gamerange - r -1]
		diag = max((diag1 == self.turn).sum(), (diag2==self.turn).sum())
		if diag == Game.gamerange:
			self.game_end(self.turn)
			print("diag: {}".format(diag))#####
			return self.turn

		return None

	def game_display(self):
		print(self.board)
	
	def game_end(self, PlayerID):
		if PlayerID == None:
			self.playerList[0].result(None)
			self.playerList[1].result(None)
			self.flag = False
			return
		self.playerList[PlayerID].result(True)
		self.playerList[1-PlayerID].result(False)
		self.flag = False

