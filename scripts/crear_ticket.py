import mysql.connector
from mysql.connector import Error

def ejecutar_app():
    conexion = None
    try:
        # 1. Configuración de la conexión
        # Añado ssl_disabled para evitar problemas de compatibilidad entre Python y Ubuntu.
        conexion = mysql.connector.connect(
            host='localhost',
            user='edgar',  # MI USUARIO DE EJEMPLO, SUSTITUIR POR EL PROPIO
            password='1234',  # MI CONTRASEÑA DE EJEMPLO, SUSTITUIR POR LA PROPIA
            database='gestor_tickets',
            ssl_disabled=True       
        )

        if conexion.is_connected():
            cursor = conexion.cursor()
            
            print("\n" + "="*30)
            print("  NUEVO TICKET DE SOPORTE")
            print("="*30)
            
            # 2. Pedir datos al usuario
            titulo = input("Asunto del problema: ")
            descripcion = input("Descripción detallada: ")
            
            # 3. Sentencia SQL (usamos %s por seguridad/inyección SQL)
            sql = "INSERT INTO tickets (title, description, state, priority) VALUES (%s, %s, 'no', 'medium')"
            valores = (titulo, descripcion)

            # 4. Ejecutar y guardar
            cursor.execute(sql, valores)
            conexion.commit()
            
            print(f"\n ¡Éxito! Ticket creado con ID: {cursor.lastrowid}")
            print("="*30 + "\n")

    except Error as e:
        print(f"\n Error de base de datos: {e}")
    
    except KeyboardInterrupt:
        print("\n\n Saliendo del programa...")

    finally:
        # 5. Cerrar siempre la conexión
        if conexion and conexion.is_connected():
            cursor.close()
            conexion.close()
            print(" Conexión cerrada de forma segura.")

if __name__ == "__main__":
    ejecutar_app()
