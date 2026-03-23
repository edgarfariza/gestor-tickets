# Scripts de Automatización (Bash)

Esta carpeta contiene las herramientas de administración que he desarrollado para gestionar el sistema desde la terminal de **Linux**.

##  Scripts Incluidos

1. **`backup_tickets.sh`**: 
   * Realiza un volcado (`dump`) completo de la base de datos.
   * Organiza las copias por fecha en la carpeta `/database/backups`.
   * Garantiza que los datos estén seguros ante cualquier fallo del sistema.

2. **`reporte_diario.sh`**: 
   * Extrae métricas clave directamente de MySQL (tickets pendientes, carga por técnico y prioridades).
   * Muestra un resumen visual con colores en la terminal para una lectura rápida.

##  Automatización con Cron
Para profesionalizar el proyecto, he programado las tareas en el sistema **Crontab** de Linux para que se ejecuten automáticamente:

* **Backups:** Programados diariamente a las 03:00 AM para no interferir con el uso del sistema.
* **Reportes:** Generación automática de un estado de situación cada lunes a las 08:00 AM.

> **Configuración:** `00 03 * * * /ruta/al/script/backup_tickets.sh`

