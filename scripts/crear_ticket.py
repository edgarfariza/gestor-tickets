import mysql.connector
from mysql.connector import Error

def ejecutar_app():
    conexion = None
    try:
        # 1. Configuración (añlado ssl_disabled para evitar problemas de compatibilidad entre versiones Python e Ubuntu).
        conexion = mysql.connector.connect(
            host='localhost',
            user='edgar',      # mi usuario de ejemplo
            password='1234',  # mi contraseña de ejemplo
            database='gestor_tickets',
            ssl_disabled=True       
        )

        if conexion.is_connected():
            cursor = conexion.cursor()
            
            print("\n" + "="*45)
            print("    SISTEMA DE GESTIÓN DE TICKETS PRO")
            print("="*45)

            # 2. Mostrar USUARIOS
            print("\n SELECCIONA UN USUARIO:")
            cursor.execute("SELECT id_user, name FROM users")
            for u in cursor.fetchall():
                print(f"  [{u[0]}] {u[1]}")
            id_cliente = input(" ID del usuario: ")

            # 3. Mostrar CATEGORÍAS 
            print("\n SELECCIONA UNA CATEGORÍA:")
            cursor.execute("SELECT id_category, name_category FROM categories")
            for c in cursor.fetchall():
                print(f"  [{c[0]}] {c[1]}")
            id_cat = input(" ID de la categoría: ")

            # 4. Datos del ticket
            print("\n DETALLES DEL PROBLEMA:")
            titulo = input(" Asunto: ")
            descripcion = input(" Descripción: ")
            
            # 5. SQL Completo con todas las Foreign Keys obligatorias
            sql = """
            INSERT INTO tickets (title, description, state, priority, id_user, id_category) 
            VALUES (%s, %s, 'no', 'medium', %s, %s)
            """
            valores = (titulo, descripcion, id_cliente, id_cat)

            # 6. Ejecutar y Guardar
            cursor.execute(sql, valores)
            conexion.commit()
            
            print(f"\n ¡Ticket '{titulo}' creado con éxito!")
            print(f" ID Asignado: {cursor.lastrowid}")
            print("="*45 + "\n")

    except Error as e:
        print(f"\n Error de base de datos: {e}")
    
    except KeyboardInterrupt:
        print("\n\n Saliendo...")

    finally:
        if conexion and conexion.is_connected():
            cursor.close()
            conexion.close()
            print(" Conexión cerrada de forma segura.")

if __name__ == "__main__":
    ejecutar_app()
