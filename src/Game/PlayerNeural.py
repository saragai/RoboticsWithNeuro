#PlayerNeural.py

from . import PlayerBase
import EchoStateNetwork.Network

PlayerBase = PlayerBase.PlayerBase
Network = EchoStateNetwork.Network.Network

class PlayerNeural(PlayerBase):
	def __init__(self):
		self.Network = Network()
		self.Network
	def move(self, board):
		
		pass
	
	def result(self, res):

		pass

