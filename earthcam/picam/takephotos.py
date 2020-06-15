from picamera import PiCamera, Color
from time import sleep
from datetime import datetime

from photo_frequency import getfrequency

speedlist=[2,4,8,10,20,30,40,50,60,70,80,90,100]

# init camera
camera = PiCamera()
try:
	camera.resolution = (3280, 2464)
	# less resolution but full sensor 1640x1232
	# full resolution: 3280x2464

	# off auto night nightpreview backlight spotlight sports snow beach verylong fixedfps antishake fireworks
	camera.exposure_mode = 'antishake'

	# off auto sunlight cloudy shade tungsten fluorescent incandescent flash horizon
	camera.awb_mode = 'horizon'

	# init subtitle
	camera.annotate_text_size = 50
	camera.annotate_background = Color('blue')
	camera.annotate_foreground = Color('yellow')

	while(True):
	#	print(num)
		sleeptime = getfrequency()
		print('sleeptime: ' + str(sleeptime))

		now = datetime.now() # current date and time
		date_time = now.strftime("%Y-%m-%d_%H-%M-%S-%f")
		print('date: ' + date_time)
		camera.annotate_text = "EARTHCAM: " + date_time
		for speed in speedlist:
			# setting shutter speed in microseconds
			camera.shutter_speed = speed
			print(speed)
			camera.capture('/home/pi/shots/earthcam_' + date_time + '(' + str(speed)  + ').jpg')
		sleep(sleeptime)
finally:
	camera.close()

#camera.start_preview()
#sleep(5)
#camera.stop_preview()
