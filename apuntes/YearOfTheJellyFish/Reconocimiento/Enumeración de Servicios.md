# Enumeración de servicios encontrados

De forma alternativa, se hizo uso de la utilidad `whatweb`, determinando que el gestor de contenido en uso para el servicio HTTP encontrado por el puerto 80 es un **Internet Information Services** (IIS):

```bash
> http://3.249.136.61 [302 Found] Apache[2.4.29], Country[UNITED STATES][US], HTTPServer[Ubuntu Linux][Apache/2.4.29 (Ubuntu)], IP[3.249.136.61], RedirectLocation[https://robyns-petshop.thm/], Title[302 Found]
```

Ademas, por los puertos que se encuentran abiertos, tambien se peude hacer una enumeracion de los servicios que estos corren:

puerto 8000
```bash
http://3.249.136.61:8000 [200 OK] Country[UNITED STATES][US], IP[3.249.136.61], Title[Under Development!]
```
puerto 8096
```bash
http://3.249.136.61:8096 [302 Found] Country[UNITED STATES][US], HTTPServer[Kestrel], IP[3.249.136.61], RedirectLocation[/web/index.html]
http://3.249.136.61:8096/web/index.html [200 OK] Country[UNITED STATES][US], HTML5, HTTPServer[Kestrel], IP[3.249.136.61], Open-Graph-Protocol[article], Script, Title[Jellyfin], UncommonHeaders[x-response-time-ms]
```