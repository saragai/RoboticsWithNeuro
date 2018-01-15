#main.py
import numpy as np
import Game.Game
import Game.PlayerRandom as PlayerRandom
import Game.PlayerHuman as PlayerHuman
import Game.PlayerQ as PlayerQ

PlayerRandom = PlayerRandom.PlayerRandom
PlayerHuman = PlayerHuman.PlayerHuman
PlayerQ = PlayerQ.PlayerQ
Game = Game.Game
game = Game.Game()
#pl0 = PlayerRandom()
pl0 = PlayerQ(game.gamerange, gamma=.9, alpha=.1, epsilon=.1)
pl1 = PlayerQ(game.gamerange, gamma=.9, alpha=.1, epsilon=.1)
pl2 = PlayerHuman()

game.set_player(pl1,pl1)

for i in range(10000):
    game.game_main()
    if i%1000 == 999:
        
        print("win:{}, even:{}, lose:{}, suicide:{}".format(pl1.winnum, pl1.evennum, pl1.losenum, pl1.suicide))
        pl1.winnum = 0
        pl1.losenum = 0
        pl1.evennum = 0
        pl1.suicide = 0
        game.game_change_order()

pl0.epsilon = 0
pl1.epsilon = 0

for i in range(1000):
    game.game_main()
print("win:{}, even:{}, lose:{}, suicide:{}".format(pl1.winnum, pl1.evennum, pl1.losenum, pl1.suicide))

#print("====player0====")
#print(pl0.resultList)
#print("")
print("====player1====")
#result = np.array(pl1.resultList)
#result.shape = [10,1000]
#print(result.sum(axis = 1))
