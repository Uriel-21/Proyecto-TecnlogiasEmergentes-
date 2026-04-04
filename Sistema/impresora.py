import subprocess

def imprimirReporte(rutaPDF):
    try:
        print(f"Realizando comunicación con la impresora para: {rutaPDF}...")
        
        subprocess.run(["lp", rutaPDF], check=True)
        
        print("Reporte impreso con exito")
        
    except subprocess.CalledProcessError as e:
        print(f"Ocurrio un error con el sistema de impresión: {e} ")
    except FileNotFoundError:
        print("Error no se encontro el sistema de impresión")