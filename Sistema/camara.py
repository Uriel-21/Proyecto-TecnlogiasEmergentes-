import cv2

# 1. Inicializar la captura de video
# El argumento '0' indica que usaremos la cámara por defecto de la laptop/PC.
cap = cv2.VideoCapture(0)

# Verificamos si la cámara se abrió correctamente
if not cap.isOpened():
    print("Error: No se pudo acceder a la cámara.")
    exit()

print("Presiona la tecla 'q' para cerrar la ventana.")

while True:
    # 2. Capturar frame a frame
    # 'ret' es un booleano (True/False) que indica si el frame se leyó bien.
    # 'frame' es la imagen capturada en ese instante.
    ret, frame = cap.read()

    if not ret:
        print("Error al recibir el frame. Finalizando...")
        break

    # 3. Mostrar el resultado en una ventana
    cv2.imshow('Cámara en Vivo', frame)

    # 4. Condición de salida
    # Espera 1 milisegundo a que se presione una tecla. 
    # Si la tecla es 'q' (código ASCII), rompe el ciclo.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 5. Liberar recursos
cap.release()        # Libera el hardware de la cámara
cv2.destroyAllWindows() # Cierra todas las ventanas de OpenCV