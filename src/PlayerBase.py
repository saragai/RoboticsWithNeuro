#PlayerBase.py

class PlayerBase:
    def __init__(self):
        self.winnum = 0
        self.evennum = 0
        self.losenum = 0
        pass

    def move(self, board):
        #return [x, y]
        pass
    

    def reward(self, board, reward):
        pass

    def result(self, flag):
        if flag is None:
            self.evennum += 1
        elif flag is True:
            self.winnum += 1
        else:
            self.losenum += 1