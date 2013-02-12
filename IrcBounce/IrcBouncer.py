import socket

server = "irc.freenode.net"
channel = "#tkkrlab"
nick = "Daulity"
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def ping():
    #print ircsock.send("PONG :Pong\n")
    ircsock.send("PONG :Pong\n")

def sendmsg(chan, msg):
    ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n")

def joinchan(chan):
    ircsock.send("JOIN "+ chan +"\n")

def connectIrc():
    ircsock.connect((server, 6667))
    ircsock.send("USER "+ nick +" "+ nick +" "+ nick +" :Duality's Diy Irc Bouncer!.\n")
    ircsock.send("NICK "+ nick +"\n")
    identify();
    joinchan(channel)

def identify():
    ircsock.send("PRIVMSG nickserv :identify daulity <@wereld12> \n")

connectIrc()
while True:
    ircmsg = ircsock.recv(2048)
    ircmsg = ircmsg.strip('\n\r')
    ircmsg = str(ircmsg).lower();
    #print(ircmsg)
    
    if ircmsg.find("PING :".lower()) != -1:
        ping();
