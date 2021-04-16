# Descubrimiento de rutas

Mediante el uso de la utilidad `gobuster`, atendiendo a la respuesta del lado del servidor, ha sido posible encontrar los siguientes recursos existentes en la página web:

* **/UploadedFiles**
* **/transfer.aspx**

A continuación, se reportan las evidencias:

* **/UploadedFiles**

```bash
 1   │ http://10.10.10.5/aspnet_client        (Status: 301) [Size: 155] [--> http://10.10.10.5/aspnet_client/]

```
