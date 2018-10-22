# Sirviendo aplicaciones PHP y Python

## Sito web 1

http://php.alu6124.me

Configuramos la web para que pueda interpretar ficheros .php, para ello creamos el fichero /etc/nginx/sites-available/php.alu6224.me.

![](imagenes/1.PNG)

Añadimos el location php con esta configuración y declaramos que el autoindex sea .php.

![](imagenes/2.PNG)

Hacemos el enlace con el comando ln -s ../sites-available/php.alu6124.me.

![](imagenes/2.5.PNG)

Ahora nos situamos en la ruta /webapps/php y dentro del directorio hacemos un wget para obtener el zip.

![](imagenes/3.PNG)

Ejecutamos la herramienta unzip y extraemos los archivos del zip.

![](imagenes/4.PNG)

Ahora accedemos al directorio que hemos descomprimido y extraemos los archivos al directorio php.

![](imagenes/5.PNG)

Comprobamos que la web funciona correctamente.

![](imagenes/6.PNG)

## Sitio web 2

http://now.alu6124.me

Creamos el virtual host para la aplicación Python, ejecutamos el comando */etc/nginx/sites-available/now.alu6124.me.*

![](imagenes/10.PNG)

Configuramos el fichero tal que así, el puerto que hemos añadido es el *8081* dado que el *8080* ya está en uso.

![](imagenes/11.PNG)

Enlazamos el virtual host para habilitarlo, accedemos a la ruta /etc/nginx/sites-enabled/ y ejecutamos el comando *ln -s ../sites-available/now.alu6124.me* recargamos nginx y comprobamos.

![](imagenes/12.PNG)

Accedemos a la ruta */webapps/now* y creamos *now.py* con el siguiente código.

![](imagenes/14.PNG)

Lanzamos el proceso *uwsgi --socket :8081 --protocol http --home $(pipenv --venv) -w now:app* para que escuche las peticiones.

![](imagenes/15.1.PNG)
![](imagenes/15.PNG)

Comprobamos que funciona.

![](imagenes/16.PNG)

Creamos un script llamado *run.sh* para que sintetice el comando que hemos creado en *now.py*, le indicamos que escuche el puerto *8081*.

![](imagenes/17.PNG)

Le damos permisos de ejecución.

![](imagenes/18.PNG)

Ejecutamos *run.sh* y comprobamos que esta funcionando y que ya se encuentra el puerto *8081* en esucha.

![](imagenes/19.PNG)

En el entorno virtual instalamos los paquetes Flask y pytz, ambos deben residir en */home/webapps/now.*

![](imagenes/20.PNG)

![](imagenes/21.PNG)

Configuramos **supervisor** para que gestione el proceso *uwsgi*, indicamos las rutas correctas.

![](imagenes/22.PNG)

Comprobamos que se ha creado y reinciamos **supervisor**.

![](imagenes/23.PNG)

Accedemos a la web solo con la ruta http://now.alu6124.me sin poner el puerto *8081* para comprobar que funciona correctamente.

![](imagenes/24.PNG)

Comprobamos los siguientes comandos y la respuesta del navergador.

**supervisorctl status**

![](imagenes/25.PNG)

**supervisorctl start now**

![](imagenes/28.PNG)

**supervisorctl stop now**

![](imagenes/26.PNG)

**supervisorctl restart now**

![](imagenes/27.PNG)
