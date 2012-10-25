from time import gmtime, strftime, time
currentTime = 0
previousTime = 0
interval = 10

while True:
	currentTime=time()
	if currentTime - previousTime > interval:
		previousTime = currentTime
		print "Hello!"
	 	print strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
