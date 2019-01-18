# Instalación de Wordpress
# Vamos a instalar un sitio web Wordpress en nuestra máquina de producción.

### Configuración de la base de datos.
Wordpress necesita credenciales (usuario/contraseña) para acceder a una base de datos. Para ello, usaremos el intérprete de MySQL, **tenemos que crear la base de datos, el usuario y asignar privilegios:**

![](imagen/1.PNG)


### Descarga de código
**Descargamos el código fuente de Wordpress desde su página web y descomprimimos el código y lo copiamos en /usr/share:**

![](imagen/2.PNG)

![](imagen/3.PNG)

Ahora tenemos que establecer los permisos necesarios para que el usuario web www-data pueda usar estos ficheros:

![](imagen/4.PNG)

### Editar ficheros de configuración
Para una configuración básica de WordPress debemos especificar lo siguiente:
**El nombre de la base de datos.
El usuario.
La contraseña.**

Para ello copiamos el archivo y lo renombramos antes de modificarlo.

![](imagen/5.PNG)

Editamos el fichero una vez realizado el paso anterior.

![](imagen/6.PNG)

### Acceso mediante Nginx.
Para que nuestro sitio Wordpress sea accesible desde un navegador web, debemos incluir las directivas necesarias en la configuración del servidor web Nginx.

![](imagen/7.0.PNG)

Creamos un nuevo virtual host.

![](imagen/7.PNG)

Enlazamos la configuración para que el virtual host esté disponible:

![](imagen/8.PNG)

Recargamos el servidor web Nginx para que los cambios sean efectivos y lo comprobamos.

![](imagen/9.PNG)


Una vez instalado comenzamos la configuración de nuestro Wordpress vía web.

![](imagen/10.PNG)

Elegimos idioma español y le damos a continuar.

![](imagen/11.PNG)

Rellenamos los campos.

![](imagen/12.PNG)

Accedemos con nuestras credenciales.

![](imagen/13.PNG)

![](imagen/14.PNG)

### Ajuste de permalinks
En primer lugar activamos esta opción dentro de la interfaz administrativa de Wordpress:

![](imagen/15.PNG)

Seleccionamos el ajuste Día y nombre.

### Ahora debemos indicar a Nginx que procese estas URLs:

![](imagen/16.0.PNG)


![](imagen/16.PNG)


### Recargamos la configuración de Nginx:

![](imagen/17.PNG)


### Límite de tamaño en la subida de archivos.

Buscamos las siguientes lineas en el codigo php.ini de la ruta /etc/php/7.2/fpm.

![](imagen/18.PNG)

![](imagen/19.PNG)

![](imagen/20.PNG)

### Ahora reinciamos el servicio php-fpm:

![](imagen/21.PNG)

### Añadimos una línea en el fichero de configuración de Nginx:

![](imagen/22.PNG)

### A continuación reiniciamos el servidor web Nginx para que tengan efectos los cambios realizados en el fichero de configuración:

![](imagen/23.PNG)

La estructuras de ficheros ha quedado tal que así.

![](imagen/24.PNG)

## WordPress

Ahora elegimos un tema y lo configuramos, además de escribir un post con las estadísticas de wordpress.

![](imagen/26.PNG)

![](imagen/25.PNG)
