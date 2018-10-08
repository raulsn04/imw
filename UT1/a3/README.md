# **Trabajos con virtual host**

## En esta actividad vamos a crear 4 Virtual host (sitios web) en el servidor de **Nginx**.

## Sitio web 1

Debemos mostrar una página con la imagen del diagrama de unidades de trabajo, para ello debemos descargar la imagen al directorio de trabajo de la máquina de producción.
Para ello debemos usar un tag <img> apuntando a la ruta local.

**imw.alu6124.me**

configuramos la página imw.alu6124.me en el archivo de configuración */etc/nginx/sites-available/imw.alu6124.me*

![imagenes](imagenes/1.PNG)

ahora enlazamos el fichero, para ello accedemos a la ruta */etc/sites-enabled* y con el comando ln -s ../sites-available/imw.alu6124.me, una vez echo esto recargamos el servicio y comprobamos que se ha creado.

![imagenes](imagenes/2.PNG)

volvemos a la ruta anterior y cremos la carpeta imw y dentro de ella creamos un index.html.
para obtener la imagen debemos ejecutar el comando wget junto con la ruta de la imagen.

![imagenes](imagenes/3.PNG)

comprobamos que el index y la imagen se encuentran en la carpeta correctamente.

![imagenes](imagenes/4.PNG)

editamos el index y añadimos un título y el tag para la imagen.

![imagenes](imagenes/5.PNG)

accedemos a la página para comprobar que funciona.

![imagenes](imagenes/6.PNG)

**http://imw.alu6124.me/mec/**

añadimos el location a la ruta de mec.

![imagenes](imagenes/1.PNG)

creamos la carpeta mec y el index.html.

![imagenes](imagenes/7.PNG)

editamos el index.html, añadimos un título y el enlace al Real decreto del título de Administración de Sistemas Informáticos en Red.

![imagenes](imagenes/8.PNG)

comprobamos que la pagina funciona y muestra el enlace al Real decreto.

![imagenes](imagenes/9.PNG)


## Sitio web 2

**http://varlib/alu6124.me:9000**

configuramos la página imw.alu6124.me en el archivo de configuración */etc/nginx/sites-available/varlib.alu6124.me*

![imagenes](imagenes/11.PNG)

ahora enlazamos el fichero, para ello accedemos a la ruta */etc/sites-enabled* y con el comando ln -s ../sites-available/varlib.alu6124.me, una vez echo esto recargamos el servicio y comprobamos que se ha creado.

![imagenes](imagenes/12.PNG)


recargamos el servicio.

![imagenes](imagenes/13.PNG)

creamos la carpeta varlib.

![imagenes](imagenes/14.PNG)

le añadimos autoindex on, y que escuche el puerto 9000.

![imagenes](imagenes/15.PNG)

hacemos el enlace, comprobamos que se ha creado y recargamos el servicio.

![imagenes](imagenes/16.PNG)

comprobamos que funciona la web y el enlace

![imagenes](imagenes/17.PNG)

![imagenes](imagenes/18.PNG)

## Sitio web 3

** https://ssl.alu6124.me/students/**

creamos la carpeta students.

![imagenes](imagenes/21.PNG)

dentro de la carpeta students ejecutamos el comando perl -le 'print crypt("aula108",'fewsalt')' para que nos encripte la contraseña que va a tener el usuario1, una vez ejecutado nos muestra la contraseña encriptada, luego creamos el fichero .htpasswd y dentro añadimos el nombre del usuario y la contraseña.

![imagenes](imagenes/22.PNG)

![imagenes](imagenes/23.PNG)
