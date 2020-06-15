from picamera import PiCamera, Color
from time import sleep
from datetime import datetime

from photo_frequency import getfrequency


# init camera
camera = PiCamera()
camera.resolution = (800, 600)

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
	print(getfrequency())

	now = datetime.now() # current date and time
	date_time = now.strftime("%Y-%m-%d_%H-%M-%S-%f")
	camera.annotate_text = "EARTHCAM: " + date_time
	camera.capture('/home/pi/shots/earthcam_' + date_time  + '.jpg')
	sleep(getfrequency())

#camera.start_preview()
#sleep(5)
#camera.stop_preview()
