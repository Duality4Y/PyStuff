import socket
import sys
import serial

server = "Server-Duality";
channel = "Duality";
nick = "serialbot";
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
#ser = serial.Serial(str(raw_input("Enter device location: ")), int(raw_input("and baud: ")));


def pin():
	ircsock.send("PONG :Pong\n");

def sendmsg(chan, msg):
	ircsock.send("PRIVMS "+chan+" :"+msg+"\n");

def joinchan(chan):
	ircsock.send("JOIN "+chan+"\n");

def connectIrc():
	ircsock.connect((server, 6667));
	ircsock.send("USER "+nick+" "+nick+" "+nick+" :irc Serial By Duality.\n");
	ircsock.send("NICK "+nick+"\n");
	joinchan(channel);
	
def irc():
	ircmsg = ircsock.recv(2048);
	ircmsg = ircmsg.strip('\n\r');
	ircmsg = str(ircmsg).lower();
	if(ircmsg.find("ping :") != -1):
		ping();
	print(ircmsg);
	#sendmsg(channel, ser.readline());
	
def main():
	connectIrc();
	while(True):
		irc();
		
main();
