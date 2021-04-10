# Enumeración de servicios encontrados

De forma alternativa, se hizo uso de la utilidad `whatweb`, determinando que el gestor de contenido en uso para el servicio HTTP encontrado por el puerto 80 es un **Internet Information Services** (IIS):

```bash
> whatweb http://10.10.10.93
http://10.10.10.93 [200 OK] Country[RESERVED][ZZ], HTTPServer[Microsoft-IIS/7.5], IP[10.10.10.93], Microsoft-IIS[7.5], Title[Bounty], X-Powered-By[ASP.NET]
```