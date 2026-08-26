# =============================================================================
# MAIN APP: SIMULADOR DE TORQUE Y BRIDAS (ASME PCC-1-2022)
# Autoría y Propiedad de la Documentación: Fabricio Pizzolato
# Institución: IPCL MENFA - UTN
# =============================================================================
import streamlit as st

# Configuración inicial de la página en Streamlit (debe ser la primera orden Streamlit)
st.set_page_config(
    page_title="Simulador ASME PCC-1 | IPCL MENFA",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# IMPORTACIÓN DINÁMICA / CONTROLADA DE MÓDULOS
# -----------------------------------------------------------------------------
# Nota: Cada módulo debe contener una función render_module_X() o similar.
try:
    from modules.módulo_4 import render_module_4
except ImportError:
    render_module_4 = None

# -----------------------------------------------------------------------------
# BARRA LATERAL (SIDEBAR): LOGO, MENÚ Y ESTADO
# -----------------------------------------------------------------------------
with st.sidebar:
    st.image("https://via.placeholder.com/250x80.png?text=IPCL+MENFA+-+UTN", use_container_width=True)
    st.title("🛠️ Menú Principal")
    st.caption("Sistema Integrado de Cálculo y Montaje de Bridas (ASME PCC-1-2022)")
    
    st.markdown("---")
    
    # Navegación Principal por Módulos
    opcion_modulo = st.radio(
        "Seleccione un Módulo:",
        [
            "🏠 Inicio / Dashboard",
            "1️⃣ Módulo 1: Selección de Junta y Brida",
            "2️⃣ Módulo 2: Inspección y Tolerancias (Sec. 4)",
            "3️⃣ Módulo 3: Alineación y Holguras (App. E/G)",
            "4️⃣ Módulo 4: Target Torque & Tightening Engine",
            "5️⃣ Módulo 5: Registro de Campo y Torquímetro",
            "6️⃣ Módulo 6: Generación de Reporte PDF (App. R)"
        ],
        index=4  # Módulo 4 por defecto para desarrollo
    )
    
    st.markdown("---")
    
    # Información de Autoría y Licencia
    st.markdown("### 📌 Información de Autoría")
    st.markdown("**Desarrollador:** Fabricio Pizzolato")
    st.markdown("**Institución:** IPCL MENFA / UTN")
    st.markdown("**Norma:** ASME PCC-1-2022")
    st.markdown("**Versión:** 2.4.0 (2026)")

# -----------------------------------------------------------------------------
# ENRUTADOR DE MÓDULOS Y CONTENIDO PRINCIPAL
# -----------------------------------------------------------------------------
if opcion_modulo == "🏠 Inicio / Dashboard":
    st.title("⚙️ Simulador Técnico de Torque y Ajuste de Bridas")
    st.subtitle("Basado en los lineamientos de ASME PCC-1-2022")
    
    st.markdown("""
    Bienvenido al simulador técnico e interactivo diseñado para la capacitación y asistencia operativa 
    en uniones bridadas según la norma **ASME PCC-1-2022**.

    ### 📌 Estructura del Simulador:
    * **Módulo 1:** Selección de Junta, Brida y Espárragos.
    * **Módulo 2:** Inspección de Superficies de Asiento y Tolerancias (Sección 4).
    * **Módulo 3:** Verificación de Alineación y Holguras Permisibles (Apéndices E y G).
    * **Módulo 4:** Cálculo de Target Torque y Protocolo de Pases (Apéndice O & Secciones 10/11).
    * **Módulo 5:** Hoja de Campo y Control de Apriete en Tiempo Real.
    * **Módulo 6:** Emisión de Certificado y Informe Técnico en PDF (Apéndice R).
    """)
    st.info("👈 Utilizá la barra lateral para navegar por los diferentes módulos.")

elif opcion_modulo == "1️⃣ Módulo 1: Selección de Junta y Brida":
    st.title("1️⃣ Módulo 1: Selección de Junta y Brida")
    st.info("Módulo en desarrollo / Integración de base de datos de bridas y juntas.")

elif opcion_modulo == "2️⃣ Módulo 2: Inspección y Tolerancias (Sec. 4)":
    st.title("2️⃣ Módulo 2: Inspección de Caras de Brida")
    st.info("Módulo en desarrollo / Verificación de ralladuras, rugosidad y daños en la cara de contacto.")

elif opcion_modulo == "3️⃣ Módulo 3: Alineación y Holguras (App. E/G)":
    st.title("3️⃣ Módulo 3: Verificación de Alineación")
    st.info("Módulo en desarrollo / Evaluación de desalineación axial, angular y de paralaje.")

elif opcion_modulo == "4️⃣ Módulo 4: Target Torque & Tightening Engine":
    if render_module_4 is not None:
        render_module_4()
    else:
        st.error("No se pudo cargar el archivo `modules/módulo_4.py`. Verificá que la carpeta `modules/` exista y contenga el archivo correctamente nombrado.")

elif opcion_modulo == "5️⃣ Módulo 5: Registro de Campo y Torquímetro":
    st.title("5️⃣ Módulo 5: Hoja de Registro de Campo")
    st.info("Módulo en desarrollo / Carga de torques reales aplicados por perno y pase.")

elif opcion_modulo == "6️⃣ Módulo 6: Generación de Reporte PDF (App. R)":
    st.title("6️⃣ Módulo 6: Generador de Reportes PDF (Apéndice R)")
    st.info("Módulo en desarrollo / Exportación oficial de datos e instrucción técnica.")
