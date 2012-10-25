import sys
import socket
import string
import select
import tty
import termios

Input = ""
server = "irc.freenode.net"
channel = "#test1123"
nick = "TestClient"
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

old_settings = termios.tcgetattr(sys.stdin)

def isData():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def ping():
	ircsock.send("PONG :Pong\n")

def sendmsg(chan, msg):
	ircsock.send("PRIVMSG "+chan+" :"+msg+"\n")

def joinchan(chan):
	ircsock.send("JOIN "+chan+"\n")

def quit(temp):
	try:
		msg=temp.split(" ",1)[1]
	except IndexError:
		msg = ""
	ircsock.send("QUIT :"+msg+"\r\n")
	exit()

def connectIrc():
	ircsock.connect((server, 6667))
	ircsock.send("USER "+nick+" "+nick+" "+nick+" :PyIrc By Duality.\n")
	ircsock.send("NICK "+nick+"\n")
	joinchan(channel)

def clientInput():
	try:
		#tty.setcbreak(sys.stdin.fileno())
		c = sys.stdin.read(1)
		print c
		return c
	finally:
		termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

def irc():
	ircmsg = ircsock.recv(2048)
	ircmsg = ircmsg.strip('\n\r')
	ircmsg = str(ircmsg).lower()
	
	if ircmsg.find("ping :") != -1:
		ping()
	print(ircmsg)

connectIrc()

while True:
	irc()
	Input = clientInput()
	print Input
	#if Input:
	#	sendmsg(channel, str(Input))
	#	print Input
	#	Input = ""
