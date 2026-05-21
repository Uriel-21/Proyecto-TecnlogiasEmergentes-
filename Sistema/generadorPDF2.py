import os 
from datetime import datetime
from fpdf import FPDF

def crearMulta(placa, marca, modelo, dueño, motivo, color):
    
    carpetaDestino = "reportes"
    if not os.path.exists(carpetaDestino):
        os.makedirs(carpetaDestino)
    
    pdf = FPDF(orientation='P', unit='mm', format=(58,100))
    pdf.set_margins(left=3, top=5, right=3) 
    pdf.set_auto_page_break(auto=True, margin=5)   
    
    pdf.add_page()
    
    pdf.set_font("helvetica", "B", 10)
    pdf.multi_cell(52, 5, "SISTEMA \nREPORTE DE INFRACCION", align="C", new_x="LMARGIN", new_y="NEXT")
    
    pdf.ln(3)
    
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pdf.set_font("helvetica", "I", 7)
    pdf.multi_cell(52, 4, f"Fecha: {fecha_actual}", align="C", new_x="LMARGIN", new_y="NEXT")
    
    pdf.ln(5)
    
    pdf.set_font("helvetica", "", 8)
    pdf.multi_cell(52, 4, f"Propietario: {dueño}", new_x="LMARGIN", new_y="NEXT")
    pdf.multi_cell(52, 4, f"Vehiculo: {marca} {modelo}", new_x="LMARGIN", new_y="NEXT")
    pdf.multi_cell(52, 4, f"Placas: {placa}", new_x="LMARGIN", new_y="NEXT")
    pdf.multi_cell(52, 4, f"Color: {color}", new_x="LMARGIN", new_y="NEXT")
    
    pdf.ln(5)
    
    pdf.set_font("helvetica", "B", 9)
    pdf.set_text_color(220, 53, 69) 
    pdf.multi_cell(52, 4, f"MOTIVO:\n{motivo}", new_x="LMARGIN", new_y="NEXT")
    
    hora_archivo = datetime.now().strftime("%H%M%S")
    nombre_archivo = f"{carpetaDestino}/Alerta_{placa}_{hora_archivo}.pdf"
    
    pdf.output(nombre_archivo)
    print(f" Reporte generado: {nombre_archivo}")
    
    return nombre_archivo