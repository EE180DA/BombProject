import time
from random import shuffle

class GameInstance:

	def __init__(self, diff = -1):
		while diff < 1 or diff > 3:
			diff = raw_input("Please choose a difficulty level (1-3): ")
			diff = int(diff)
		self.difficulty = diff
		self.time = 50*self.difficulty #time left in seconds
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

	def print_timeleft(self, startTime, oldtimeleft):
		timeDiff = int(time.time()) - startTime
		self.timeleft = self.time - timeDiff
		if oldtimeleft-self.timeleft >= 1:
			self.get_time()
			return self.timeleft
		return oldtimeleft
			#Also write new time to LCD screen

	def start_game(self):
		startTime = int(time.time())
		oldtimeleft = self.timeleft
		currGame = 1
		while(not self.complete and self.timeleft > 0):
			oldtimeleft = self.print_timeleft(startTime, oldtimeleft)
				#Also write new time to LCD screen

			print "Time to play: " + self.minigames[0]
			while(self.timeleft > 0):
				oldtimeleft = self.print_timeleft(startTime, oldtimeleft)
				if(self.timeleft < self.time-5):
					break

			print "Time to play: " + self.minigames[1]
			while(self.timeleft > 0):
				oldtimeleft = self.print_timeleft(startTime, oldtimeleft)
				if(self.timeleft < self.time-10):
					break

			print "Time to play: " + self.minigames[2]
			while(self.timeleft > 0):
				oldtimeleft = self.print_timeleft(startTime, oldtimeleft)
				if(self.timeleft < self.time-15):
					break

			print "Time to play: " + self.minigames[3]
			while(self.timeleft > 0):
				oldtimeleft = self.print_timeleft(startTime, oldtimeleft)
				if(self.timeleft < self.time-20):
					break

			print "Time to play: " + self.minigames[4]
			while(self.timeleft > 0):
				oldtimeleft = self.print_timeleft(startTime, oldtimeleft)
				if(self.timeleft < self.time-25):
					break
			self.complete = True


		if self.timeleft == 0:
			print "BOOM"
		else:
			print "Congratulations you've defused the bomb"

	def get_minigames(self):
		print '[%s]'%', '.join(map(str, self.minigames))
		return self.minigames




if __name__ == '__main__':
	g = GameInstance()
	g.get_minigames()
	g.start_game()