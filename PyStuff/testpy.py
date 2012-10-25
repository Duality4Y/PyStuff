i=0
tocheck = [2,3,5,7]

for i in xrange(100):
	for l in tocheck:
		if i%l:
			print i

