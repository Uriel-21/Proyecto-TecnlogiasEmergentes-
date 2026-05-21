import qrcode
import os
from bd_config import Conexion

def generar_qrs_desde_bd():

    carpeta_destino = "qrs_vehiculos"
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    print("Conectando....")
    conexion = Conexion()
    
    if conexion:
        try:
            cursor = conexion.cursor()
        
            query = "SELECT idAuto, placa FROM datos_auto"
            cursor.execute(query)
            vehiculos = cursor.fetchall()
            
            if len(vehiculos) == 0:
                print("Tabla vacía")
                return
            
            print(f"Se encontraron {len(vehiculos)} vehículos registrados.")
            print("Generando códigos QR...")
            
            for vehiculo in vehiculos:
                id_auto = vehiculo[0] 
                placa = vehiculo[1]   
                
                imagen_qr = qrcode.make(id_auto)
                
                nombre_archivo = f"{carpeta_destino}/{placa}_{id_auto}.png"
                imagen_qr.save(nombre_archivo)
                
                print(f"Generado: {nombre_archivo}")
                
        except Exception as e:
            print(f"Error en la base de datos: {e}")
            
        finally:
            cursor.close()
            conexion.close()
            print("Proceso terminado.")
    else:
        print("No se pudo conectar a la BD.")

if __name__ == "__main__":
    generar_qrs_desde_bd()