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
		
knownNames = ('Mario' , 'Pit' , 'Donkey Kong', 'Link', 'Kirby', 'Yoshi' , 'Fox', 'Pikachu', 'Luigi', 'Peach', 'Ness' , 'Zelda', 'Captain Falcon')
knownWeapons = ('Super Launch Star', 'Smash Ball', 'Poké Ball', 'Beam Sword', 'Super Scope', 'Banana Gun' , 'Drill', 'Super Mushroom')

class Fighting(VideoGames):
	def nameofplayer1(self,P1name):
		if not (P1name in knownNames):
			raise UnknownPlayerError, "Unknown Player Name"
		self.P1name=P1name
		print('Here comes %s!\n' % P1name)
	
	def equipweapon(self,weapon):
		if not (weapon in knownWeapons):
			raise UnknownWeaponError, "Unknown Weapon Name"
		self.weapon=weapon
		print('You equip %s\n' % weapon)

	def timefight(self,time):
		if not (0<time<9):
			raise OutOfRangeError, "time must be between 1 and 8 minutes"
		if int(time) <> time:
			raise NotIntegerError, "non-integers can not be time"
		print('You have %d minutes ! Good luck ! \n' %time)

	

		
#MarioKart = Racing('Desert',1,3)
#MarioKart.__spe__('Dry Dry Desert')
#MarioKart.JoinGame(2)
#MarioKart.EngineCylinder(150)
