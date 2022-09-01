import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys

print ("WARP-PLUS-CLOUDFLARE By ALIILAPRO")

startTime = time.time()
referrer = os.getenv('DEVICE_ID')
def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)		    
def digitString(stringLength):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for i in range(stringLength)))    
	except Exception as error:
		print(error)	
url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
def run():
	try:
		install_id = genString(22)
		body = {"key": "{}=".format(genString(43)),
				"install_id": install_id,
				"fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
				"referrer": referrer,
				"warp_enabled": False,
				"tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
				"type": "Android",
				"locale": "es_ES"}
		data = json.dumps(body).encode('utf8')
		headers = {'Content-Type': 'application/json; charset=UTF-8',
					'Host': 'api.cloudflareclient.com',
					'Connection': 'Keep-Alive',
					'Accept-Encoding': 'gzip',
					'User-Agent': 'okhttp/3.12.1'
					}
		req         = urllib.request.Request(url, data, headers)
		response    = urllib.request.urlopen(req)
		status_code = response.getcode()	
		return status_code
	except Exception as error:
		if error.getcode() != 429:
			print(error)
			sys.exit(0)

ts = 23
suc = 0
bad = 0
while True:
	if time.time() - startTime >= 14400:
		print(f"总计获取{suc}GB流量，失败{bad}次")
		break
	result = run()
	if result == 200:
		suc = suc +1
		if ts > 23: ts = ts - 1
		time.sleep(ts)
	else:
		bad = bad + 1
		ts = ts + 1
		time.sleep(ts)
