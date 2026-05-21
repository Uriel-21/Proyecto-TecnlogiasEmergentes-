import os
from datetime import datetime
from fpdf import FPDF

def crearMulta(placa, marca, modelo, dueño, motivo, color):
    carpetaDestino = "reportes"
    if not os.path.exists(carpetaDestino):
        os.makedirs(carpetaDestino)
    
    pdf = FPDF(orientation='P', unit='mm', format='Letter')
    pdf.add_page()
    
    pdf.set_font("helvetica", "B", 18)
    pdf.cell(0, 15, "REPORTE DE INFRACCIÓN", border=False, align="C", new_x="LMARGIN", new_y="NEXT")

    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pdf.set_font("helvetica", "I", 10)
    pdf.cell(0, 10, f"Fecha de emisión: {fecha_actual}", align="R", new_x="LMARGIN", new_y="NEXT")
    
    pdf.ln(10) 
    
    pdf.set_font("helvetica", "", 12)
    pdf.cell(0, 10, f"Propietario Registrado: {dueño}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, f"Vehículo: {marca} {modelo}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, f"Placas: {placa}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, f"Color: {color}", new_x="LMARGIN", new_y="NEXT")
    
    pdf.ln(10)
    
    pdf.set_font("helvetica", "B", 14)
    pdf.set_text_color(220, 53, 69) 
    pdf.multi_cell(0, 10, f"MOTIVO DE LA DETENCIÓN: {motivo}")
    
    hora_archivo = datetime.now().strftime("%H%M%S")
    nombre_archivo = f"{carpetaDestino}/Alerta_{placa}_{hora_archivo}.pdf"
    
    pdf.output(nombre_archivo)
    print(f"Evidencia legal generada: {nombre_archivo}")
    
    return nombre_archivo
    