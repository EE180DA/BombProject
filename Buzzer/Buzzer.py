import time
from upm import pyupm_buzzer as upmBuzzer

def main():
    # Create the buzzer object using GPIO pin 5
    class Buzzer():
        def __init__ (self):
        pass


    buzzer = upmBuzzer.Buzzer(5)

    chords = [1000];

    # Print sensor name
    print(buzzer.name())

    # Play sound (DO, RE, MI, etc.), pausing for 0.1 seconds between notes
    for chord_ind in range (0,7):
        # play each note for a half second
        print(buzzer.playSound(chords[chord_ind], 500000))
        time.sleep(0.1)

    print("exiting application")

    # Delete the buzzer object
    del buzzer

if __name__ == '__main__':
    main()