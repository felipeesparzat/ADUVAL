import streamlit as st
import os
import pandas as pd

# Título de la aplicación
st.title("Selecciona una Opción")

# Desplegable con opciones "Sí" y "No"
opcion = st.selectbox("Elige una opción:", ["Sí", "No"])

# Mostrar la opción seleccionada
st.write(f"Has seleccionado: {opcion}")

# Crear directorio si no existe
directorio = './datos/guardar_opciones'
if not os.path.exists(directorio):
    os.makedirs(directorio)

# Ruta del archivo CSV
archivo_csv = os.path.join(directorio, 'opciones_seleccionadas.csv')

# Botón de guardar
if st.button("Guardar"):
    # Crear o leer el archivo CSV
    if os.path.exists(archivo_csv):
        # Si el archivo ya existe, lo leemos
        df = pd.read_csv(archivo_csv)
    else:
        # Si no existe, creamos un DataFrame vacío
        df = pd.DataFrame(columns=["Opción"])

    # Añadir la nueva opción al DataFrame
    df = df.append({"Opción": opcion}, ignore_index=True)

    # Guardar los datos en el archivo CSV
    df.to_csv(archivo_csv, index=False)

    # Confirmación de guardado
    st.write(f"¡Opción '{opcion}' guardada correctamente en {archivo_csv}!")
