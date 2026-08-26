# =============================================================================
# SIMULADOR COMPLETO ASME PCC-1-2022 - ENRUTADOR CENTRAL
# Autoría y Propiedad de la Documentación: Fabricio Pizzolato 
# Institución: IPCL MENFA - UTN
# =============================================================================
import streamlit as st
from datetime import date
import sys
import os

# Configuración global y estética de la plataforma Streamlit (Debe ser la primera instrucción)
st.set_page_config(
    page_title="Simulador ASME PCC-1-2022",
    page_icon="🔧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Fuerza a Python a buscar e indexar las subcarpetas del directorio actual
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importación de los módulos referenciando la subcarpeta /modules
try:
    from modules.module_0 import render_module_0
    from modules.module_1 import render_module_1
    from modules.module_2 import render_module_2
    from modules.module_3 import render_module_3
    from modules.module_4 import render_module_4
    from modules.module_5 import render_module_5
    from modules.module_6 import render_module_6
except ImportError as e:
    st.error(f"⚠️ Error de Infraestructura: No se pudo cargar un módulo. Detalle: {e}")
    st.stop()


def main():
    # Inicialización de estado de sesión para el rol de usuario
    if "user_role" not in st.session_state:
        st.session_state["user_role"] = "Operador"

    # -------------------------------------------------------------------------
    # PANEL LATERAL: Identidad Corporativa, Control de Rol y Navegación
    # -------------------------------------------------------------------------
    st.sidebar.image("https://img.icons8.com/fluency/96/worker-with-road-cone.png", width=80)
    st.sidebar.title("Simulador ASME PCC-1")
    st.sidebar.markdown("**Autor:** Fabricio Pizzolato")
    st.sidebar.markdown("**Unidad:** IPCL MENFA - UTN")
    st.sidebar.markdown("---")

    # Selector de Perfil de Usuario (Operador vs Supervisor QA/QC)
    rol_seleccionado = st.sidebar.selectbox(
        "Perfil de Usuario Activo:",
        ["Operador de Campo", "Supervisor QA/QC - Ingeniería"],
        index=0 if st.session_state["user_role"] == "Operador" else 1
    )
    
    # Sincronización del estado de sesión
    st.session_state["user_role"] = "Operador" if "Operador" in rol_seleccionado else "Supervisor"

    st.sidebar.markdown("---")
    
    # Menú de selección radial vinculado a la estructura modular del proyecto
    module_selection = st.sidebar.radio(
        "Seleccione el Módulo de Capacitación:",
        [
            "Módulo 0: Prólogo e Introducción",
            "Módulo 1: Procedimientos de Campo",
            "Módulo 2: Inspección y Defectos",
            "Módulo 3: Base de Datos y Pernos",
            "Módulo 4: Control de Torque y Ajuste",
            "Módulo 5: Ensayos y Desarmado Seguro",
            "Módulo 6: Panel de Evaluación Histórica"
        ],
        index=0
    )
    
    st.sidebar.markdown("---")
    
    # Marco Normativo Integrado en la Barra Lateral
    st.sidebar.subheader("📖 Referencias Normativas")
    st.sidebar.caption(
        "• **ASME PCC-1-2022:** Guidelines for Pressure Boundary Bolted Flange Joint Assembly\n"
        "• **ASME B16.5 / B16.47:** Steel Pipe Flanges & Fittings\n"
        "• **ASME B16.20:** Metallic Gaskets for Pipe Flanges\n"
        "• **ASME Sec VIII Div 1 App 2:** Rules for Bolted Flange Connections\n"
        "• **EN 1591-4:** Qualification of Personnel Competence"
    )

    st.sidebar.markdown("---")
    st.sidebar.caption(f"Plataforma Educativa v2.5 • {date.today().strftime('%Y')}")

    # -------------------------------------------------------------------------
    # INDICADOR SUPERIOR DE PERFIL ACTIVO
    # -------------------------------------------------------------------------
    col_hdr1, col_hdr2 = st.columns([3, 1])
    with col_hdr1:
        st.caption(f"PERFIL ACTIVO: **{rol_seleccionado.upper()}**")
    with col_hdr2:
        if st.session_state["user_role"] == "Supervisor":
            st.warning("🔒 MODO SUPERVISIÓN / INGENIERÍA HABILITADO")
        else:
            st.success("👷 MODO OPERACIÓN DE CAMPO HABILITADO")

    # -------------------------------------------------------------------------
    # ENRUTAMIENTO LÓGICO: Renderizado Condicional de Módulos
    # -------------------------------------------------------------------------
    if "Módulo 0" in module_selection:
        render_module_0()
        
    elif "Módulo 1" in module_selection:
        render_module_1()
        
    elif "Módulo 2" in module_selection:
        render_module_2()
        
    elif "Módulo 3" in module_selection:
        render_module_3()
        
    elif "Módulo 4" in module_selection:
        render_module_4()
        
    elif "Módulo 5" in module_selection:
        render_module_5()
        
    elif "Módulo 6" in module_selection:
        render_module_6()

if __name__ == "__main__":
    main()
