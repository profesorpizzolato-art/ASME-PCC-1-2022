# =============================================================================
# MAIN APP: SIMULADOR DE TORQUE Y BRIDAS (ASME PCC-1-2022)
# Autoría y Propiedad de la Documentación: Fabricio Pizzolato
# Institución: IPCL MENFA - UTN
# =============================================================================
import streamlit as st

# Configuración inicial de la página (debe ser la primera orden de Streamlit)
st.set_page_config(
    page_title="Simulador ASME PCC-1 | IPCL MENFA",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# IMPORTACIÓN DINÁMICA Y SEGURA DE MÓDULOS
# -----------------------------------------------------------------------------
try:
    from modules.módulo_2 import render_module_2
except ImportError:
    render_module_2 = None

try:
    from modules.módulo_3 import render_module_3
except ImportError:
    render_module_3 = None

try:
    from modules.módulo_4 import render_module_4
except ImportError:
    render_module_4 = None

try:
    from modules.módulo_5 import render_module_5
except ImportError:
    render_module_5 = None

try:
    from modules.módulo_operador import render_module_operador
except ImportError:
    render_module_operador = None

try:
    from modules.módulo_supervisor import render_module_supervisor
except ImportError:
    render_module_supervisor = None

# -----------------------------------------------------------------------------
# BARRA LATERAL (SIDEBAR): MENÚ DE NAVEGACIÓN Y CRÉDITOS
# -----------------------------------------------------------------------------
with st.sidebar:
    st.image("https://via.placeholder.com/250x80.png?text=IPCL+MENFA+-+UTN", use_container_width=True)
    st.title("🛠️ Menú Principal")
    st.caption("Sistema Integrado de Cálculo y Montaje de Bridas (ASME PCC-1-2022)")
    
    st.markdown("---")
    
    # Navegación Principal por Módulos
    opcion_modulo = st.radio(
        "Seleccione un Módulo / Rol:",
        [
            "🏠 Inicio / Dashboard",
            "1️⃣ Módulo 1: Selección de Junta y Brida",
            "2️⃣ Módulo 2: Inspección y Tolerancias (Sec. 4)",
            "3️⃣ Módulo 3: Alineación y Holguras (App. E/G)",
            "4️⃣ Módulo 4: Target Torque & Tightening Engine",
            "5️⃣ Módulo 5: Registro de Campo y Torquímetro",
            "👷 Módulo Operador: Consola en Sitio",
            "👨‍💼 Módulo Supervisor: QA/QC & Release",
            "6️⃣ Módulo 6: Generación de Reporte PDF (App. R)"
        ],
        index=4  # Módulo 4 seleccionado por defecto
    )
    
    st.markdown("---")
    
    # Información de Autoría y Licencia
    st.markdown("### 📌 Información de Autoría")
    st.markdown("**Desarrollador:** Fabricio Pizzolato")
    st.markdown("**Institución:** IPCL MENFA / UTN")
    st.markdown("**Norma:** ASME PCC-1-2022")
    st.markdown("**Versión:** 2.5.0 (2026)")

# -----------------------------------------------------------------------------
# ENRUTADOR DE MÓDULOS Y CONTENIDO PRINCIPAL
# -----------------------------------------------------------------------------
if opcion_modulo == "🏠 Inicio / Dashboard":
    st.title("⚙️ Simulador Técnico de Torque y Ajuste de Bridas")
    st.caption("Basado en los lineamientos de la norma ASME PCC-1-2022")
    
    st.markdown("""
    Bienvenido al simulador técnico e interactivo diseñado para la capacitación, supervisión y asistencia operativa 
    en uniones bridadas.

    ### 📌 Estructura y Módulos Disponibles:
    * **Módulo 1:** Selección de Junta, Brida y Espárragos.
    * **Módulo 2:** Inspección de Superficies de Asiento y Tolerancias (Sección 4 & Apéndice C).
    * **Módulo 3:** Verificación de Alineación y Holguras Permisibles (Apéndices E y G).
    * **Módulo 4:** Cálculo de Target Torque y Protocolo de Pases (Apéndice O & Secciones 10/11).
    * **Módulo 5:** Hoja de Campo, Conversión de Bomba Hidráulica y Selección de Bocas.
    * **Entorno Operador:** Consola móvil guiada para ejecución paso a paso en sitio.
    * **Entorno Supervisor:** Panel de control de calidad, auditoría y liberación (*Sign-off*).
    * **Módulo 6:** Emisión de Certificado e Informe Técnico en PDF (Apéndice R).
    """)
    st.info("👈 Utilizá la barra lateral para navegar entre las calculadoras y entornos de rol.")

elif opcion_modulo == "1️⃣ Módulo 1: Selección de Junta y Brida":
    st.title("1️⃣ Módulo 1: Selección de Junta y Brida")
    st.info("Módulo en desarrollo / Base de datos dimensional de bridas ASME B16.5 y juntas.")

elif opcion_modulo == "2️⃣ Módulo 2: Inspección y Tolerancias (Sec. 4)":
    if render_module_2 is not None:
        render_module_2()
    else:
        st.error("No se pudo cargar `modules/módulo_2.py`. Verificá la existencia del archivo.")

elif opcion_modulo == "3️⃣ Módulo 3: Alineación y Holguras (App. E/G)":
    if render_module_3 is not None:
        render_module_3()
    else:
        st.error("No se pudo cargar `modules/módulo_3.py`. Verificá la existencia del archivo.")

elif opcion_modulo == "4️⃣ Módulo 4: Target Torque & Tightening Engine":
    if render_module_4 is not None:
        render_module_4()
    else:
        st.error("No se pudo cargar `modules/módulo_4.py`. Verificá la existencia del archivo.")

elif opcion_modulo == "5️⃣ Módulo 5: Registro de Campo y Torquímetro":
    if render_module_5 is not None:
        render_module_5()
    else:
        st.error("No se pudo cargar `modules/módulo_5.py`. Verificá la existencia del archivo.")

elif opcion_modulo == "👷 Módulo Operador: Consola en Sitio":
    if render_module_operador is not None:
        render_module_operador()
    else:
        st.error("No se pudo cargar `modules/módulo_operador.py`. Verificá la existencia del archivo.")

elif opcion_modulo == "👨‍💼 Módulo Supervisor: QA/QC & Release":
    if render_module_supervisor is not None:
        render_module_supervisor()
    else:
        st.error("No se pudo cargar `modules/módulo_supervisor.py`. Verificá la existencia del archivo.")

elif opcion_modulo == "6️⃣ Módulo 6: Generación de Reporte PDF (App. R)":
    st.title("6️⃣ Módulo 6: Generador de Reportes PDF (Apéndice R)")
    st.info("Módulo en desarrollo / Exportación oficial de datos e instrucción técnica.")
