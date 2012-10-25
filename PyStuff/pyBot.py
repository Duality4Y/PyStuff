import socket
import string
import urllib
import random
import httplib
import pytz
from pytz import timezone
import linecache
from datetime import date, time, datetime
from time import gmtime, strftime

server = "irc.freenode.net"
#channel = raw_input("enter your channel please: ")
channel = "#test1123"
botnick = "DuaBot"
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

quoteSource = "QuoteList.txt"

listOfCommands = ["hello ", "help ", "exit ","time " ,"labstate ","quote ", "quote add ", "quote request ", "quote listlength "]
numCommands = len(listOfCommands)
#print numCommands

def checkForCommands(String):
	if String.rfind(botnick.lower()) != -1:
		if String.rfind(listOfCommands[0]) != -1:
			hello()
		elif String.rfind(listOfCommands[1]) != -1:
			for l in xrange(numCommands):
				if l == 6:
					sendmsg(channel, listOfCommands[l]+"<'Quote'> "+"%s" %botnick)
				elif l == 7:
					sendmsg(channel, listOfCommands[l]+"<Quote number> "+"%s" %botnick)
				else:
					sendmsg(channel, listOfCommands[l]+"%s" %botnick)
		elif String.rfind(listOfCommands[2]) != -1:
			exit()
		elif String.rfind(listOfCommands[3]) != -1:
			sendmsg(channel, strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
		elif String.rfind(listOfCommands[4]) != -1:
			getTkkrlabState()
		elif String.rfind(listOfCommands[5]) != -1:
			QuoteSystem(String)

def QuoteSystem(String):
	numLines = sum(1 for line in open(quoteSource))
	if String.rfind(listOfCommands[6]) != -1 :
		print "input string: ", String
		String = String.split(':')[2]
		print "stripped string at:: ", String
		quote = String[len(listOfCommands[6]):-(len(botnick)+1)]
		print "Quote: ", quote
		print "len quote: ", len(quote)
		if len(quote):
			with open(quoteSource, "a") as f:
				f.write(quote+"\n")
			f.close()
			sendmsg(channel, "thanks, I've added the Quote.")
		else:
			sendmsg(channel, "Invalid input!")
	elif String.rfind(listOfCommands[7]) != -1:
		print "requested stuff lol"
		String = String.split(':')[2]
		print "the input: ", String
		String = String.split(' ')[2]
		print "the Quote number: ", String
		try:
			if int(String) > (numLines) or int(String) < 1:
				sendmsg(channel, "Please check: Quote listlength (e.g. your entered number is to high or low)")
		except ValueError:
			sendmsg(channel, "Invalid Request.")
		else:
			quote = linecache.getline(quoteSource, int(String))
			if quote == "\n":
				sendmsg(channel, "Please check: Quote listlength (e.g. your entered number is to high or low)")
			print "your requested quote is: ", quote
			sendmsg(channel, quote)
	elif String.rfind(listOfCommands[8]) != -1:
		print "list length: ", str(numLines)
		sendmsg(channel, "number of Quotes is: "+ str(numLines))
	else:
		randomLine = (random.randrange(1, numLines+1))
		while True:
			quote = linecache.getline(quoteSource, randomLine)
			if quote != "\n":
				break
		sendmsg(channel, "Quote: "+ quote)
		print "QuoteSystem activated: ", numLines
		print "Random line choosen: ", randomLine
		#print "quote:L%sL",quote
		#textIs = ("Hello Quote, Random lineNumber is: "+ str(randomLine))
		#print textIs
	

def ping():
	print ircsock.send("PONG :Pong\n")
	ircsock.send("PONG :Pong\n")

def sendmsg(chan, msg):
	ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n")

def joinchan(chan):
	ircsock.send("JOIN "+ chan +"\n")

def hello():
	ircsock.send("PRIVMSG "+ channel +" :Hello!\n")

def getTkkrlabState():
	#for conversion timezone
	utc = pytz.utc
	amsterdam = timezone("Europe/Amsterdam")
	conn = httplib.HTTPConnection("www.tkkrlab.nl")
	conn.request("GET", "/state/state")     
	r1 = conn.getresponse()
	conn.close        
	# Time is in GMT convert to CET/Amsterdam
	gmt_dt = utc.localize(datetime.strptime(r1.getheader("Last-Modified"),"%a, %d %b %Y %H:%M:%S %Z")) 
	tkstatus_dt = gmt_dt.astimezone(amsterdam)
	tkstatus = r1.read()
	sendmsg(channel,'We are '+tkstatus+' '+tkstatus_dt.strftime("%a, %d %b %Y %H:%M:%S"))

def connectIrc():
	ircsock.connect((server, 6667))
	ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :This bot is a result of a tutorial covered on http://shellium.org/wiki.\n")
	ircsock.send("NICK "+ botnick +"\n")
	joinchan(channel)

connectIrc()

while True:
	ircmsg = ircsock.recv(2048)
	ircmsg = ircmsg.strip('\n\r')
	ircmsg = str(ircmsg).lower()
	print(ircmsg)
	if ircmsg.find("PING :".lower()) != -1:
		ping()
	if checkForCommands(ircmsg) == False:
		break
#My try at a irc Bot
