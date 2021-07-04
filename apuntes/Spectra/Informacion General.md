# Reconocimiento de puertos por TCP

To solve this machine we start with some enumeration ports (open services).

``` bash
───────┬───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
       │ File: nmapScan
───────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
   1   │ # Nmap 7.91 scan initiated Sun Jul  4 14:06:50 2021 as: nmap -p- -sS --min-rate 5000 --open -vvvv -n -Pn -oN allPortss 10.10.10.229
   2   │ Nmap scan report for 10.10.10.229
   3   │ Host is up, received user-set (0.56s latency).
   4   │ Scanned at 2021-07-04 14:06:50 -05 for 175s
   5   │ Not shown: 52501 filtered ports, 13031 closed ports
   6   │ Reason: 52501 no-responses and 13031 resets
   7   │ Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
   8   │ PORT     STATE SERVICE REASON
   9   │ 22/tcp   open  ssh     syn-ack ttl 63
  10   │ 80/tcp   open  http    syn-ack ttl 63
  11   │ 3306/tcp open  mysql   syn-ack ttl 63
  12   │
  13   │ Read data files from: /usr/bin/../share/nmap
  14   │ # Nmap done at Sun Jul  4 14:09:45 2021 -- 1 IP address (1 host up) scanned in 175.22 seconds
───────┴───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
```

There are some open ports `22,80,3306` we separate the nmap command in two. the first one to scan port recognition and it will work faster. then we can do the enumeration open services. So lets do it, Starting with port `22`and `80` we can see those are ssh and http and 80 is a webservers. And `3306` is a `mySQL services`.

``` bash
───────┬───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
       │ File: targeted
───────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
   1   │ # Nmap 7.91 scan initiated Sun Jul  4 14:34:30 2021 as: nmap -sC -sV -p22,80,3306 -oN targeted 10.10.10.229
   2   │ Nmap scan report for 10.10.10.229
   3   │ Host is up (0.11s latency).
   4   │
   5   │ PORT     STATE SERVICE VERSION
   6   │ 22/tcp   open  ssh     OpenSSH 8.1 (protocol 2.0)
   7   │ | ssh-hostkey:
   8   │ |_  4096 52:47:de:5c:37:4f:29:0e:8e:1d:88:6e:f9:23:4d:5a (RSA)
   9   │ 80/tcp   open  http    nginx 1.17.4
  10   │ |_http-server-header: nginx/1.17.4
  11   │ |_http-title: Site doesn't have a title (text/html).
  12   │ 3306/tcp open  mysql   MySQL (unauthorized)
  13   │ |_ssl-cert: ERROR: Script execution failed (use -d to debug)
  14   │ |_ssl-date: ERROR: Script execution failed (use -d to debug)
  15   │ |_sslv2: ERROR: Script execution failed (use -d to debug)
  16   │ |_tls-alpn: ERROR: Script execution failed (use -d to debug)
  17   │ |_tls-nextprotoneg: ERROR: Script execution failed (use -d to debug)
  18   │
  19   │ Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
  20   │ # Nmap done at Sun Jul  4 14:35:10 2021 -- 1 IP address (1 host up) scanned in 40.30 seconds
───────┴───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
```

Before we keep going to the 80port web server. lets do more service enumerations. Lets do some `whatweb` enumeration, and some web directory enumeration.

``` bash 
whatweb 10.10.10.229
http://10.10.10.229 [200 OK] Country[RESERVED][ZZ], HTTPServer[nginx/1.17.4], IP[10.10.10.229], nginx[1.17.4]
```

``` bash 
wfuzz -c -z file,/usr/share/wfuzz/wordlist/general/common.txt --hc 404 http://10.10.10.229/FUZZ
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://10.10.10.229/FUZZ
Total requests: 951

=====================================================================
ID           Response   Lines    Word       Chars       Payload
=====================================================================

000000501:   301        7 L      11 W       169 Ch      "main"
000000831:   301        7 L      11 W       169 Ch      "testing"

Total time: 0
Processed Requests: 951
Filtered Requests: 949
Requests/sec.: 0
```

We see some intersting directories `main and testing`.

So now we can go to web server and check what it has.
![[Pasted image 20210704145807.png]]

