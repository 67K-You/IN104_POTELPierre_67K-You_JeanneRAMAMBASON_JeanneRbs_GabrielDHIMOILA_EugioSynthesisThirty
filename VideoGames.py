class VideoGames:
	def __init__(self,setting,players,agerestriction):
		self.setting = setting
		self.players = players
		self.agerestriction = agerestriction

	def JoinGame(self,newplayers):
		self.players += newplayers
		print('%d players have joined the game, you are now %d playing.\n'%(newplayers,self.players))



class Racing(VideoGames):
	def __spe__(self,track):
		self.track=track
		print('The race will happen in %s\n' % track)
	def EngineCylinder(self,CC):
		self.CC=CC
		print('You chose %d CC. 3, 2, 1 GO!\n' % CC)

class Fighting(VideoGames):
	def nameofplayer1(self,P1name):
		self.P1name=P1name
		print('Here comes %s!\n' % P1name)
	def equipweapon(self,weapon):
		self.weapon=weapon
		print('You equip %s\n' % weapon)


#MarioKart = Racing('Desert',1,3)
#MarioKart.__spe__('Dry Dry Desert')
#MarioKart.JoinGame(2)
#MarioKart.EngineCylinder(150)