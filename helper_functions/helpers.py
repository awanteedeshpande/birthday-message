from contextlib import contextmanager
import os
import subprocess
import sys

#Do not print what is not required
@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout

#install necessary packages
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def terminal_size():
    width = os.get_terminal_size().columns
    return width

def clr():
    os.system('cls' if os.name == 'nt' else 'clear')