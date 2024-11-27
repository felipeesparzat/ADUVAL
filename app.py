import tkinter as tk
from tkinter import messagebox

# Función para guardar los valores ingresados
def guardar_valores():
    valor_utm = entry_utm.get()  # Obtener valor de UTM
    tipo_cambio = entry_tipo_cambio.get()  # Obtener valor de Tipo de Cambio
    
    # Verificar que ambos campos están llenos
    if valor_utm and tipo_cambio:
        # Aquí podrías guardar los valores en una base de datos o archivo, si lo deseas
        messagebox.showinfo("Éxito", "Valores guardados con éxito")
        entry_utm.delete(0, tk.END)  # Limpiar campo UTM
        entry_tipo_cambio.delete(0, tk.END)  # Limpiar campo Tipo de Cambio
    else:
        messagebox.showerror("Error", "Por favor complete ambos campos")

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
btn_guardar = tk.Button(root, text="Guardar", command=guardar_valores)
btn_guardar.pack(pady=20)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()


    # Guardar los datos en el archivo CSV
    df.to_csv(archivo_csv, index=False)

    # Confirmación de guardado
    st.write(f"¡Opción '{opcion}' guardada correctamente en {archivo_csv}!")
