#!/usr/bin/env python3

from forward_shell import ForwardShell 
import signal, sys 
from termcolor import colored

def ctrl_c(sig,frame):
    print(colored(f"\n[!] Exiting...", "red"))
    fs.remove_data()
    sys.exit(1)

signal.signal(signal.SIGINT,ctrl_c)

if __name__ == "__main__":
    fs = ForwardShell()
    fs.run()
