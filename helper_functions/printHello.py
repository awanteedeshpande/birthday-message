import helpers as hp
import sys
from pyfiglet import Figlet

def printHelloPerson():
    hp.clr()
    f = Figlet(font='starwars')
    print(*[x.center(hp.terminal_size()) for x in f.renderText("HI!").split("\n")],sep="\n")

def printStartMessage():
    from pyfiglet import Figlet
    f = Figlet(font='big')
    hp.clr()
    msg = "Here  is  a  special  birthday  gift  for  you \n\n^ __ ^"
    print(*[x.center(hp.terminal_size()) for x in f.renderText(msg).split("\n")], sep="\n")
