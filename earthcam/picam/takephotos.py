from picamera import PiCamera
#from time import sleep
from datetime import datetime

# init camera
camera = PiCamera()
camera.resolution = (2592, 1944)

# off auto night nightpreview backlight spotlight sports snow beach verylong fixedfps antishake fireworks
camera.exposure_mode = 'antishake'

# off auto sunlight cloudy shade tungsten fluorescent incandescent flash horizon
camera.awb_mode = 'horizon'

# init subtitle
camera.annotate_text_size = 50
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')

for num in range(1,10):
	now = datetime.now() # current date and time
	date_time = now.strftime("%Y-%m-%d_%H:%M:%S:%f")
	camera.annotate_text = "EARTHCAM: " + date_time
	camera.capture('/home/pi/shots/earthcam_' + date_time  + '.jpg')
	camera.stop_preview()

#camera.start_preview()
#sleep(5)
#camera.stop_preview()
