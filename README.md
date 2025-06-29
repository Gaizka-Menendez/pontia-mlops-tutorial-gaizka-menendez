# ML Training Project

 Este proyecto entrena un modelo de random Forest con datos sacados de la página oficial de [text](https://archive.ics.uci.edu/datasets). El proyecto se estructura en las siguientes carpetas:

 - `github/workflows` (Parte esencial para la integración, construcción y despliegue del modelo de RandomForest)

    Integration (`github/workflows/integration`) -> controla la integracion de nuevos cambios, esta preparado para ejecutarse cada vez que se realice una pull request a main y controla que todo está listo para comenzar con la siguiente fase. Entre sus acciones: ejecuta los tests en python de la carpeta tests y genera un reporte de los mismos. Además en caso de fallo de alguno de los mismos evita que la PR se fusione con el resto del código así preveniendo el código de main de verse afectado.

    Build (`github/workflows/build`) -> se ejecuta cada vez que se suben cambios a main o también de forma manual. Sus diferentes steps lo que hacen es descargar los datasets empleados por nuestro modelo y los alamacena en una carpeta para que sean manejables por el propio modelo. Se lanza el entrenamiento y el guardado del modelo al lanzar main (aqui en main se prepara los datos dividiendolos en dos conjuntos, entrena el modelo con esos conjuntos, calcula el tiempo tardado y genera los diferentes artefactos/archivos que se guardarán en la ruta de MLFlow). Se eejecutan los test de como de bien fue nuestro modelo y finalmente se guarda el mismo.

    Deploy (`github/workflows/deploy`) -> finalmente el deploy lo que hace es asegurarse que el entorno es estable y esta listo para ser usado. Realiza la autentificación requerida para realizar los siguientes steps y conecta con azure para comenzar la comunicación. Prepara y creamla imagen y el contenedor donde se desplegará nuestra API a la que se le podrán hacer requests sobre nuestro modelo entrenado y guardado previamente.

- `deployment`

    Contiene lo necesario para crear la imagen y contenedor como el Dockerfile, la lógica de la API que haremos uso (los endpoint a los que conectaremos o pediremos informacion sobre el modelo) y por último las librerías y sus versiones correspondientes que serán necesarias para la app alojada en ese contenedor en el requirements.

- `devops`

    Inicialmente durante la etapa inicial del proyecto se creó un entorno virtual para poder empezar a realizar las primeras pruebas y que los test pasaban correctamente en local antes de subirlo y desplegarlo en otro entorno.
