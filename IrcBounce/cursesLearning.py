import curses

def endCurses():
	curses.nocbreak();
	curses.keypad(0);
	curses.echo();
	curses.endwin();
#put program in to main, wrapped a try except around it so when you do a
#keyboard interupt you can safely close curses with the endCurses() function.
def main():
	print "Teehee Test1234567890a;sdlkjfasdfkja;sdfja;sdfkja;sdlfkjas;dlfkja;sldkfja;lsdkfj;alsdkjfa;sldfkj;asldkfj;a;sdlkjfa;lsdkjfa;lsdkf";

try:
	while(True):
		main();
except:
	endCurses();
	print "Hello!";
