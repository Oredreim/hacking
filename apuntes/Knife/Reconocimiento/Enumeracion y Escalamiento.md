# Enumeracion.
Ingresamos al servicio web pero logramos notar que no encontramos ninguna funcionalidad en esta.

![[Pasted image 20210623124010.png]]

A lo que procedemos a utilizar otras herramientas para lograr enumerar la pagina.

Utilizamos Gobuster pero no logramos encontrar ningun directorio.

Haciendo un curl a la pagina para intentar saber la version de php no logramos encontrar nada.
loca
A lo que procedemos a utilizar burpsuite para investigar un poco mas y logramos notar que el servicio de PHP es de version `PHP/8.1.0-dev`

![[Pasted image 20210623125946.png]]

Logramos encontrar una vulnerabilidad usando la cabezera `User-Agentt` la cual con la funcion `zerodiumsystem()` con la cual logramos ejecutar comandos de sistemas.

![[Pasted image 20210623131046.png]]

# Vulnerabilidad.
Gracias a esta funcion logramos hacer una reverseshell con bash y nos ponemos en escucha por el puerto 1337 para lograr la conexion.

![[Pasted image 20210625122418.png]]

![[Pasted image 20210625122434.png]]

Y somos ahora propietarios del usuario `james`

# Escalamiento de privilegios.

Con el comando `sudo -l` logramos notar que james puede ejecutar el comando /user/bin/knife como administrador (root) el cual nos redirige a chef-workstation que no es mas que la carpeta de instalacion de ruby.

![[Pasted image 20210625122825.png]]

Entonces podemos utilizar este comando para redireccionarlo a un ruby que nosotros hagamos para lograr escalar privilegios como root.

![[Pasted image 20210625123445.png]]


