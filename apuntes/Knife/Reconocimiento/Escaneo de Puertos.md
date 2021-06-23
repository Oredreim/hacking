# Reconocimiento de puertos por TCP

Gracias a NMAP logramos escanear los puertos abiertos de la maquina **Knife**

```bash
───────┬────────────────────────────────────────────────────────────────────────────────────────────────────────────────
       │ File: allPorts
───────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────
   1   │ # Nmap 7.91 scan initiated Wed Jun 23 10:42:08 2021 as: nmap -p- --open -sS -T5 -vvv -n -Pn -oG allPorts 10.10.
       │ 10.242
   2   │ # Ports scanned: TCP(65535;1-65535) UDP(0;) SCTP(0;) PROTOCOLS(0;)
   3   │ Host: 10.10.10.242 ()   Status: Up
   4   │ Host: 10.10.10.242 ()   Ports: 22/open/tcp//ssh///, 80/open/tcp//http///    Ignored State: closed (65533)
   5   │ # Nmap done at Wed Jun 23 10:42:40 2021 -- 1 IP address (1 host up) scanned in 32.76 seconds

   
```


Ahora Iremos a revisar los servicios que ofrecen estos puertos abiertos:

```bash
───────┬────────────────────────────────────────────────────────────────────────────────────────────────────────────────
       │ File: targeted
───────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────
   1   │ # Nmap 7.91 scan initiated Wed Jun 23 10:45:39 2021 as: nmap -sC -sV -p22,80 -oN targeted 10.10.10.242
   2   │ Nmap scan report for 10.10.10.242
   3   │ Host is up (0.11s latency).
   4   │ 
   5   │ PORT   STATE SERVICE VERSION
   6   │ 22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
   7   │ | ssh-hostkey: 
   8   │ |   3072 be:54:9c:a3:67:c3:15:c3:64:71:7f:6a:53:4a:4c:21 (RSA)
   9   │ |   256 bf:8a:3f:d4:06:e9:2e:87:4e:c9:7e:ab:22:0e:c0:ee (ECDSA)
  10   │ |_  256 1a:de:a1:cc:37:ce:53:bb:1b:fb:2b:0b:ad:b3:f6:84 (ED25519)
  11   │ 80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
  12   │ |_http-server-header: Apache/2.4.41 (Ubuntu)
  13   │ |_http-title:  Emergent Medical Idea
  14   │ Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
  15   │ 
  16   │ Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
  17   │ # Nmap done at Wed Jun 23 10:45:59 2021 -- 1 IP address (1 host up) scanned in 19.46 seconds
───────┴────────────────────────────────────────────────────────────────────────────────────────────────────────────────

```
