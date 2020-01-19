import requests
from bs4 import BeautifulSoup
from bs4 import NavigableString
from bs4 import Tag
import random
import time
startTime = time.time()
def post():
	url = 'http://bible.blessing.ru/index.php?m=r'
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')
	for br in soup.findAll('br'):
		next_s = br.nextSibling
		if not (next_s and isinstance(next_s,NavigableString)):
			continue
		next2_s = next_s.nextSibling
		if next2_s and isinstance(next2_s,Tag) and next2_s.name == 'br':
			text = str(next_s).strip()
			if text:
				return next_s
token = '' #insert your token here
owner_id_group = -119402294 #insert group to post here
number = 0
days = 0
hours = 0
minutes = 0
uptime = time.time() - startTime
clock = time.ctime(time.time())
def uptime_convert(seconds):
	global days
	global hours
	global minutes
	cnv = seconds // 60
	minutes += cnv
	if minutes == 60 or minutes > 60:
		minutes -= 60
		hours += 1
	if hours == 24 or hours > 24:
		hours -= 24
		days += 1
	return 'Minutes: %s, Hours: %s, Days: %s' % (minutes, hours, days)
def posting():
	while True:
		requests.post('https://api.vk.com/method/wall.post', data={'access_token': token,
                                                                    'owner_id': owner_id_group,
                                                                    'from_group': 1,
                                                                    'message': post(),
                                                                    'signed': 0,
                                                                    'v':"5.52"}.json())
		number += 1                                 
		global uptime
		print('%s: Posted post number %s sucessfully, uptime: %s' % (clock, number, uptime_convert(uptime)))
		time.sleep(1800)
		if number > 1 or number == 1:
			uptime += 1800

try:
	posting()
except:
	print('%s: Something went wrong. Script gonna try restart itself. If it keeps spamming errors, restart it manually.' % clock)
	posting()