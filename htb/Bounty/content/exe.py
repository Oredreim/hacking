import re
import signal
import requests
import pdb
import time
import sys

from pwn import *

def def_handler(sig, frame):
    print("\n[!] Saliendo...\n")
    sys.exit(1)

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

# Variables globales
upload_url = "http://10.10.10.93/transfer.aspx"
burp = {'http': 'http://127.0.0.1:8080'}

def uploadFile(extension):

    s = requests.session()
    filename = "example%s" % extension
    response = s.get(upload_url)

    ViewState = re.findall(r'__VIEWSTATE" value="(.*?)"', response.text)[0]
    EventValidation = re.findall(r'__EVENTVALIDATION" value="(.*?)"', response.text)[0]

    uploaded_file = {'FileUpload1': (filename,"Contenido de prueba")}

    data_post = {
        '__VIEWSTATE': ViewState,
        '__EVENTVALIDATION': EventValidation,
        'btnUpload': 'Upload'
    }

    response = s.post(upload_url, data=data_post, files=uploaded_file, proxies=burp)

    if "Invalid File. Please try again" not in response.text:
        p1.success("La extensión %s es válida" % extension)

if __name__ == '__main__':

    fp = open("extensions", "r")

    p1 = log.progress("Subida de archivos")
    p1.status("Subiendo archivos al servidor")
    time.sleep(2)

    for extension in fp:
        p1.status("Probando con extensión %s" % extension)
        uploadFile(extension.strip('\n'))