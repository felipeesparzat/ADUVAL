import subprocess
import streamlit as st

# Función para ejecutar el script
def ejecutar_script():
    try:
        # Ejecutar el script ./data/ivutmytcv
        result = subprocess.check_output(["./data/ivutmytcv"], text=True)
        st.text_area("Salida del script:", result)
        st.success("Script ejecutado con éxito.")
    except subprocess.CalledProcessError as e:
        st.error(f"Error al ejecutar el script: {e.output}")
    except FileNotFoundError:
        st.error("El archivo './data/ivutmytcv' no se encuentra o no es ejecutable.")

# Crear la interfaz de Streamlit
st.title("Ejecutar Script Externo")

# Botón para ejecutar el script
if st.button("Ejecutar Script"):
    ejecutar_script()
