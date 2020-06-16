import requests
import os
import configparser

Config = configparser.ConfigParser()
Config.read('/home/pi/picam_config.ini')

#print(Config.sections())
url = Config.get('Upload', 'url')

directory = '/home/pi/shots/'

for filename in os.listdir(directory): 
	if filename.endswith('.jpg'):
		print('upload: ' + directory + filename ) 
		headers = {'Content-Type' : 'image/jpeg'}
		file = open(directory + filename, 'rb')
		fileses = {'image': (filename, file)} 
		try:
			r = requests.post(url, files=fileses)
			print(r.text)
		finally:
			file.close()
		#response = requests.post(url, files = files, headers = headers, verify=True)
		#print(response.text)
