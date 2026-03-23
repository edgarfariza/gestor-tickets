import mysql.connector
from mysql.connector import Error

def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='edgar',      # CAMBIA ESTO
            password='1234',  # CAMBIA ESTO
            database='gestor_tickets'
        )
        if conexion.is_connected():
            return conexion
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

def insertar_ticket():
    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        
        print("\n--- 🎫 NUEVO TICKET DE SOPORTE ---")
        titulo = input("Asunto del problema: ")
        descripcion = input("Descripción detallada: ")
        
        # SQL con placeholders (%s) para evitar inyección SQL (Seguridad)
        sql = "INSERT INTO tickets (title, description, state, priority) VALUES (%s, %s, 'no', 'medium')"
        valores = (titulo, descripcion)

        try:
            cursor.execute(sql, valores)
            conexion.commit()
            print(f"\nTicket creado con éxito. ID: {cursor.lastrowid}")
        except Error as e:
            print(f"Error al insertar: {e}")
        finally:
            cursor.close()
            conexion.close()

if __name__ == "__main__":
    insertar_ticket()
