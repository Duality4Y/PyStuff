#!/usr/bin/env python
import time
import thread
import sys

def myfunction(sleeptime,lock,*args):
	while 1:
		lock.acquire()
		time.sleep(sleeptime) 
		print "Hello"
		lock.release()
		time.sleep(sleeptime)

def myfunction2(sleeptime,lock,*args):
	while 1:
		lock.acquire()
		time.sleep(sleeptime)
		for line in sys.stdin.readline():
			if "\n" in line:
				print line
			else: pass
		lock.release()
		time.sleep(sleeptime)

if __name__=="__main__":
	lock=thread.allocate_lock()
	thread.start_new_thread(myfunction,(1,lock))
	#thread.start_new_thread(myfunction2,(1,lock))
	while 1:
		for line in sys.stdin.readline():
			if "\n" in line:
				print line
			else: pass