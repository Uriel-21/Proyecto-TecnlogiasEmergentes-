import cv2
import time
from lectorqr import extreaerQR
from bd_config import Conexion, BuscarCarroQR
# from generarPDF import crearMulta
from generadorPDF2 import crearMulta
from impresora import imprimirReporte



def procesarReporte(placa, marca, modelo, dueño, motivo, color):
    
    print(f"Procesando reporte para la placa: {placa}.....")
    
    rutaReporte = crearMulta(placa, marca, modelo, dueño, motivo, color)
    
    imprimirReporte(rutaReporte)
    
def iniciar_camara():
    
    conexion = Conexion()
    if conexion is None: return 
    
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("No se pudo abrir la cámara")
        return
        
    print("Presionar tecla 'q' para cerrar")
    
    ultimo_qr_leido = ""
    tiempo_ultima_lectura = 0 
    segundos_espera = 5
    
    nombre_ventana = 'Cámara en Vivo'
    cv2.namedWindow(nombre_ventana, cv2.WINDOW_AUTOSIZE)
    
    while True:
        retornar, frame = cap.read()
        if not retornar: break
            
        id_detectado = extreaerQR(frame)
        
        if id_detectado is not None:
            tiempo_actual = time.time()
            
            if id_detectado != ultimo_qr_leido or (tiempo_actual - tiempo_ultima_lectura) > segundos_espera:
                print(f"\n Procesando ID: {id_detectado}...")
                
                ultimo_qr_leido = id_detectado
                tiempo_ultima_lectura = tiempo_actual

                datos_del_carro = BuscarCarroQR(conexion, id_detectado)
                
                if datos_del_carro:
                    placa, marca, modelo, color, estatus, dueño, verificacion = datos_del_carro
                    
                    print(f" Encontrado: {marca} {modelo} {color} ({placa}) - Dueño: {dueño}")
                    
                    if estatus == 'LIMPIO':
                        print("Vehiculo al corriente y limpio")
                    elif estatus == 'ROBO':
                        print("¡ALERTA! Vehículo Robado")
                        # crearMulta(placa, marca, modelo, dueño, 'VEHICULO CON REPORTE DE ROBO', color)
                        procesarReporte(placa, marca, modelo, dueño, motivoInfraccion, color)
                        
                    elif estatus == 'MULTAS':
                        motivoInfraccion = "VEHICULO CON MULTAS PENDIENTES"
                        print("AVISO: Multas pendientes")
                        if verificacion == 0 or verificacion == False:
                            motivoInfraccion += " Y VEHICULO SIN VERIFICACIÓN"
                            
                            # crearMulta(placa, marca, modelo, dueño, motivoInfraccion, color)
                            procesarReporte(placa, marca, modelo, dueño, motivoInfraccion, color)
                       
                else:
                    print("ALERTA: QR no registrado.")

        cv2.imshow(nombre_ventana, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    conexion.close()
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    iniciar_camara()
    
    
def procesarReporte(placa, marca, modelo, dueño, motivo, color):
    
    print(f"Procesando reporte para la placa: {placa}.....")
    
    rutaReporte = crearMulta(placa, marca, modelo, dueño, motivo, color)
    
    imprimirReporte(rutaReporte)