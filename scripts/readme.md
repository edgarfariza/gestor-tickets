# Gestión de Tickets: Proyecto de Sistemas y Programación

Este repositorio contiene las herramientas que he desarrollado para administrar una base de datos de soporte técnico. El proyecto combina el uso de bases de datos relacionales, scripts de automatización en Bash y programación interactiva en Python.

## Descripción de los Scripts

### 1. backup_tickets.sh (Bash)
Este script se encarga de la seguridad de la información.
* Realiza una copia de seguridad automática de toda la base de datos (mysqldump).
* Guarda los archivos organizados por fecha en la carpeta de backups.
* Permite recuperar toda la información en caso de fallo del sistema.

### 2. reporte_diario.sh (Bash)
Este script genera un análisis rápido del estado de las incidencias.
* Muestra el número total de tickets según su estado (resuelto o pendiente).
* Desglosa la carga de trabajo que tiene asignada cada técnico registrado.
* Utiliza comandos de MySQL integrados directamente en la terminal de Linux.

### 3. crear_ticket.py (Python)
Este programa permite la interacción con la base de datos de forma guiada.
* Muestra listas de usuarios y categorías existentes para evitar errores de selección.
* Solicita los datos del problema (asunto y descripción) a través del teclado.
* Implementa parámetros seguros para evitar ataques de inyección SQL.

## Automatización del Sistema (Cron)

He configurado el sistema operativo Linux para que ejecute estas tareas de forma automática mediante el servicio Crontab:

* **Copia de seguridad:** Programada diariamente a las 03:00 AM para asegurar los datos.
* **Reporte de estado:** Programado todos los lunes a las 08:00 AM para revisión semanal.

> **Configuración en Crontab:**
> 00 03 * * * /home/edgar/proyectos/gestor_tickets/scripts/backup_tickets.sh

---
*Este proyecto demuestra la integración de SQL, Bash y Python en un entorno real de administración de sistemas y desarrollo de software.*
