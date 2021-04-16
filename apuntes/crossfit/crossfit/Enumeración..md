## Enumeración.

A continuación, se detalla la metodología llevada a cabo para realizar una enumeración de puertos por TCP.

Para efectuar la enumeración, se ejecutó el siguiente comando con `nmap`:
```bash
[*] Extracting information...

        [*] IP Address: 10.10.10.208
        [*] Open ports: 21,22,80

[*] Ports copied to clipboard
```

Este tipo de escaneo corresponde a un TCP SYN Port Scan. Este modo de escaneo particular fue desplegado debido al tiempo de respuesta del lado del servidor, con el objetivo de agilizar el descubrimiento de puertos sobre el activo.

Seguidamente, se ejecutó el siguiente comando con el propósito de obtener información exhaustiva sobre los puertos TCP encontrados, pudiendo así determinar tanto el servicio como la versión en uso:

FTP over SSL
HTTP: Default page
Host: ebian 10+deb10u2 (protocol 2.0) 
```bash
   1   │ # Nmap 7.91 scan initiated Thu Apr 15 11:57:46 2021 as: nmap -sC -sV -p21,22,80 -oN targeted 10.10.10.208
   2   │ Nmap scan report for 10.10.10.208
   3   │ Host is up (0.12s latency).
   4   │ 
   5   │ PORT   STATE SERVICE VERSION
   6   │ 21/tcp open  ftp     vsftpd 2.0.8 or later
   7   │ | ssl-cert: Subject: commonName=*.crossfit.htb/organizationName=Cross Fit Ltd./stateOrProvinceName=NY/countryNa
       │ me=US
   8   │ | Not valid before: 2020-04-30T19:16:46
   9   │ |_Not valid after:  3991-08-16T19:16:46
  10   │ |_ssl-date: TLS randomness does not represent time
  11   │ 22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
  12   │ | ssh-hostkey: 
  13   │ |   2048 b0:e7:5f:5f:7e:5a:4f:e8:e4:cf:f1:98:01:cb:3f:52 (RSA)
  14   │ |   256 67:88:2d:20:a5:c1:a7:71:50:2b:c8:07:a4:b2:60:e5 (ECDSA)
  15   │ |_  256 62:ce:a3:15:93:c8:8c:b6:8e:23:1d:66:52:f4:4f:ef (ED25519)
  16   │ 80/tcp open  http    Apache httpd 2.4.38 ((Debian))
  17   │ |_http-server-header: Apache/2.4.38 (Debian)
  18   │ |_http-title: Apache2 Debian Default Page: It works
  19   │ Service Info: Host: Cross; OS: Linux; CPE: cpe:/o:linux:linux_kernel
  20   │ 
  21   │ Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
  22   │ # Nmap done at Thu Apr 15 11:58:09 2021 -- 1 IP address (1 host up) scanned in 23.56 seconds

```
## openssl
```bash
ONNECTED(00000003)                                                                                                     
Can't use SSL_get_servername                                                                                            
depth=0 C = US, ST = NY, O = Cross Fit Ltd., CN = *.crossfit.htb, emailAddress = info@gym-club.crossfit.htb             
verify error:num=18:self signed certificate                                                                             
verify return:1                                                                                                         
depth=0 C = US, ST = NY, O = Cross Fit Ltd., CN = *.crossfit.htb, emailAddress = info@gym-club.crossfit.htb             
verify return:1                                                                                                         
---                                                                                                                     
Certificate chain                                                                                                       
 0 s:C = US, ST = NY, O = Cross Fit Ltd., CN = *.crossfit.htb, emailAddress = info@gym-club.crossfit.htb                
   i:C = US, ST = NY, O = Cross Fit Ltd., CN = *.crossfit.htb, emailAddress = info@gym-club.crossfit.htb                
---                                                                                                                     
Server certificate                                                                                                      
-----BEGIN CERTIFICATE-----                                                                                             
MIID0TCCArmgAwIBAgIUFlxL1ZITpUBfx69st7fRkJcsNI8wDQYJKoZIhvcNAQEL                                                        
BQAwdzELMAkGA1UEBhMCVVMxCzAJBgNVBAgMAk5ZMRcwFQYDVQQKDA5Dcm9zcyBG                                                        
aXQgTHRkLjEXMBUGA1UEAwwOKi5jcm9zc2ZpdC5odGIxKTAnBgkqhkiG9w0BCQEW                                                        
GmluZm9AZ3ltLWNsdWIuY3Jvc3NmaXQuaHRiMCAXDTIwMDQzMDE5MTY0NloYDzM5                                                        
OTEwODE2MTkxNjQ2WjB3MQswCQYDVQQGEwJVUzELMAkGA1UECAwCTlkxFzAVBgNV                                                        
BAoMDkNyb3NzIEZpdCBMdGQuMRcwFQYDVQQDDA4qLmNyb3NzZml0Lmh0YjEpMCcG                                                        
CSqGSIb3DQEJARYaaW5mb0BneW0tY2x1Yi5jcm9zc2ZpdC5odGIwggEiMA0GCSqG                                                        
SIb3DQEBAQUAA4IBDwAwggEKAoIBAQDgibxJvtPny7Vee6M0BFBPFBohEQ+0zLDq                                                        
LdkW/OSl4tfEdZYn6U5cNYKTyYJ8CuytGlMpFw5OgOBPATtBYoGrQZdlN+7LQwF+                                                        
CZsedPs30ijAhygI7pM5S0hwiqdVReR/hhFHD/zry3M5+9NGeDLPgLbQG8qgPspv                                                        
Y+ErCXXotxVI+VrTPfGkjPixfgUTYsEetrkmXlig0S2ukxmNs7HXkjli4Z+qpGrn                                                        
mpFQokBE6RlD6VjxPzx0pfgK587s7F0/pIfXTHGfIOMnqXuLKBXsYIAEjJQxlLUt                                                        
U3lb7aZdqIZnvhTuzuOxFUIe5dRWyfERyODEd5WUlwsbY4Qo2HhZAgMBAAGjUzBR                                                        
MB0GA1UdDgQWBBTG3S2NuuXiSQ4dRvDnLqiWQdvY7jAfBgNVHSMEGDAWgBTG3S2N                                                        
uuXiSQ4dRvDnLqiWQdvY7jAPBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3DQEBCwUA                                                        
A4IBAQB/tGKHZ9oXsqLGGW0wRRgCZj2adl1sq3S69e9R4yVQW7zU2Sw38CAA/O07                                                        
MEgbqrzUI0c/T+Wb1D+gRamCUxSB7FXfMzGRhwUqMsLp8uGNlxyDcMU34ecRwOil                                                        
r4jLmfeGyok1r8CFHg8Om1TeZfzNeVtkAkqf3XoIxbKQk4s779n/84FAtLkZNqyb                                                        
cSv8nnClQQSlf42P3AiRBbwM1Cx9SyKq977sIwOzKTOM4NcSivNdtov+Pc0z+T9I                                                        
95SsqLKtO/8T0h6hgY6JQG1+A4ivnlZ8nqSFWYsnX10lJN2URlAwXUYuTw0vCMy+                                                        
Xk0OmbR/oG052H02ZsmfJQhqPNF1                                                                                            
-----END CERTIFICATE----- 
```