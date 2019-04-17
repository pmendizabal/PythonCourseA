"""
SQLite:
Es un sistema de gestion de BBDD relacional, escrito en C con codigo abierto, forma
parte integral del programa y se guarda como un unico fichero en host.
Ventajas:
Ocupa muy poco espacio en disco y memoria
Muy eficiente y rapido
Multiplataforma
Sin admon/configuracion
Dominio publico
Desventajas:
No admite clausulas anidades
No existen usuarios
Falta de clave foranea en modo consola

PASOS A SEGUIR PARA CONECTAR CON BBDD

1.-Abrir-crear conexion
2.-Crear puntero
3.-Ejecutar query(consulta) SQL
4.-Manejar resultados de la query
5.-Cerrar puntero
6.-Cerrar conexion