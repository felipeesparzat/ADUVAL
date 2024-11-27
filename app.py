import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Función para guardar los valores y exportarlos como PDF
def guardar_valores():
    valor_utm = entry_utm.get()  # Obtener valor de UTM
    tipo_cambio = entry_tipo_cambio.get()  # Obtener valor de Tipo de Cambio
    
    # Verificar que ambos campos están llenos
    if valor_utm and tipo_cambio:
        # Aquí se genera el archivo PDF
        exportar_a_pdf(valor_utm, tipo_cambio)
        
        # Mostrar mensaje de éxito
        messagebox.showinfo("Éxito", "Valores exportados a PDF con éxito")
        
        # Limpiar los campos
        entry_utm.delete(0, tk.END)
        entry_tipo_cambio.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Por favor complete ambos campos")

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

# Crear la ventana principal
root = tk.Tk()
root.title("Formulario de Valores")

# Configurar el tamaño de la ventana
root.geometry("300x200")

# Etiqueta y campo de texto para el valor de UTM
label_utm = tk.Label(root, text="Valor de UTM:")
label_utm.pack(pady=10)

entry_utm = tk.Entry(root)
entry_utm.pack(pady=5)

# Etiqueta y campo de texto para el valor de Tipo de Cambio
label_tipo_cambio = tk.Label(root, text="Valor de Tipo de Cambio:")
label_tipo_cambio.pack(pady=10)

entry_tipo_cambio = tk.Entry(root)
entry_tipo_cambio.pack(pady=5)

# Botón para guardar los valores
btn_guardar = tk.Button(root, text="Exportar a PDF", command=guardar_valores)
btn_guardar.pack(pady=20)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()

    # Guardar los datos en el archivo CSV
    df.to_csv(archivo_csv, index=False)

    # Confirmación de guardado
    st.write(f"¡Opción '{opcion}' guardada correctamente en {archivo_csv}!")
