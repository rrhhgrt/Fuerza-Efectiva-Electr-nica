import streamlit as st

# Configuración de la página web
st.set_page_config(
    page_title="Ficha Personal - Jefatura de Policía de Montevideo",
    page_icon="🛡️",
    layout="centered"
)

# Estilo CSS: Todo en mayúsculas por defecto, EXCEPTO el campo del correo Zimbra
st.markdown("""
    <style>
    input, textarea {
        text-transform: uppercase;
    }
    /* Excepción para que el campo de Zimbra se vea siempre en minúsculas */
    div[data-testid="stTextInput"] input[aria-label="Usuario (lo que antecede)"] {
        text-transform: lowercase !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ Jefatura de Policía de Montevideo")
st.subheader("Ficha Personal y de Dotación")
st.markdown("---")

# Pantalla de doble validación de Cédula (Seguridad inicial: Exactamente 8 dígitos numéricos)
st.subheader("1. Validación de Identidad")
col1, col2 = st.columns(2)

with col1:
    cedula_1 = st.text_input("Ingrese su Cédula de Identidad (8 dígitos)", max_chars=8).strip()
with col2:
    cedula_2 = st.text_input("Reingrese su Cédula para confirmar", max_chars=8).strip()

# Validar que ambas estén completas y tengan exactamente 8 dígitos numéricos
cedula_valida = False

if cedula_1 or cedula_2:
    if not (cedula_1.isdigit() and cedula_2.isdigit() and len(cedula_1) == 8 and len(cedula_2) == 8):
        st.warning("⚠️ La cédula debe contener exclusivamente **8 dígitos numéricos** en ambos campos.")
    elif cedula_1 != cedula_2:
        st.error("⚠️ Las cédulas no coinciden. Por favor, verifique e intente nuevamente.")
    else:
        cedula_valida = True
        st.success(f"Cédula verificada correctamente: **{cedula_1}**")
        st.markdown("---")

# El formulario completo solo se despliega si la cédula es correcta (8 dígitos y coinciden)
if cedula_valida:
    with st.form("form_ficha_policial", clear_on_submit=True):
        
        # --- SECCIÓN 2: DATOS PERSONALES ---
        st.subheader("2. Datos Personales")
        apellidos = st.text_input("Apellidos").upper()
        nombres = st.text_input("Nombres").upper()
        autogenerado = st.text_input("Autogenerado").upper()
        
        col_cr1, col_cr2 = st.columns(2)
        with col_cr1:
            cred_civica = st.text_input("Credencial Cívica (Número y Serie)").upper()
        with col_cr2:
            depto_credencial = st.text_input("Departamento de la Credencial Cívica").upper()
            
        estado_civil = st.selectbox("Estado Civil", ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
        
        st.text("Fecha de Nacimiento:")
        col_fn1, col_fn2, col_fn3 = st.columns(3)
        with col_fn1:
            dia_nac = st.selectbox("Día Nac.", [str(i).zfill(2) for i in range(1, 32)])
        with col_fn2:
            mes_nac = st.selectbox("Mes Nac.", [str(i).zfill(2) for i in range(1, 13)])
        with col_fn3:
            anio_nac = st.text_input("Año Nac. (AAAA)", value="1990").upper()
            
        lugar_nac = st.text_input("Lugar de Nacimiento (Ciudad / Departamento)").upper()
            
        domicilio = st.text_input("Domicilio (Calle, N°, Apto, Asentamiento)").upper()
        entre_calles = st.text_input("Entre Calles").upper()
        localidad = st.text_input("Ciudad o Localidad").upper()
        departamento = st.text_input("Departamento", value="MONTEVIDEO").upper()
        
        # Campos estrictamente numéricos para teléfonos
        telefono = st.text_input("Número de Teléfono / Celular (Solo números)", placeholder="EJ. 099123456").strip()
        tel_emergencia = st.text_input("Teléfono de Emergencia (Solo números)", placeholder="EJ. 099123456").strip()
        
        # Correo Zimbra en minúsculas
        st.text("Correo Zimbra:")
        col_z1, col_z2 = st.columns([2, 3])
        with col_z1:
            correo_usuario = st.text_input("Usuario (lo que antecede)", placeholder="nombre.apellido").strip().lower()
        with col_z2:
            st.markdown("<br><span style='text-transform: lowercase;'><b>@minterior.gub.uy</b></span>", unsafe_allow_html=True)
        
        st.markdown("---")
        
        # --- SECCIÓN 3: DATOS FUNCIONALES Y DOTACIÓN ---
        st.subheader("3. Datos Funcionales y Dotación")
        
        cargo = st.selectbox(
            "Grado",
            ["Seleccione...", "Agente", "Cabo", "Sargento", "Sub Oficial Mayor", "Oficial Ayudante", "Oficial Principal", "Sub Comisario", "Comisario"]
        )
        legajo = st.text_input("Número de Legajo (Solo números)").strip()
        
        st.markdown("#### 🔫 Armamento")
        marca_arma = st.selectbox("Marca de Pistola", ["Seleccione...", "HK", "Glock"])
        num_arma = st.text_input("Número de Pistola (Solo números)").strip()
        cant_cargadores = st.number_input("Cantidad de Cargadores", min_value=0, value=3)
        cant_municiones = st.number_input("Cantidad de Municiones", min_value=0, value=15)
        
        st.markdown("#### 🛡️ Chaleco Balístico")
        marca_chaleco = st.selectbox("Marca de Chaleco Balístico", ["Seleccione...", "Kavro", "Marom Dolphin", "Xin Xing", "Caballero"])
        num_chaleco = st.text_input("Número de Chaleco Balístico (Solo números)").strip()
        
        anio_venc_chaleco = st.text_input("Año Vencimiento Chaleco (AAAA)", value="2028").upper()
            
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
            
        t_botas = st.text_input("Talle de Botas", placeholder="EJ. 42").upper()
        
        st.markdown("---")
        
        # --- SECCIÓN 5: SALUD, EDUCACIÓN Y ANTECEDENTES ---
        st.subheader("5. Salud, Educación y Antecedentes")
        nivel_educativo = st.selectbox("Nivel Educativo", ["Primaria", "Ciclo Básico", "Bachillerato / Secundaria", "Terciaria / Universitaria"])
        enfermedad_cronica = st.text_input("¿Posee alguna enfermedad crónica? ¿Cuál?", value="NO").upper()
        
        col_obs1, col_obs2, col_obs3 = st.columns(3)
        with col_obs1:
            sumario = st.selectbox("¿Tiene sumario?", ["No", "Sí"])
        with col_obs2:
            amenazas = st.selectbox("¿Amenazas?", ["No", "Sí"])
        with col_obs3:
            violencia_domestica = st.selectbox("¿Violencia doméstica?", ["No", "Sí"])
        
        detalle_sumario = st.text_area("Detalles sobre Sumario (Opcional)").upper()
        detalle_amenazas = st.text_area("Detalles sobre Amenazas (Opcional)").upper()
        detalle_vd = st.text_area("Detalles sobre Violencia Doméstica (Opcional)").upper()
        
        st.markdown("---")
        
        # --- SECCIÓN 6: DOCUMENTACIÓN ---
        st.subheader("6. Documentación")
        foto_cedula = st.file_uploader("Adjuntar Foto de la Cédula o Documentos", type=["jpg", "jpeg", "png"])
        
        enviar = st.form_submit_button("Enviar Ficha de Registro")
        
        if enviar:
            # Validar que los campos numéricos contengan solo números
            campos_numericos = [
                (telefono, "Teléfono"),
                (tel_emergencia, "Teléfono de Emergencia"),
                (legajo, "Número de Legajo"),
                (num_arma, "Número de Pistola"),
                (num_chaleco, "Número de Chaleco Balístico")
            ]
            
            error_numerico = False
            for valor, nombre_campo in campos_numericos:
                if valor and not valor.isdigit():
                    st.error(f"⚠️ El campo **{nombre_campo}** debe contener únicamente números.")
                    error_numerico = True
            
            if not error_numerico:
                if not apellidos or not nombres or cargo == "Seleccione..." or marca_arma == "Seleccione..." or marca_chaleco == "Seleccione..." or not foto_cedula:
                    st.error("Por favor, complete los campos obligatorios (Apellidos, Nombres, Grado, Arma, Chaleco y la Foto).")
                else:
                    st.success("¡Ficha enviada con éxito! Quedará pendiente de aprobación por la administración.")
                    st.balloons()
else:
    st.info("ℹ️ Ingrese su número de cédula (exactamente 8 dígitos) en ambos campos para habilitar el formulario.")
