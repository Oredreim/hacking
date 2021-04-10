# Reconocimiento de puertos por TCP

A continuación, se detalla la metodología llevada a cabo para realizar una enumeración de puertos por TCP.

Para efectuar la enumeración, se ejecutó el siguiente comando con `nmap`:

```bash
> nmap -p- -sS --min-rate 5000 --open -vvv -n -Pn 10.10.10.93 -oG allPorts
```

Este tipo de escaneo corresponde a un `TCP SYN Port Scan`. Este modo de escaneo particular fue desplegado debido al tiempo de respuesta del lado del servidor, con el objetivo de agilizar el descubrimiento de puertos sobre el activo.

Seguidamente, se ejecutó el siguiente comando con el propósito de obtener información exhaustiva sobre los puertos TCP encontrados, pudiendo así determinar tanto el servicio como la versión en uso:

```bash
> nmap -sC -sV -p80 10.10.10.93 -oN targeted
Starting Nmap 7.91 ( https://nmap.org ) at 2021-04-10 20:57 WEST
Nmap scan report for 10.10.10.93
Host is up (0.069s latency).

PORT   STATE SERVICE VERSION
80/tcp open  http    Microsoft IIS httpd 7.5
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/7.5
|_http-title: Bounty
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 23.78 seconds
```