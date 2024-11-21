import streamlit as st

# Título de la aplicación
st.title("Desplegable de Sí y No")

# Desplegable con opciones "Sí" y "No"
opcion = st.selectbox("Elige una opción:", ["Sí", "No"])

# Mostrar la opción seleccionada
st.write(f"Has seleccionado: {opcion}")
