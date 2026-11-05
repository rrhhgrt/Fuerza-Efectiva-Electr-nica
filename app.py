import streamlit as st
from datetime import datetime

# Configuración de la página web
st.set_page_config(
    page_title="Ficha Personal - Jefatura de Policía de Montevideo",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ Jefatura de Policía de Montevideo")
st.subheader("Ficha Personal y de Dotación")
st.markdown("---")

# Pantalla de doble validación de Cédula (Seguridad inicial)
st.subheader("1. Validación de Identidad")
col1, col2 = st.columns(2)

with col1:
    cedula_1 = st.text_input("Ingrese su Cédula de Identidad")
with col2:
    cedula_2 = st.text_input("Reingrese su Cédula para confirmar")

# Validación de cédulas
if cedula_1 and cedula_2:
    if cedula_1 != cedula_2:
        st.error("⚠️ Las cédulas no coinciden. Por favor, verifique e intente nuevamente.")
    else:
        st.success(f"Cédula verificada correctamente: **{cedula_1}**")
        st.markdown("---")
        
        # Formulario principal basado exactamente en la ficha de papel
        with st.form("form_ficha_policial", clear_on_submit=True):
            
            # --- SECCIÓN 2: DATOS PERSONALES ---
            st.subheader("2. Datos Personales")
            apellidos = st.text_input("Apellidos")
            nombres = st.text_input("Nombres")
            autogenerado = st.text_input("Autogenerado")
            cred_civica = st.text_input("Credencial Cívica (Número y Serie)")
            estado_civil = st.selectbox("Estado Civil", ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
            
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                fecha_nac = st.text_input("Fecha de Nacimiento (DD/MM/AAAA)")
            with col_f2:
                lugar_nac = st.text_input("Lugar de Nacimiento (Ciudad / Departamento)")
                
            domicilio = st.text_input("Domicilio (Calle, N°, Apto, Asentamiento)")
            entre_calles = st.text_input("Entre Calles")
            localidad = st.text_input("Ciudad o Localidad")
            departamento = st.text_input("Departamento", value="Montevideo")
            
            telefono = st.text_input("Número de Teléfono / Celular")
            tel_emergencia = st.text_input("Teléfono de Emergencia")
            correo = st.text_input("Correo Electrónico / Zimbra")
            
            st.markdown("---")
            
            # --- SECCIÓN 3: DATOS FUNCIONALES Y DOTACIÓN ---
            st.subheader("3. Datos Funcionales y Dotación")
            
            cargo = st.selectbox(
                "Cargo / Grado",
                ["Agente", "Cabo", "Sargento", "Oficial Sub Ayudante", "Oficial Ayudante", "Oficial Principal", "Comisario"]
            )
            chapa = st.text_input("Número de Chapa")
            legajo = st.text_input("Número de Legajo")
            funcion = st.text_input("Función que Desempeña (Ej. Judiciales)")
            
            st.markdown("#### 🔫 Armamento")
            marca_arma = st.selectbox("Marca de Pistola", ["Glock", "Bersa Thunder", "Browning", "Otra"])
            num_arma = st.text_input("Número de Pistola")
            cant_cargadores = st.number_input("Cantidad de Cargadores", min_value=0, value=3)
            cant_municiones = st.number_input("Cantidad de Municiones", min_value=0, value=15)
            
            st.markdown("#### 🛡️ Chaleco Balístico")
            marca_chaleco = st.text_input("Marca de Chaleco Balístico (Ej. MC-CONFORT - IIIA)")
            num_chaleco = st.text_input("Número de Chaleco Balístico")
            venc_chaleco = st.text_input("Año y Mes de Vencimiento del Chaleco (Ej. Abril/2028)")
            talle_chaleco = st.selectbox("Talle de Chaleco Balístico", ["S", "M", "L", "XL", "XXL"])
            
            st.markdown("---")
            
            # --- SECCIÓN 4: TALLES DE UNIFORME ---
            st.subheader("4. Talles de Uniforme e Indumentaria")
            
            col_t1, col_t2, col_t3 = st.columns(3)
            with col_t1:
                t_campera = st.selectbox("Talle Camperas", ["S", "M", "L", "XL", "XXL"], index=1)
                t_buzo = st.selectbox("Talle Buzos", ["S", "M", "L", "XL", "XXL"], index=1)
            with col_t2:
                t_camisa_c = st.selectbox("Talle Camisa M/Corta", ["S", "M", "L", "XL", "XXL"], index=1)
                t_camisa_l = st.selectbox("Talle Camisa M/Larga", ["S", "M", "L", "XL", "XXL"], index=1)
            with col_t3:
                t_pantalon = st.selectbox("Talle Pantalón", ["S", "M", "L", "XL", "XXL"], index=1)
                t_kepi = st.selectbox("Talle Kepi", ["S", "M", "L", "XL"], index=1)
                
            t_botas = st.text_input("Talle de Botas (Ej. 42)")
            
            st.markdown("---")
            
            # --- SECCIÓN 5: SALUD Y EDUCACIÓN ---
            st.subheader("5. Salud y Educación")
            nivel_educativo = st.selectbox("Nivel Educativo", ["Primaria", "Ciclo Básico", "Bachillerato / Secundaria", "Terciaria / Universitaria"])
            enfermedad_cronica = st.text_input("¿Posee alguna enfermedad crónica? ¿Cuál? (Si no posee, escriba No)")
            carnet_salud = st.selectbox("¿Posee Carné de Salud vigente?", ["Sí", "No"])
            
            st.markdown("---")
            
            # --- SECCIÓN 6: DOCUMENTACIÓN ---
            st.subheader("6. Documentación")
            foto_cedula = st.file_uploader("Adjuntar Foto de la Cédula o Documentos", type=["jpg", "jpeg", "png"])
            
            enviar = st.form_submit_button("Enviar Ficha de Registro")
            
            if enviar:
                if not apellidos or not nombres or not chapa or not foto_cedula:
                    st.error("Por favor, complete los campos obligatorios (Apellidos, Nombres, Chapa y la Foto).")
                else:
                    st.success("¡Ficha enviada con éxito! Quedará pendiente de aprobación por la administración.")
                    st.balloons()
else:
    st.info("ℹ️ Para comenzar a llenar la ficha, ingrese su número de cédula en ambos campos para confirmar su identidad.")
