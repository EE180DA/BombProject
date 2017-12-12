import time

# Import the LSM9DS0 module
import IMU

class Response(object):
	def __init__(self): 
		self.g_threshold = 3000
		self.idle1 = 0
		self.idle2 = 0
		self.idle3 = 0
		self.idle4 = 0
		self.lcount = 0
		self.rcount = 0
		self.bcount = 0
		self.fcount = 0
		self.nodcount = 4
		self.shakecount = 4
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
		    if gyro_x > self.g_threshold:
		        print('Forward')
		        if self.idle1 < 20:
		            self.fcount+=1
		            self.idle1=0
		        else:
		            self.fcount=0
		            self.idle1=0
		    elif gyro_x<-self.g_threshold:
		        print('Back')
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
		        print('Nod Complete')
		        self.fcount=0
		        self.bcount=0
		        self.idle1=0
		        self.idle2=0
		        time.sleep(1)
		        return 1
		    if gyro_z > self.g_threshold:
		        print('Right')
		        if self.idle3 < 20:
		            self.rcount+=1
		            self.idle3=0
		        else:
		            self.rcount=0
		            self.idle3=0
		    elif gyro_z<-self.g_threshold:
		        print('Left')
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
		        print('Shake Complete')
		        self.rcount=0
		        self.lcount=0
		        self.idle3=0
		        self.idle4=0
		        time.sleep(1)
		        return 2
		    time.sleep(0.1)

if __name__ == '__main__':
	r=Response()
	r.get()