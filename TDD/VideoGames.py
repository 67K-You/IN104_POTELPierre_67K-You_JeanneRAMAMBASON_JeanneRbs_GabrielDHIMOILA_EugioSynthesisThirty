# -*- coding: utf-8 -*-

#Define exceptions
class VideogameError(Exception): pass
class OutOfRangeError(VideogameError): pass
class NotIntegerError(VideogameError): pass
class UnknownTrackError(VideogameError): pass

class VideoGames:
	def __init__(self,setting,players,agerestriction):
		self.setting = setting
		self.players = players
		self.agerestriction = agerestriction

	def JoinGame(self,newplayers):
		self.players += newplayers
		print('%d players have joined the game, you are now %d playing.\n'%(newplayers,self.players))

KnownTracks=("Mario Kart Stadium",
"Water Park",
"Sweet Sweet Canyon",
"Thwomp Ruins",
"Mario Circuit",
"Toad Harbour",
"Twisted Mansion",
"Shy Guy Falls",
"Sunshine Airport",
"Dolphin Shoals",
"Electrodrome",
"Mount Wario",
"Cloudtop Cruise",
"Bone-Dry Dunes",
"Bowser's Castle"
"Rainbow Road")

class Racing(VideoGames):
	def spe(self,track):
		if track not in KnownTracks:
			raise UnknownTrackError, "This track is not part of the game"
		else:
			self.track=track
			print('The race will happen in %s\n' % track)
		return self.track
	def EngineCylinder(self,CC):
		if CC<0:
			raise OutOfRangeError, "CC can't be a negative number"
		elif not CC == int(CC):
			raise NotIntegerError, "CC can't be a decimal number"
		else:
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
