#main.py

from Game import Game
from PlayerRandom import PlayerRandom
from PlayerHuman import PlayerHuman

game = Game()
pl1 = PlayerRandom()
pl2 = PlayerHuman()

game.set_player(pl1,pl2)

result = game.game_main()

print(result)
