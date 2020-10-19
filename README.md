# Proyecto final POO

## Documentación:

Para poder utilizar el sistema de gestión de pedido es necesario tener un super usuario quien será la persona encargada de gestionar todos los usuarios.

Para ello es necesario crear uno o mas super usuarios esto con la documentación oficial de Django.

Luego de ello el o los super usuarios podrán iniciar sesión a través de este enlace: 

	/admin

Ahí podrán empezar a crear los usuarios para que así estos sean entregados solo al personal autorizado.

Usuarios:

Los usuarios una vez creados pueden iniciar sesión a través de este enlace: 

	/login

Una vez que se inicie sesión se encontrar con una interfaz donde podrá encontrar la interfaz con todos los datos del sistema separado por secciones.

Dentro de la pagina de inicio habrá varias urls con distintas funciones.

	/agregar = agregar nuevos productos

	/borrar (Requiere pasar datos como el ID) = borrar producto

	/editar (Requiere pasar datos como el ID) =  edita los datos de un producto

	/vender = vender productos

	/logout = cerrar sesión