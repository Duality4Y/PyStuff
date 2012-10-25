from sys import argv
script, input, numycolums = argv
#input = raw_input("How many times? >>")
for l in xrange(1,int(input)):
	pronic = l*(l+1)
	print  pronic, '\t',
	if l%int(numycolums) == 0:
		print '\n'
print '\n'
