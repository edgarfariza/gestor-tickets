# Gestor de Tickets 

Este proyecto es un sistema de soporte técnico para gestionar incidencias. Está diseñado para centralizar el reporte de errores, asignarlos a técnicos especializados y controlar su resolución mediante prioridades.

## Funcionamiento General
El sistema permite registrar **Usuarios** que abren **Tickets** de soporte. Cada ticket se clasifica en una **Categoría** (Software, Hardware, etc.) y puede ser asignado a un **Técnico** específico. 

* **Flujo:** El usuario crea el ticket → Se asigna prioridad → El técnico cambia el estado a "Resuelto".
* **Control:** El uso de tipos `ENUM` en la base de datos asegura que los estados y prioridades sean siempre consistentes.

## Tecnologías Implementadas
* **Motor de Base de Datos:** MySQL 8.0.
* **Sistema Operativo:** Servidor Linux (Ubuntu) para el alojamiento del motor.
* **Gestión de Datos:** DBeaver (Cliente universal de DB).
* **Arquitectura:** Modelo Relacional de 4 tablas con integridad referencial (Foreign Keys).

##  Estructura del Proyecto
* `/database`: Contiene el `DUMP` SQL para replicar la base de datos.
* `/database` : Diagrama Entidad-Relación (ER) con la lógica del diseño.
