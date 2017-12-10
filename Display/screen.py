from grove_rgb_lcd import *

class Display:
	def __init__(self):
		setRGB(255,255,255)
#write on top row
        def writeTop(self,text):
		setText(text,1)
#write on bottom row
        def writeBot(self,text):
		setText(text,2)
#flash for x seconds 
        def flash(self,timer):
            while timer>0:
                setRGB(255,0,0)
                time.sleep(0.1)
                setRGB(255,255,255)
                time.sleep(0.1)
                timer -= 0.2


if __name__ == '__main__':
	g=Display()
	g.writeTop("Hello")
	g.writeBot("World")
        time.sleep(1)
        g.writeTop("Refresh")
        g.flash(3)

