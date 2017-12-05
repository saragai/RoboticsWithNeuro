#main.py
import numpy as np
from Game import Game
from PlayerRandom import PlayerRandom
from PlayerHuman import PlayerHuman
from PlayerQ import PlayerQ

game = Game()
pl0 = PlayerRandom()
pl1 = PlayerRandom()
#pl0 = PlayerQ(Game.gamerange, gamma=.9, alpha=.1, epsilon=.05)
#pl1 = PlayerQ(Game.gamerange, gamma=.9, alpha=.1, epsilon=.05)
#pl1 = PlayerHuman()

game.set_player(pl1,pl0)

for i in range(10000):
    game.game_main()
    if i%1000 == 0:
        
        print("win:{}, even:{}, lose:{}, suicide:{}".format(pl1.winnum, pl1.evennum, pl1.losenum, pl1.suicide))
        pl1.winnum = 0
        pl1.losenum = 0
        pl1.evennum = 0
        pl1.suicide = 0
        game.game_change_order()


#print("====player0====")
#print(pl0.resultList)
#print("")
print("====player1====")
#result = np.array(pl1.resultList)
#result.shape = [10,1000]
#print(result.sum(axis = 1))
