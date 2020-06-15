#!/usr/bin/python3
import datetime
import configparser

conf = configparser.ConfigParser()
conf.read('/home/pi/photo_frequency_conf.ini')

now = datetime.datetime.now()
def getfrequency():
	"Returns frequency of photos based on time and conf"
	if (conf.getint('Start', 'mintime') <= now.minute and conf.getint('Start', 'hourtime') <= now.hour and conf.getint('Start', 'daytime') <= now.day and conf.getint('Start', 'mintime') + conf.getint('Start', 'minduration') >= now.minute and conf.getint('Start', 'hourtime') + conf.getint('Start', 'hourduration') >= now.hour and conf.getint('Start', 'daytime') + conf.getint('Start', 'dayduration') >= now.day):
		return conf.getint('Start', 'frequency')
	elif (conf.getint('Stop', 'mintime') <= now.minute and conf.getint('Stop', 'hourtime') <= now.hour and conf.getint('Stop', 'daytime') <= now.day):
		return conf.getint('Start', 'frequency')
	elif (conf.getint('Night', 'mintime') <= now.minute and conf.getint('Night', 'hourtime') <= now.hour and conf.getint('Night', 'mintime') + conf.getint('Night', 'minduration') >= now.minute and conf.getint('Night', 'hourtime') + conf.getint('Night', 'hourduration') >= now.hour):
		return conf.getint('Night', 'frequency')
	else:
		return conf.getint('Normal', 'frequency')
