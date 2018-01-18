<<<<<<< HEAD:VoiceRecog/speech.py
import collections
import mraa
import os
import sys
import time

# Import things for pocketsphinx
import pyaudio
import wave
import pocketsphinx as ps
import sphinxbase

class SpeechRecognition:
    # Parameters for pocketsphinx
    def __init__(self):
        self.LMD   = "/home/root/led-speech-edison/lm/3867.lm"
        self.DICTD = "/home/root/led-speech-edison/lm/3867.dic"
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 16000
        self.RECORD_SECONDS = 2
        self.PATH = 'output'
        self.items = ['APPLE', 'BANANA', 'ORANGE', 'GRAPEFRUIT']
        self.answer = ""
        


    def triggerWords(self, words, game_code):
        self.answer = self.items[game_code]
        print(self.answer)
        #Grapefruit is unlikely to be randomly triggered by noise
        #Difficult to detect 'keyword grapefruit' all together
        #Thus, 'Keyword' does not need to be said if the answer is grapefruit
        if self.answer == "GRAPEFRUIT":
            if "GRAPEFRUIT" in words:
                print("Correct Keyword Detected")
                return(1)
        #Detect keyword and then answer to complete round
        if "KEYWORD" in words:
            if self.answer in words:
                print("Correct Keyword Detected")
                return(1)
          
    def decodeSpeech(self, speech_rec, wav_file):
	wav_file = file(wav_file,'rb')
	wav_file.seek(44)
	speech_rec.decode_raw(wav_file)
	result = speech_rec.get_hyp()
	return result[0]

   # def blockprint(self):
    #    sys.stderr = open(os.devnull, 'w')

    def startrecording(self, game_code):
       
        if not os.path.exists(self.PATH):
            os.makedirs(self.PATH)

        p = pyaudio.PyAudio()
        speech_rec = ps.Decoder(lm=self.LMD, dict=self.DICTD)

        while True:
            # Record audio
            stream = p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
            print("* recording")
            frames = []
            for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
                    data = stream.read(self.CHUNK)
                    frames.append(data)
            print("* done recording")
            stream.stop_stream()
            stream.close()
            #p.terminate()

            # Write .wav file
            fn = "o.wav"
            wf = wave.open(os.path.join(self.PATH, fn), 'wb')
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(p.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(frames))
            wf.close()

            # Decode speech
            wav_file = os.path.join(self.PATH, fn)
            recognised = self.decodeSpeech(speech_rec, wav_file)
            rec_words = recognised.split()

            # Trigger Words
            result = self.triggerWords(rec_words, game_code)
            #Check if the correct answer was said
            if result == 1:
                return(1)

            # Playback recognized word(s)
            cm = 'espeak "'+recognised+'"'
            os.system(cm)

if __name__ == "__main__":
    g = SpeechRecognition()
    try:
        output = g.startrecording(1)
        if output == 1:
            print("Round passed")
        else:
            print("Round failed")
    except KeyboardInterrupt:
        print "Keyboard interrupt received. Cleaning up..."
        
=======
import collections
import mraa
import os
import sys
import time

# Import things for pocketsphinx
import pyaudio
import wave
import pocketsphinx as ps
import sphinxbase

class SpeechRecognition:
    # Parameters for pocketsphinx
    def __init__(self):
        self.LMD   = "/home/root/BombProject/VoiceRecog/speech/speech/lm/3867.lm"
        self.DICTD = "/home/root/BombProject/VoiceRecog/speech/speech/lm/3867.dic"
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 16000
        self.RECORD_SECONDS = 2
        self.PATH = 'output'
        self.items = ['APPLE', 'BANANA', 'ORANGE', 'GRAPEFRUIT']
        self.answer = ""
        


    def triggerWords(self, words, game_code):
        self.answer = self.items[game_code]
        print(self.answer)
        #Grapefruit is unlikely to be randomly triggered by noise
        #Difficult to detect 'keyword grapefruit' all together
        #Thus, 'Keyword' does not need to be said if the answer is grapefruit
        if self.answer == "GRAPEFRUIT":
            if "GRAPEFRUIT" in words:
                print("Correct Keyword Detected")
                return(1)
        #Detect keyword and then answer to complete round
        if "KEYWORD" in words:
            if self.answer in words:
                print("Correct Keyword Detected")
                return(1)
          
    def decodeSpeech(self, speech_rec, wav_file):
	wav_file = file(wav_file,'rb')
	wav_file.seek(44)
	speech_rec.decode_raw(wav_file)
	result = speech_rec.get_hyp()
	return result[0]

   # def blockprint(self):
    #    sys.stderr = open(os.devnull, 'w')

    def startrecording(self, game_code):
       
        if not os.path.exists(self.PATH):
            os.makedirs(self.PATH)

        p = pyaudio.PyAudio()
        speech_rec = ps.Decoder(lm=self.LMD, dict=self.DICTD)

        while True:
            # Record audio
            stream = p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
            print("* recording")
            frames = []
            for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
                    data = stream.read(self.CHUNK)
                    frames.append(data)
            print("* done recording")
            stream.stop_stream()
            stream.close()
            #p.terminate()

            # Write .wav file
            fn = "o.wav"
            wf = wave.open(os.path.join(self.PATH, fn), 'wb')
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(p.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(frames))
            wf.close()

            # Decode speech
            wav_file = os.path.join(self.PATH, fn)
            recognised = self.decodeSpeech(speech_rec, wav_file)
            rec_words = recognised.split()

            # Trigger Words
            result = self.triggerWords(rec_words, game_code)
            #Check if the correct answer was said
            if result == 1:
                return(1)

            # Playback recognized word(s)
            cm = 'espeak "'+recognised+'"'
            os.system(cm)

if __name__ == "__main__":
    g = SpeechRecognition()
    try:
        output = g.startrecording(1)
        if output == 1:
            print("Round passed")
        else:
            print("Round failed")
    except KeyboardInterrupt:
        print "Keyboard interrupt received. Cleaning up..."
        
>>>>>>> f03d66580898aa50ce8bebd32c7097066ad0429a:VoiceRecog/speech/speech/speech.py
