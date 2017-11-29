import time
from random import shuffle

class GameInstance:

	def __init__(self, diff = -1):
		while diff < 1 or diff > 3:
			diff = raw_input("Please choose a difficulty level (1-3): ")
			diff = int(diff)
		self.difficulty = diff
		self.time = 5 #time left in seconds
		self.timeleft = self.time+3
		
		self.complete = False
		self.minigames = ['wires', 'images', 'gestures', 'voice']
		shuffle(self.minigames)
		self.minigames.append('wirecutting')


	def kill(self):
		del self

	def get_difficulty(self):
		print "Difficulty level: " + str(self.difficulty)
		return self.difficulty

	def get_time(self):
		print "Time left: " + str(int(self.timeleft))
		return int(self.timeleft)

	def start_game(self):
		startTime = int(time.time())
		oldtimeleft = self.timeleft
		while(not self.complete and self.timeleft > 0):
			timeDiff = int(time.time()) - startTime
			self.timeleft = self.time - timeDiff
			if oldtimeleft-self.timeleft >= 1:
				self.get_time()
				oldtimeleft = self.timeleft
				#Also write new time to LCD screen
		if self.timeleft == 0:
			print "BOOM"
		else:
			print "congratulations"

	def get_minigames(self):
		print '[%s]'%', '.join(map(str, self.minigames))
		return self.minigames




if __name__ == '__main__':
	g = GameInstance()
	g.get_minigames()
	g.start_game()