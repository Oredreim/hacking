# Descubrimiento de rutas

Mediante el uso de la utilidad `gobuster`, atendiendo a la respuesta del lado del servidor, ha sido posible encontrar los siguientes recursos existentes en la página web:

* **/UploadedFiles**
* **/transfer.aspx**

A continuación, se reportan las evidencias:

* **/UploadedFiles**

```bash
gobuster dir -u http://10.10.10.93 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 25
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.10.93
[+] Threads:        25
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2021/04/10 21:07:44 Starting gobuster
===============================================================
/UploadedFiles (Status: 301)
```

* **/transfer.aspx**

```bash
gobuster dir -u http://10.10.10.93 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x aspx -t 25
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.10.93
[+] Threads:        25
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Extensions:     aspx
[+] Timeout:        10s
===============================================================
2021/04/10 21:10:38 Starting gobuster
===============================================================
/transfer.aspx (Status: 200)
```
