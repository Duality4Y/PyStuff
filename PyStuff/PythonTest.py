import liblo, sys, time
 
# 192.168.100.250 is IP adres tkkrlab server
# 8000 Heinze's protocol default poort
# server restart ssh server sudo su dan: /etc/init.d/tomcat6 restart
try:
	target = liblo.Address("192.168.100.250", 8000)
except liblo.AddressError, err:
	print str(err)
	sys.exit()
 
# aankondigen output ports (vervang python door je eigen naam)
liblo.send(target, "/PyTestRob/out/outputs", "a,b,c,d")
x = 0.0
while True:
	while x < 1.0:
		# zend output waarde
		liblo.send(target, "/PyTestRob/out/a", x)
		time.sleep(0.01)
		x += 0.001
		print x
	while x > 0.0:
		liblo.send(target, "/PyTestRob/out/a", x)
		time.sleep(0.01)
		x -= 0.001
		print x
	
