#!/usr/bin/python
## IRC TKKRLAB BOT
## Date : 30-4-2011
## Dave Borghuis
## V1.2
## 23-04-2011 Dave Added help function
## 03-05-2011 Dave Added redirect to sterr to file (to catch errors)
## 16-06-2011 Dave Added guard for disconnect, 
##                 !led command to update matrix
##                  fix private messages to tkkrlabbot
## 13-12-2011 Dave Added Random quote function

import socket
from time import sleep
import httplib
import sys
import time
from datetime import date, time, datetime
from pytz import timezone
import pytz
import random

## for debug
#fsock = open('/root/irc_error.log','w')
#sys.stderr = fsock
#sys.stdout = fsock

#for conversion timezone
utc = pytz.utc
amsterdam = timezone("Europe/Amsterdam")

## IRC Details, change these
#irc_network = 'lindbohm.freenode.net'
#irc_network = 'kornbluth.freenode.net'
irc_network = 'irc.freenode.net'
bot_owner = 'Daulity'
nick_name = 'zenBot'
irc_channel = '#test1231'
irc_port = 6667

#
tkoldstatus = ''
tkstatus_dt = 0
tkstatus = ''

def randomquote():
	loctext = open("quotes.txt").readlines()
	return random.choice(loctext)	

def ircconnect():
	#print 'irc connect'
	#print datetime.now()
	global irc
	irc = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
	irc.setblocking(1)
	irc.settimeout(500)
	irc.connect( ( irc_network, irc_port ) )
	irc.send( 'NICK '+nick_name+'\r\n' )
	irc.send( 'USER Tkkrlab Tkkrlab Tkkrlab :TkkrLab\r\n' )
	#irc.send( 'PRIVMSG :MSG NickServ IDENTIFY tkkrlab1337\r\n' )
	irc.send( 'JOIN ' + irc_channel +'\r\n' )
	#print "tkkrlab bot started... "

def status ():
	# Get status/date from file
        conn = httplib.HTTPConnection("www.tkkrlab.nl")
        conn.request("GET", "/state/state")     
        r1 = conn.getresponse()
        conn.close        
        # Time is in GMT convert to CET/Amsterdam
        gmt_dt = utc.localize(datetime.strptime(r1.getheader("Last-Modified"),"%a, %d %b %Y %H:%M:%S %Z")) 
        tkstatus_dt = gmt_dt.astimezone(amsterdam)
        tkstatus = r1.read()
        return 'We are '+tkstatus+' '+tkstatus_dt.strftime("%a, %d %b %Y %H:%M:%S")

def sendled(led_message):
        #print led_message
        #conn = httplib.HTTPConnection("[2001:610:600:6db::2]")
        conn = httplib.HTTPConnection("192.168.100.250")
        conn.request("GET", "/~manson/led/txt.php?text="+led_message)
        conn.close        

def getircstring():
        data = ''
        try:
            data = irc.recv(4096)
            return data
        except socket.timeout:
            ircconnect()
            return data

#print randomquote()
#exit

ircconnect()
while True:
        data = getircstring()
        print data            		
        if data.find ( 'PING' ) != -1:
                irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
        elif data.find ( 'PRIVMSG' ) != -1:
                nick = data.split ( '!' ) [ 0 ].replace ( ':', '' )
                message = ':'.join ( data.split ( ':' ) [ 2: ] )
                #destination = ''.join ( data.split ( ':' ) [ :2 ] ).split ( ' ' ) [ -2 ] //works only with ipv4
                destination = ''.join(data[data.rfind(':')+1:])
                if destination == nick_name:
                       destination = 'PRIVATE'
                # voorbeelden voor data variabele:
                # :hansw!~hans@p4FCAA757.dip.t-dialin.net PRIVMSG #tkkrlab :hmm, dat kan best leuk zijn
                # :zeno4ever!~zeno4ever@2001:980:49b2:1:21b:63ff:fe92:f5cc PRIVMSG #tkkrlab2 :!status
                if message.find( '!status' ) != -1:     
                        tkstatus = status()     
                        irc.send ( 'PRIVMSG '+irc_channel +' :' + tkstatus +'\r\n' )
                        #irc.send ( 'PRIVMSG '+irc_channel +' :' + tkstatus +'\r\n' )
                if message.find( '!led' ) != -1:
                        ledmessage = message[message.index('!led')+4:]
                        sendled(ledmessage)  
                        irc.send ( 'PRIVMSG '+irc_channel +' : Led updated with:'+ledmessage)
		if message.find( '!quote' ) != -1:
			quotetext = randomquote()
			irc.send( 'PRIVMSG '+irc_channel + ' : Quote: '+quotetext)           
                if message.find( '!tkkrhelp' ) != -1:
			irc.send ( 'PRIVMSG '+irc_channel +' :!quote: to get a random quote\r\n' )
                        irc.send ( 'PRIVMSG '+irc_channel +' :!status: to get open/close status of tkkrlab space\r\n' )
                        irc.send ( 'PRIVMSG '+irc_channel +' :!led messge: put message on led matrix board\r\n' )                        
                        irc.send ( 'PRIVMSG '+irc_channel +' :!tkkrhelp: this message\r\n' )
                        irc.send ( 'PRIVMSG '+irc_channel +' :See also my friends Lock-O-Matic and arcade 1943 (if he is around)\r\n' )
