import cv2

def iniciar_camara():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("No se pudo abrir la cámara")
        return
        
    print("Presionar tecla 'q' para cerrar")
    
    nombre_ventana = 'Cámara en Vivo'
    cv2.namedWindow(nombre_ventana, cv2.WINDOW_AUTOSIZE)
    
    while True:
        retornar, frame = cap.read()
        
        if not retornar: 
            print('Error al recibir el frame')
            break
            
        cv2.imshow(nombre_ventana, frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.getWindowProperty(nombre_ventana, cv2.WND_PROP_VISIBLE) < 1:
            break
            
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    iniciar_camara()