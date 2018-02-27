import time

# Import the LSM9DS0 module
import IMU

class Response(object):
	def __init__(self): 
		self.g_threshold = 1900
		self.idle1 = 0
		self.idle2 = 0
		self.idle3 = 0
		self.idle4 = 0
		self.idle5 = 0
		self.idle6 = 0
		self.tiltidle = 0
		self.lcount = 0
		self.rcount = 0
		self.bcount = 0
		self.fcount = 0
		self.ucount = 0
		self.dcount = 0
		self.nodcount = 2
		self.shakecount = 2
		self.hintcount = 2
		self.imu = IMU.IMU()
	def get(self):
		while True:
		    # Grab (x, y, z) readings for gyro, mag and accelerometer
		    gyro, mag, accel = self.imu.read()
		    # Unpack tuples
		    gyro_x, gyro_y, gyro_z = gyro
		    mag_x, mag_y, mag_z = mag
		    accel_x, accel_y, accel_z = accel
		    # Check for nod and shake
		    if gyro_y > self.g_threshold:
		    	# print('Tilt detected')
		    	self.tiltidle+=1
		    	if self.tiltidle > 3:
		    		self.tiltidle=0
		    elif gyro_y < -self.g_threshold: 
		    	# print('Tilt detected')
		    	self.tiltidle+=1
		    	if self.tiltidle > 3:
		    		self.tiltidle=0
		    if gyro_x > self.g_threshold:
		        # print('Forward')
		        self.tiltidle=0
		        if self.idle1 < 20:
		            self.fcount+=1
		            self.idle1=0
		        else:
		            self.fcount=0
		            self.idle1=0
		    elif gyro_x<-self.g_threshold:
		        # print('Back')
		        self.tiltidle=0
		        if self.idle2<20:
		            self.bcount+=1
		            self.idle2=0
		        else:
		            self.bcount=0
		            self.idle2=0
		    else:
		        self.idle1+=1
		        self.idle2+=1
		        
		    if self.bcount>self.nodcount and self.fcount>self.nodcount:
		        # When a nod is detected, return 1
		        #print('Nod Complete')
		        self.fcount=0
		        self.bcount=0
		        self.idle1=0
		        self.idle2=0
		        return 1
		    if gyro_z > self.g_threshold:
		        #print('Right')
		        if self.idle3 < 20:
		            self.rcount+=1
		            self.idle3=0
		        else:
		            self.rcount=0
		            self.idle3=0
		    elif gyro_z<-self.g_threshold:
		        #print('Left')
		        if self.idle4<20:
		            self.lcount+=1
		            self.idle4=0
		        else:
		            self.lcount=0
		            self.idle4=0
		    else:
		        self.idle3+=1
		        self.idle4+=1
		    if self.lcount>self.shakecount and self.rcount>self.shakecount:
		        # When a shake is detected, return 2
		        #print('Shake Complete')
		        self.rcount=0
		        self.lcount=0
		        self.idle3=0
		        self.idle4=0
		        return 2
		    if accel_z > 800:
		        #print('Up')
		        self.tiltidle=0
		        if self.idle5 < 20:
		            self.ucount+=1
		            self.idle5=0
		        else:
		            self.ucount=0
		            self.idle5=0
		    elif accel_z<-2800:
		        #print('Down')
		        self.tiltidle=0
		        if self.idle6<20:
		            self.dcount+=1
		            self.idle6=0
		        else:
		            self.dcount=0
		            self.idle6=0
		    else:
		        self.idle5+=1
		        self.idle6+=1
		        if self.tiltidle>0:
		        	self.tiltidle+=1
		        if self.tiltidle>20:
		        	#print('Tilted')
		        	self.tiltidle=0
		        	return 3
		    if self.ucount>self.shakecount and self.dcount>self.shakecount:
		        # When a hint is detected, return 3
		        #print('Hint Complete')
		        self.ucount=0
		        self.dcount=0
		        self.idle5=0
		        self.idle6=0
		        return 4
		    time.sleep(0.05)

if __name__ == '__main__':
	r=Response()
	while True:
		print('Do a nod')
		response=r.get()
		if response==1:
			print('Nod Detected. Good job!')
			time.sleep(1)
			break
		else: 
			print('Please try again. Make sure to nod up and down more than 3 times')
			time.sleep(1)
	while True:
		print('Do a shake')
		response=r.get()
		if response==2:
			print('Shake detected. Good job!')
			time.sleep(1)
			break
		else: 
			print('Please try again. Make sure to shake left and right more than 3 times')
			time.sleep(1)
	while True:
		print('Do a tilt')
		response=r.get()
		if response==3:
			print('Tilt detected. Good job!')
			time.sleep(1)
			break
		else:
			print('Please try again. Try tilting it faster, then holding it for 2 seconds')
			time.sleep(1)=
	print('Calibration complete.')
