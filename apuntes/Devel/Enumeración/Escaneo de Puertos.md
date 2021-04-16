# Reconocimiento de puertos por TCP

A continuación, se detalla la metodología llevada a cabo para realizar una enumeración de puertos por TCP.

Para efectuar la enumeración, se ejecutó el siguiente comando con `nmap`:
```bash
nmap -p- -sS -T5 -vvv -n -Pn -oG allPorts 10.10.10.5
```

Este tipo de escaneo corresponde a un `TCP SYN Port Scan`. Este modo de escaneo particular fue desplegado debido al tiempo de respuesta del lado del servidor, con el objetivo de agilizar el descubrimiento de puertos sobre el activo.

Seguidamente, se ejecutó el siguiente comando con el propósito de obtener información exhaustiva sobre los puertos TCP encontrados, pudiendo así determinar tanto el servicio como la versión en uso:

```bash
   1   │ # Nmap 7.91 scan initiated Sat Apr  3 19:08:34 2021 as: nmap -sC -sV -p21,80 -oN targetted 10.10.10.5
   2   │ Nmap scan report for 10.10.10.5
   3   │ Host is up (0.099s latency).
   4   │ 
   5   │ PORT   STATE SERVICE VERSION
   6   │ 21/tcp open  ftp     Microsoft ftpd
   7   │ | ftp-anon: Anonymous FTP login allowed (FTP code 230)
   8   │ | 03-18-17  02:06AM       <DIR>          aspnet_client
   9   │ | 04-04-21  02:18AM                 1412 bendicion.asp
  10   │ | 04-04-21  02:05AM                 1581 cmdasp.asp
  11   │ | 03-17-17  05:37PM                  689 iisstart.htm
  12   │ | 04-04-21  02:00AM                   23 test.htm
  13   │ | 04-04-21  02:11AM                 1412 webshell.asp
  14   │ | 04-04-21  02:03AM                 4464 webshell.aspx
  15   │ |_03-17-17  05:37PM               184946 welcome.png
  16   │ | ftp-syst: 
  17   │ |_  SYST: Windows_NT
  18   │ 80/tcp open  http    Microsoft IIS httpd 7.5
  19   │ | http-methods: 
  20   │ |_  Potentially risky methods: TRACE
  21   │ |_http-server-header: Microsoft-IIS/7.5
  22   │ |_http-title: IIS7
  23   │ Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows
  24   │ 
  25   │ Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
  26   │ # Nmap done at Sat Apr  3 19:08:50 2021 -- 1 IP address (1 host up) scanned in 16.12 seconds
```


