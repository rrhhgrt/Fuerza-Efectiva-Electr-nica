import streamlit as st
from datetime import datetime

# Configuración de la página web
st.set_page_config(
    page_title="Registro de Personal - Sistema Policial",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ Registro de Armas y Equipamiento Policial")
st.markdown("---")

# Pantalla de doble validación de Cédula
st.subheader("Identificación del Efectivo")
col1, col2 = st.columns(2)

with col1:
    cedula_1 = st.text_input("Ingrese su Número de Cédula", type="default")
with col2:
    cedula_2 = st.text_input("Reingrese su Cédula para confirmar", type="default")

# Botón para continuar al formulario si las cédulas coinciden
if cedula_1 and cedula_2:
    if cedula_1 != cedula_2:
        st.error("⚠️ Las cédulas no coinciden. Por favor, verifique e intente nuevamente.")
    else:
        st.success(f"Cédula verificada correctamente: **{cedula_1}**")
        st.markdown("---")
        
        # Formulario principal estandarizado con opciones de selección
        st.subheader("Formulario de Dotación")
        
        with st.form("form_registro_policial"):
            nombre = st.text_input("Nombre y Apellido Completo")
            
            grado = st.selectbox(
                "Grado",
                ["Seleccione...", "Agente", "Cabo", "Sargento", "Oficial Sub Ayudante", "Oficial Ayudante", "Oficial Principal", "Comisario"]
            )
            
            genero = st.selectbox(
                "Género",
                ["Seleccione...", "Masculino", "Femenino", "Otro"]
            )
            
            arma = st.selectbox(
                "Tipo y Marca de Arma de Dotación",
                ["Seleccione...", "Pistola Glock 17", "Pistola Glock 19", "Pistola Bersa Thunder", "Pistola Browning", "Otra"]
            )
            
            chaleco = st.selectbox(
                "Marca de Chaleco Balístico",
                ["Seleccione...", "Marca A (Nivel IIIA)", "Marca B (Nivel II)", "Otra"]
            )
            
            municiones = st.number_input("Cantidad de Municiones Asignadas", min_value=0, max_value=100, value=15)
            
            direccion = st.text_input("Dirección de Domicilio")
            telefono = st.text_input("Número de Teléfono / Celular")
            
            foto_cedula = st.file_uploader("Adjuntar Foto de la Cédula de Identidad", type=["jpg", "jpeg", "png"])
            
            enviar = st.form_submit_button("Enviar Registro")
            
            if enviar:
                if nombre == "" or grado == "Seleccione..." or arma == "Seleccione..." or not foto_cedula:
                    st.error("Por favor, complete todos los campos obligatorios y adjunte la foto.")
                else:
                    # Aquí es donde el sistema guardará los datos en la nube en los siguientes pasos
                    st.success("¡Registro enviado con éxito! Quedará pendiente de aprobación por el administrador.")
                    st.balloons()
else:
    st.info("ℹ️ Para comenzar a llenar el formulario, ingrese su número de cédula en ambos campos para confirmar su identidad.")
