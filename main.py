#https://stackoverflow.com/questions/60946171/python-how-to-offer-a-single-executable-file-without-showing-the-code-in-2020
#https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df
import sys
import time
import os

if os.name == 'nt':
    sys.path.insert(1, '.\helper_functions')
else:
    sys.path.insert(1, './helper_functions')

import helpers as hp

time.sleep(1)
print("Let's check if you have everything you need for this to work...")
time.sleep(1.5)
print("It might take a few seconds...")
if 'pyfiglet' not in sys.modules:
        hp.install('pyfiglet')
if 'pillow' not in sys.modules:
        hp.install('Pillow')
if 'termcolor' not in sys.modules:
        hp.install('termcolor')
print("Okay, let's begin!")
time.sleep(2)
hp.clr()

import printASCII as ascii
import printHello as ph
import runClues as rc

ph.printHelloPerson()
time.sleep(0.7)
ascii.convert_to_ascii()
time.sleep(4)
ph.printStartMessage()
time.sleep(4)
rc.runAll()
hp.clr()
#replace with your own custom present ;)
link = "https://youtu.be/nl62hhiBMOM"
print("\n\n\n\n\n\n")
print(f"And this is your final gift:\n\n".center(hp.terminal_size()))
print(link.center(hp.terminal_size()))
time.sleep(2)
print(f"\n\n\nPress Ctrl+C to end".center(hp.terminal_size()))

i = 0
while True:
    try:
        i += 1
    except KeyboardInterrupt:
        break