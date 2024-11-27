import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class VUTMTC:
    # Función para exportar los valores a un archivo PDF
    def exportar_a_pdf(valor_utm, tipo_cambio):
        # Crear un archivo PDF
        archivo_pdf = "valores_exportados.pdf"
        
        # Crear un objeto canvas para el PDF
        c = canvas.Canvas(archivo_pdf, pagesize=letter)
        
        # Añadir texto al PDF
        c.setFont("Helvetica", 12)
        c.drawString(100, 750, f"Valor de UTM: {valor_utm}")
        c.drawString(100, 730, f"Valor de Tipo de Cambio: {tipo_cambio}")
        
        # Guardar el archivo PDF
        c.save()
        
        return archivo_pdf

    # Título de la aplicación
    st.title("Formulario de Valores")

    # Ingreso de valores a través de formularios
    valor_utm = st.text_input("Valor de UTM")
    tipo_cambio = st.text_input("Valor de Tipo de Cambio")

    # Botón para guardar los valores y exportarlos a PDF
    if st.button("Exportar a PDF"):
        if valor_utm and tipo_cambio:
            archivo_pdf = exportar_a_pdf(valor_utm, tipo_cambio)
            st.success("Valores exportados a PDF con éxito")
            
            # Opción para descargar el archivo PDF
            with open(archivo_pdf, "rb") as f:
                st.download_button(
                    label="Descargar PDF",
                    data=f,
                    file_name=archivo_pdf,
                    mime="application/pdf"
                )
        else:
            st.error("Por favor complete ambos campos")
