import time
from upm import pyupm_buzzer as upmBuzzer



class Buzzer():
    def __init__ (self, pin_number):
        buzzer = upmBuzzer.Buzzer(pin_number)

    buzzer = upmBuzzer.Buzzer(5)
    sounds = {"right" : [1000, 250, 500], "wrong" : [5000, 6000], "win" : [500, 4000, 3000, 300], "lose" : [300], "beep" : [3000]}  
    durations = {"right" : [50000, 50000, 50000], "wrong" : [10000, 500000], "win" : [200000, 50000, 30000, 100000], "lose" : [2000000], "beep" : [50000]}
    delay = {"right" : 0.01, "wrong" : 0.1, "win" : 0.01, "lose" : 0.1, "beep" : 0}

    def play(self, name):
        if name in self.sounds:
            sound = self.sounds[name]
            duration = self.durations[name]
            for i in range (0, len(sound)):
                self.buzzer.playSound(sound[i], duration[i])
                time.sleep(self.delay[name])


    # Play sound (DO, RE, MI, etc.), pausing for 0.1 seconds between notes

if __name__ == '__main__':
    buzzer = Buzzer(5)
    buzzer.play("right")
    time.sleep(2)
    buzzer.play("wrong")
    time.sleep(2)
    buzzer.play("win")
    time.sleep(2)
    buzzer.play("lose")
