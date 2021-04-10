# Identificación de Sistema Operativo

A través de una traza ICMP con `ping` se visualiza que el valor del TTL es `127`, determinando en consecuencia que nos encontramos ante una máquina Windows:

```bash
> ping -c 1 10.10.10.93
PING 10.10.10.93 (10.10.10.93) 56(84) bytes of data.
64 bytes from 10.10.10.93: icmp_seq=1 ttl=127 time=65.1 ms

--- 10.10.10.93 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 65.106/65.106/65.106/0.000 ms
```

De forma alternativa, mediante la creación de un script en Python, fue posible determinar también el sistema operativo en uso por el equipo a auditar:

```python
#!/usr/bin/python

import subprocess, re, sys

def return_ttl(address):
        proc = subprocess.Popen(["ping -c 1 %s" % address, ""], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        out = out.split()
        out = re.findall(r"\d{1,3}", out[12])

        return out[0]

def return_ttl_os_name(ttl_number):

        if ttl_number >= 0 and ttl_number <= 64:
                return "Linux"
        elif ttl_number >= 65 and ttl_number <= 128:
                return "Windows"
        else:
                return "Unknown"

if len(sys.argv) != 2:
        print "\n[*] Usage: python " + sys.argv[0] + " <ip-address>\n"
        sys.exit(1)

if __name__ == '__main__':
        addr = sys.argv[1]
        ttl = return_ttl(addr)

        try:
                print "\n%s -> %s" % (addr, return_ttl_os_name(int(ttl)))
        except:
                pass
```

Obteniendo los siguientes resultados tras su ejecución:

```bash
> whichSystem.py 10.10.10.93

10.10.10.93 -> Windows
```