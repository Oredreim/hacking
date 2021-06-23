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