# PlayerQ.py
from . import PlayerBase
import numpy as np
PlayerBase = PlayerBase.PlayerBase

class PlayerQ(PlayerBase):
    def __init__(self, gamerange, gamma=.9, alpha=.1, epsilon=.1):
        PlayerBase.__init__(self)
        self.gamerange = gamerange
        self._Q = np.zeros(3**(gamerange**2) * gamerange**2)
        self.actions = np.array([[x, y] for x in range(gamerange) for y in range(gamerange)])
        self.gamma = gamma
        self.alpha = alpha
        self.epsilon = epsilon
        self.oldBoard = np.zeros([gamerange, gamerange])
        self.oldAction = None
        
        
    def scalar_board_action(self, board, action):
        board.shape = [board.size]
        ret = 0
        for i in range(board.size):
            ret += 3**i * board[i]
        ret += 3**(i+1) * action[0]
        ret += 3**(i+2) * action[1]
        board.shape = [self.gamerange, self.gamerange]
        return int(ret)
    
    def Q(self, board, action):
        #print("board",board)
        #print("action",action)
        #print("scalar",self.scalar_board_action(board, action))
        return self._Q[self.scalar_board_action(board, action)]
        
    def move(self, board):
        self.oldBoard = board
        #if board[1,1] == 2:
        #    self.oldAction = [1,1]
        #    return [1,1]
        if np.random.rand() < self.epsilon:
            arg = np.random.randint(0, self.gamerange**2)
        else:
            arg = self.argmax_action(board)
            if board[self.actions[arg][0], self.actions[arg][1]] != 2:
                self.suicide += 1
            """
            while(True):
                arg = self.argmax_action(board)
                if board[self.actions[arg][0], self.actions[arg][1]] != 2:
                    self._Q[self.scalar_board_action(board, self.actions[arg])] -= 1000
                else:
                    break;
            """
        self.oldAction = self.actions[arg]
        return self.actions[arg]
    
    def reward(self, board, reward):
        if self.oldAction is None:
            #print("oldAction is None")
            return
        
        #print("reward : ",reward)
        
            
        """
            print("board")
            print(board)
            print("oldboard")
            print(self.oldBoard)
            print("action: ",self.oldAction)
        """
        actarg = self.argmax_action(board)
        qarg = self.scalar_board_action(self.oldBoard, self.oldAction)
        oldQ = self._Q[qarg]
        self._Q[qarg] += self.alpha * (reward + self.gamma * self.Q(board, self.actions[actarg]) - oldQ)
        if reward != 0:
            self.oldBoard = 2*np.ones([self.gamerange, self.gamerange])
            self.oldAction = None
    
    def argmax_action(self, board):
        actarg = 0
        actmax = -1000
        for ai in range(self.gamerange**2):
            q = self.Q(board, self.actions[ai])
            if q > actmax:
                actmax = q
                actarg = ai
        return actarg
        

    
