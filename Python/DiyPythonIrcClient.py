import time
import thread
import sys

import socket
import string

userinput = ''

server = "irc.freenode.net"
channel = "#tkkrlab"
#nick =raw_input("Enter Nick: ")
nick = "Duality-pyIrc"
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def ping():
	ircsock.send("PONG :Pong\n")

def sendmsg(chan, msg):
	ircsock.send("PRIVMSG "+chan+" :"+msg+"\n")

def joinchan(chan):
	ircsock.send("JOIN "+chan+"\n")

def quit(temp):
	try:
		msg = temp.split(" ",1)[1]
	except IndexError:
		msg = ""
	#msg = temp.split(' ')
	#del msg[0]
	#msg = " ".join(msg)
	ircsock.send("QUIT :"+msg+"\r\n")
	exit()

def connectIrc():
	ircsock.connect((server, 6667))
	ircsock.send("USER "+nick+" "+nick+" "+nick+" :PyIrc By Duality.\n")
	ircsock.send("NICK "+nick+"\n")
	joinchan(channel)

def clientInput():
	userinput_ = sys.stdin.readline()
	if "\n" in userinput_:
		#print userinput
		userinput = userinput_.strip('\n\r')
		return userinput
	else: pass

#def clientInput():
#	for line in sys.stdin.readline():
#		if "\n" in line:
#			print "Line: ",line
#		else: pass

def irc():
	ircmsg = ircsock.recv(2048)
	ircmsg = ircmsg.strip('\n\r')
	ircmsg = str(ircmsg).lower()
	
	if ircmsg.find("ping :") != -1:
		ping()
	print(ircmsg)

def ircServerSide(sleeptime,lock,*args):
	while 1:
		lock.acquire()
		time.sleep(sleeptime)
		irc()
		lock.release()
		time.sleep(sleeptime)

if __name__=="__main__":
	connectIrc()
	lock=thread.allocate_lock()
	Time = 0.01
	thread.start_new_thread(ircServerSide,(Time,lock))
	while 1:
		userinput = clientInput()
		if userinput.rfind("/quit") != -1:
			quit(userinput)
		sendmsg(channel, userinput)
