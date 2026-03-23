#!/bin/bash

# --- Configuración de conexión ---
USER="edgar"
DATABASE="gestor_tickets"

# Colores para que el reporte se vea pro en la terminal
VERDE='\033[0;32m'
ROJO='\033[0;31m'
AZUL='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${AZUL}=========================================="
echo -e "   REPORTE DIARIO: GESTOR DE TICKETS   "
echo -e "==========================================${NC}"
echo "Fecha: $(date +'%d/%m/%Y %H:%M')"
echo ""

# 1. Resumen de tickets por Estado
echo -e "${VERDE}[+] Resumen de Estados:${NC}"
mysql -u $USER -p -e "USE $DATABASE; SELECT state as 'Estado', COUNT(*) as 'Total' FROM tickets GROUP BY state;" 

echo ""

# 2. Alerta de Tickets de Alta Prioridad No Resueltos
echo -e "${ROJO}[!] Tickets Críticos Pendientes (Prioridad High):${NC}"
mysql -u $USER -p -e "USE $DATABASE; SELECT id_ticket, title, created_at FROM tickets WHERE priority = 'high' AND state = 'no';"

echo ""

# 3. Carga de trabajo por Técnico
echo -e "${VERDE}[+] Tickets asignados por Técnico:${NC}"
mysql -u $USER -p -e "USE $DATABASE; 
SELECT t.name as 'Técnico', COUNT(tk.id_ticket) as 'Tickets Asignados' 
FROM technicians t 
LEFT JOIN tickets tk ON t.id_tech = tk.id_tech 
GROUP BY t.name;"

echo -e "${AZUL}==========================================${NC}"
