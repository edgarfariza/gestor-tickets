#!/bin/bash

# Configuración
FECHA=$(date +%Y-%m-%d_%H-%M)
DESTINO="../database/backups"
mkdir -p $DESTINO

echo "--- Iniciando mantenimiento del Gestor de Tickets ---"

# 1. Hacer el Backup (Sistemas)
mysqldump -u edgar -p gestor_tickets > $DESTINO/backup_$FECHA.sql
echo "Backup guardado en: $DESTINO/backup_$FECHA.sql"

# 2. Reporte rápido (Consulta SQL desde Bash)
echo "Estado actual de los tickets:"
mysql -u edgar -p -e "USE gestor_tickets; SELECT state, COUNT(*) FROM tickets GROUP BY state;"
