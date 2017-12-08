#Game.py

import numpy as np
class Game:
    gamerange = 3
    display = False
    def __init__(self):
        self.game_init()
        self.playerList = []
        
    def set_player(self, pl1, pl2):
        # call once
        self.playerList.append(pl1)
        self.playerList.append(pl2)
    
    def game_init(self):
        self.board = 2 * np.ones([Game.gamerange,Game.gamerange])
        self.turn = 0
        self.flag = True
    
    def game_change_order(self):
        self.playerList[0], self.playerList[1] = self.playerList[1], self.playerList[0]
        
    def game_main(self):
        self.game_init()
        while(self.flag):
            if(Game.display):
                self.game_display()
            x,y = self.game_input()
            if(Game.display):
                print("Player{}, ({},{})".format(self.turn,x,y))
            self.game_update(x,y)
            reward = self.game_judge()
            self.game_reward(reward)
            self.turn = 1 - self.turn
    
    def game_input(self):
        x, y = self.playerList[self.turn].move(self.board)
        return x,y

    def game_update(self, x, y):
        if(self.board[x,y] == 2):
            self.board[x,y] = self.turn
        else:
            if(Game.display):
                print("update x,y = {},{}".format(x,y))
            reward = -100*self.game_end(1-self.turn)
            self.game_reward(reward)
    
    def game_judge(self):
        if (self.board == 2).sum() == 0:
            reward = self.game_end(None)
            return reward
        
        diag1 = np.zeros(Game.gamerange)
        diag2 = np.zeros(Game.gamerange)
        for r in range(Game.gamerange):
            s = max((self.board[r,:]==self.turn).sum(), (self.board[:,r]==self.turn).sum())
            if s == Game.gamerange:
                reward = self.game_end(self.turn)
                return reward
            diag1[r] = self.board[r, r]
            diag2[r] = self.board[r, Game.gamerange - r -1]
        diag = max((diag1 == self.turn).sum(), (diag2==self.turn).sum())
        if diag == Game.gamerange:
            reward = self.game_end(self.turn)
            return reward

        return -0.05

    def game_display(self):
        print(self.board)
    
    def game_reward(self, reward):
        self.playerList[self.turn].reward(self.board, reward)
        self.playerList[1-self.turn].reward(self.board, -reward)
    
    def game_end(self, PlayerID):
        if PlayerID == None:
            self.playerList[0].result(None)
            self.playerList[1].result(None)
            self.flag = False
            return 0
        self.playerList[PlayerID].result(True)
        self.playerList[1-PlayerID].result(False)
        self.flag = False
        return 1

