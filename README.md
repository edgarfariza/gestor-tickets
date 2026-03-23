# Sistema de Gestión de Tickets (Híbrido)

Proyecto desarrollado para la gestión de incidencias técnicas, integrando administración de sistemas Linux y programación de aplicaciones. Realizado en un entorno Ubuntu mediante conexion SSH (Warp para trabajo, DBeaver para bases de datos.)

## Tecnologías Utilizadas
* **Base de Datos:** MySQL (Diseño relacional con claves foráneas).
* **Sistemas:** Bash Scripting (Ubuntu/Linux).
* **Programación:** Python 3.12 (Conexión a base de datos).

## Estructura del Proyecto
* **/database**: Contiene el esquema SQL y los datos iniciales de prueba.
* **/scripts**: Incluye los scripts de Bash para backups y reportes, y la aplicación Python para insertar tickets.

## Funcionalidades Clave
1. **Automatización:** Backups diarios y reportes semanales programados mediante Crontab.
2. **Interfaz Interactiva:** Programa en Python para añadir tickets consultando usuarios y categorías en tiempo real.
3. **Seguridad:** Control de integridad de datos y prevención de inyección SQL.

## Instalación Rápida
1. Importar el archivo SQL en MySQL/DBeaver.
2. Configurar usuario y contraseña en los archivos de la carpeta /scripts.
3. Instalar el conector de Python: `sudo apt install python3-mysql.connector`.

---
*Desarrollado como proyecto de integración de conocimientos de 1º de DAM.*
