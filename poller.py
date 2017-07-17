import json
import urllib2

def poll_goniyo():
	import time
	while 1:
		data = json.load(urllib2.urlopen('https://api.goniyo.com/health'))
		if data["status"] == "UP":
			print(True)
		else:
			print(False)
		time.sleep(5)

poll_goniyo()