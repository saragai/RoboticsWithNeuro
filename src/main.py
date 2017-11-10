#main.py

from Game import Game
from RandomPlayer import RandomPlayer

game = Game()
pl1 = RandomPlayer()
pl2 = RandomPlayer()

game.set_player(pl1,pl2)

result = game.game_main()

print(result)