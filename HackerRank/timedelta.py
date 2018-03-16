#displays the abs difference between two timestamps in seconds.
#the stamps are in the format: 'Sun 10 May 2015 13:54:36 +0700'
#here, '+0700' is the timezone.

import datetime
for i in range(int(input())):
	start=datetime.datetime.strptime(input(),'%a %d %b %Y %X %z')
	end=datetime.datetime.strptime(input(),'%a %d %b %Y %X %z')
	print (abs(int((start-end).total_seconds())))