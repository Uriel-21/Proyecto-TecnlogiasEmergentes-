from pyzbar.pyzbar import decode

def extreaerQR(frameImagen):
    codigos = decode(frameImagen)
    
    for codigo in codigos: 
        textoLimpio = codigo.data.decode('utf-8')
        return textoLimpio
    
    return None