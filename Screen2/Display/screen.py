from grove_rgb_lcd import *

class Display:
	def __init__(self):
            setRGB(255,255,255)
#write on top row
        def write_top(self,text):
            setText(text,1)
            return text
#write on bottom row
        def write_bot(self,text):
            setText(text,2)
            return text
#flash for x seconds 
        def flash(self,timer,color):
            while timer>0:
                if (color == "r"):
                    r=255
                    g=0
                    b=0
                elif (color == "g"):
                    r=0
                    g=255
                    b=0
                setRGB(r,g,b)
                time.sleep(0.1)
                setRGB(0,0,0)
                time.sleep(0.1)
                timer -= 0.2

        def set_color(self, color):
            if (color == "r"):
                r=255
                g=0
                b=0
            elif (color == "g"):
                r=0
                g=255
                b=0
            elif (color == "o"):
                r=0
                g=0
                b=0
            setRGB(r,g,b)


if __name__ == '__main__':
	g=Display()
	g.write_top("Hello")
	g.write_bot("World")
        time.sleep(1)
        g.write_top("Refresh")
        g.flash(4,"r")

