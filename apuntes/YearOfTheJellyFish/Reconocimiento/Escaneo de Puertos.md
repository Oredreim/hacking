# Reconocimiento de puertos por TCP

A continuación, se detalla la metodología llevada a cabo para realizar una enumeración de puertos por TCP.

Para efectuar la enumeración, se ejecutó el siguiente comando con `nmap`:

```bash
> nmap -p- -sS --min-rate 5000 --open -vvv -n -Pn "IP" -oG allPorts
```

Este tipo de escaneo corresponde a un `TCP SYN Port Scan`. Este modo de escaneo particular fue desplegado debido al tiempo de respuesta del lado del servidor, con el objetivo de agilizar el descubrimiento de puertos sobre el activo.

Seguidamente, se ejecutó el siguiente comando con el propósito de obtener información exhaustiva sobre los puertos TCP encontrados, pudiendo así determinar tanto el servicio como la versión en uso:


```bash
   1   │ # Nmap 7.91 scan initiated Fri May 14 13:48:13 2021 as: nmap -sC -sV -p21,22,80,443,8000,8096 -oN targeted 63.35.209.118
   2   │ Nmap scan report for ec2-63-35-209-118.eu-west-1.compute.amazonaws.com (63.35.209.118)
   3   │ Host is up (0.11s latency).
   4   │ 
   5   │ PORT     STATE SERVICE  VERSION
   6   │ 21/tcp   open  ftp      vsftpd 3.0.3
   7   │ 22/tcp   open  ssh      OpenSSH 5.9p1 Debian 5ubuntu1.4 (Ubuntu Linux; protocol 2.0)
   8   │ | ssh-hostkey: 
   9   │ |_  2048 46:b2:81:be:e0:bc:a7:86:39:39:82:5b:bf:e5:65:58 (RSA)
  10   │ 80/tcp   open  http     Apache httpd 2.4.29
  11   │ |_http-server-header: Apache/2.4.29 (Ubuntu)
  12   │ |_http-title: Did not follow redirect to https://robyns-petshop.thm/
  13   │ 443/tcp  open  ssl/http Apache httpd 2.4.29 ((Ubuntu))
  14   │ |_http-server-header: Apache/2.4.29 (Ubuntu)
  15   │ |_http-title: Robyn&#039;s Pet Shop
  16   │ | ssl-cert: Subject: commonName=robyns-petshop.thm/organizationName=Robyns Petshop/stateOrProvinceName=South West/countryName=GB
  17   │ | Subject Alternative Name: DNS:robyns-petshop.thm, DNS:monitorr.robyns-petshop.thm, DNS:beta.robyns-petshop.thm, DNS:dev.robyns-petshop.thm
  18   │ | Not valid before: 2021-05-14T17:31:44
  19   │ |_Not valid after:  2022-05-14T17:31:44
  20   │ |_ssl-date: TLS randomness does not represent time
  21   │ | tls-alpn: 
  22   │ |_  http/1.1
  23   │ 8000/tcp open  http-alt
  24   │ | fingerprint-strings: 
  25   │ |   GenericLines: 
  26   │ |     HTTP/1.1 400 Bad Request
  27   │ |     Content-Length: 15
  28   │ |_    Request
  29   │ |_http-title: Under Development!
  30   │ |_http-trane-info: Problem with XML parsing of /evox/about
  31   │ 8096/tcp open  unknown
  32   │ | fingerprint-strings: 
  33   │ |   FourOhFourRequest: 
  34   │ |     HTTP/1.1 404 Not Found
  35   │ |     Connection: close
  36   │ |     Date: Fri, 14 May 2021 17:48:49 GMT
  37   │ |     Server: Kestrel
  38   │ |     Content-Length: 0
  39   │ |     X-Response-Time-ms: 311
  40   │ |   GenericLines: 
  41   │ |     HTTP/1.1 400 Bad Request
  42   │ |     Connection: close
  43   │ |     Date: Fri, 14 May 2021 17:48:20 GMT
  44   │ |     Server: Kestrel
  45   │ |     Content-Length: 0
  46   │ |   GetRequest: 
  47   │ |     HTTP/1.1 302 Found
  48   │ |     Connection: close
  49   │ |     Date: Fri, 14 May 2021 17:48:20 GMT
  50   │ |     Server: Kestrel
  51   │ |     Content-Length: 0
  52   │ |     Location: /web/index.html
  53   │ |   HTTPOptions: 
  54   │ |     HTTP/1.1 302 Found
  55   │ |     Connection: close
  56   │ |     Date: Fri, 14 May 2021 17:48:21 GMT
  57   │ |     Server: Kestrel
  58   │ |     Content-Length: 0
  59   │ |     Location: /web/index.html
  60   │ |   Help, SSLSessionReq: 
  61   │ |     HTTP/1.1 400 Bad Request
  62   │ |     Connection: close
  63   │ |     Date: Fri, 14 May 2021 17:48:37 GMT
  64   │ |     Server: Kestrel
  65   │ |     Content-Length: 0
  66   │ |   Kerberos, TLSSessionReq, TerminalServerCookie: 
  67   │ |     HTTP/1.1 400 Bad Request
  68   │ |     Connection: close
  69   │ |     Date: Fri, 14 May 2021 17:48:38 GMT
  70   │ |     Server: Kestrel
  71   │ |     Content-Length: 0
  72   │ |   LPDString: 
  73   │ |     HTTP/1.1 400 Bad Request
  74   │ |     Connection: close
  75   │ |     Date: Fri, 14 May 2021 17:48:50 GMT
  76   │ |     Server: Kestrel
  77   │ |     Content-Length: 0
  78   │ |   RTSPRequest: 
  79   │ |     HTTP/1.1 505 HTTP Version Not Supported
  80   │ |     Connection: close
  81   │ |     Date: Fri, 14 May 2021 17:48:21 GMT
  82   │ |     Server: Kestrel
  83   │ |_    Content-Length: 0
  84   │ 2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
  85   │ ==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
  86   │ SF-Port8000-TCP:V=7.91%I=7%D=5/14%Time=609EB7E9%P=x86_64-pc-linux-gnu%r(Ge
  87   │ SF:nericLines,3F,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Length:\x2
  88   │ SF:015\r\n\r\n400\x20Bad\x20Request");
  89   │ ==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
  90   │ SF-Port8096-TCP:V=7.91%I=7%D=5/14%Time=609EB7E4%P=x86_64-pc-linux-gnu%r(Ge
  91   │ SF:nericLines,78,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nConnection:\x20clo
  92   │ SF:se\r\nDate:\x20Fri,\x2014\x20May\x202021\x2017:48:20\x20GMT\r\nServer:\
  93   │ SF:x20Kestrel\r\nContent-Length:\x200\r\n\r\n")%r(GetRequest,8D,"HTTP/1\.1
  94   │ SF:\x20302\x20Found\r\nConnection:\x20close\r\nDate:\x20Fri,\x2014\x20May\
  95   │ SF:x202021\x2017:48:20\x20GMT\r\nServer:\x20Kestrel\r\nContent-Length:\x20
  96   │ SF:0\r\nLocation:\x20/web/index\.html\r\n\r\n")%r(HTTPOptions,8D,"HTTP/1\.
  97   │ SF:1\x20302\x20Found\r\nConnection:\x20close\r\nDate:\x20Fri,\x2014\x20May
  98   │ SF:\x202021\x2017:48:21\x20GMT\r\nServer:\x20Kestrel\r\nContent-Length:\x2
  99   │ SF:00\r\nLocation:\x20/web/index\.html\r\n\r\n")%r(RTSPRequest,87,"HTTP/1\
 100   │ SF:.1\x20505\x20HTTP\x20Version\x20Not\x20Supported\r\nConnection:\x20clos
 101   │ SF:e\r\nDate:\x20Fri,\x2014\x20May\x202021\x2017:48:21\x20GMT\r\nServer:\x
 102   │ SF:20Kestrel\r\nContent-Length:\x200\r\n\r\n")%r(Help,78,"HTTP/1\.1\x20400
 103   │ SF:\x20Bad\x20Request\r\nConnection:\x20close\r\nDate:\x20Fri,\x2014\x20Ma
 104   │ SF:y\x202021\x2017:48:37\x20GMT\r\nServer:\x20Kestrel\r\nContent-Length:\x
 105   │ SF:200\r\n\r\n")%r(SSLSessionReq,78,"HTTP/1\.1\x20400\x20Bad\x20Request\r\
 106   │ SF:nConnection:\x20close\r\nDate:\x20Fri,\x2014\x20May\x202021\x2017:48:37
 107   │ SF:\x20GMT\r\nServer:\x20Kestrel\r\nContent-Length:\x200\r\n\r\n")%r(Termi
 108   │ SF:nalServerCookie,78,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nConnection:\x
 109   │ SF:20close\r\nDate:\x20Fri,\x2014\x20May\x202021\x2017:48:38\x20GMT\r\nSer
 110   │ SF:ver:\x20Kestrel\r\nContent-Length:\x200\r\n\r\n")%r(TLSSessionReq,78,"H
 111   │ SF:TTP/1\.1\x20400\x20Bad\x20Request\r\nConnection:\x20close\r\nDate:\x20F
 112   │ SF:ri,\x2014\x20May\x202021\x2017:48:38\x20GMT\r\nServer:\x20Kestrel\r\nCo
 113   │ SF:ntent-Length:\x200\r\n\r\n")%r(Kerberos,78,"HTTP/1\.1\x20400\x20Bad\x20
 114   │ SF:Request\r\nConnection:\x20close\r\nDate:\x20Fri,\x2014\x20May\x202021\x
 115   │ SF:2017:48:38\x20GMT\r\nServer:\x20Kestrel\r\nContent-Length:\x200\r\n\r\n
 116   │ SF:")%r(FourOhFourRequest,8F,"HTTP/1\.1\x20404\x20Not\x20Found\r\nConnecti
 117   │ SF:on:\x20close\r\nDate:\x20Fri,\x2014\x20May\x202021\x2017:48:49\x20GMT\r
 118   │ SF:\nServer:\x20Kestrel\r\nContent-Length:\x200\r\nX-Response-Time-ms:\x20
 119   │ SF:311\r\n\r\n")%r(LPDString,78,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nCon
 120   │ SF:nection:\x20close\r\nDate:\x20Fri,\x2014\x20May\x202021\x2017:48:50\x20
 121   │ SF:GMT\r\nServer:\x20Kestrel\r\nContent-Length:\x200\r\n\r\n");
 122   │ Service Info: Host: robyns-petshop.thm; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
 123   │ 
 124   │ Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
 125   │ # Nmap done at Fri May 14 13:50:26 2021 -- 1 IP address (1 host up) scanned in 132.54 seconds

```