#Importamos la libreria para la conexión con la base de datos
import mysql.connector 
from mysql.connector import Error

# Funcion para hacer la conexion
def Conexion (): 
    try:
        # Datos de la conexion con la base de datos
        conexion = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='1234',
            database='BD_Proyecto' 
        )
        if conexion.is_connected(): 
            print ("conexión establecida")
            return conexion
    except Error as e: 
        print (f"Error al conectar a la base de datos: {e}")
        return None

Conexion()

def BuscarCarroQR(conexion, idDetectado):
    
    try: 
        cursor = conexion.cursor()
        query = "SELECT placa, marca, modelo, color, estatus_legar, dueño, verificacion FROM datos_auto WHERE idAuto = %s"
        cursor.execute(query, [idDetectado])
        
        datos = cursor.fetchone()
        cursor.close()
        
        return datos
        
    except Exception as e:
        print(f"Error al consultar la base de datos {e}")
        return None