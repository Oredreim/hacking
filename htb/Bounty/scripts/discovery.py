#!/usr/bin/python3

import re
import signal
import requests
import pdb
import time

from pwn import *

def def_handler(sig, frame):
    print ("\n [+] saliendo...\n")


signal.signal(signal.SIGINT,def_handler)
if __name__=='__main__':
    time.sleep(10)

