# Enumeration.
Nmap scanning.

``` bash 
# Nmap 7.91 scan initiated Wed Jul 21 20:09:38 2021 as: nmap -sC -sV -vvv -T5 -oA targeted 10.10.10.161
Warning: 10.10.10.161 giving up on port because retransmission cap hit (2).
Nmap scan report for 10.10.10.161
Host is up, received echo-reply ttl 127 (0.21s latency).
Scanned at 2021-07-21 20:09:38 -05 for 38s
Not shown: 989 closed ports
Reason: 989 resets
PORT     STATE SERVICE      REASON          VERSION
53/tcp   open  domain       syn-ack ttl 127 Simple DNS Plus
88/tcp   open  kerberos-sec syn-ack ttl 127 Microsoft Windows Kerberos (server time: 2021-07-22 01:29:20Z)
135/tcp  open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
139/tcp  open  netbios-ssn  syn-ack ttl 127 Microsoft Windows netbios-ssn
389/tcp  open  ldap         syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: htb.local, Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds syn-ack ttl 127 Windows Server 2016 Standard 14393 microsoft-ds (workgroup: HTB)
464/tcp  open  kpasswd5?    syn-ack ttl 127
593/tcp  open  ncacn_http   syn-ack ttl 127 Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped   syn-ack ttl 127
3268/tcp open  ldap         syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: htb.local, Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped   syn-ack ttl 127
Service Info: Host: FOREST; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 2h39m30s, deviation: 4h02m31s, median: 19m29s
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 35384/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 32753/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 59040/udp): CLEAN (Timeout)
|   Check 4 (port 44587/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb-os-discovery: 
|   OS: Windows Server 2016 Standard 14393 (Windows Server 2016 Standard 6.3)
|   Computer name: FOREST
|   NetBIOS computer name: FOREST\x00
|   Domain name: htb.local
|   Forest name: htb.local
|   FQDN: FOREST.htb.local
|_  System time: 2021-07-21T18:29:32-07:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: required
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2021-07-22T01:29:33
|_  start_date: 2021-07-21T09:14:05

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jul 21 20:10:16 2021 -- 1 IP address (1 host up) scanned in 38.28 seconds
```

We see that there is a domain `htb.local` lets add it to our `/etc/hosts`.

Lets keep watching our nmap, and it says that there is a `smb` service lets try to enumerate it, after trying to do a lot of tools to get informartion, I finally found something with `rpcclient` 

``` bash
rpcclient -U "" -N 10.10.10.161
```

With this command I can get acces and enumerate some users.

![](Images/Pasted%20image%2020210721204018.png)

Lets now look for some domain groups.

![](Images/Pasted%20image%2020210721204133.png)

But nothing interesting.

# User.

Now lets use GetNPUsers.py to enumerate some password for the users we got.

![](Images/Pasted%20image%2020210721213135.png)

![](Images/Pasted%20image%2020210721213529.png)

Now lets crack the hash with `john the ripper`.

![](Images/Pasted%20image%2020210721214507.png)

And we got the password.

I use `evil-winrm` to get access to the machine with the user and password I got.

![](Images/Pasted%20image%2020210721214623.png)

# Privilege Scalation.
I had no idea what to do here to get root, but I could do something to understand and see how can I get root.

Lets use BloodHound.

After I uploaded everything to get the `.zip` to put in BloodHound. I got this path to Domain Admin.

![](Images/Pasted%20image%2020210722112244.png)

So it says I can create new users, and give them group domain, cause with this user `svc-alfresco` I'm not part of a group.

So lets create the user and add it to a group.

![](Images/Pasted%20image%2020210722135746.png)

Now I just need to check the `help` on the path and follow the commands it says I must do.

![](Images/Pasted%20image%2020210722141329.png)

It says also I need to use `PowerView.ps1`, I need to reopen a service with python to put the file on the victim machine, lets do that again but put in `PowerView.ps1`.

![](Images/Pasted%20image%2020210722150208.png)
![](Images/Pasted%20image%2020210722143702.png)
![](Images/Pasted%20image%2020210722150123.png)

Now i can use an other tool to dump the hash from the administrator user. Named secretdump.py and we give it permissions with the user and password we create.

![](Images/Pasted%20image%2020210722150309.png)

I have now a Administrator's hash. I can use it to get access to the victim machine with the tool `pth-winexe`.
![](Images/Pasted%20image%2020210722150721.png)
