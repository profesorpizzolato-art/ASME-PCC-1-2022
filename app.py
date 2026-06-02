# app.py
import streamlit as st

# Importación de los módulos locales
from modules.module_0 import render_module_0
from modules.module_1 import render_module_1

# Configuración inicial de la app
st.set_page_config(
    page_title="Simulador ASME PCC-1-2022",
    page_icon="🔧",
    layout="wide"
)

def main():
    st.sidebar.title("🔧 Simulador ASME PCC-1-2022")
    st.sidebar.caption("Pressure Boundary Bolted Flange Joint Assembly")
    st.sidebar.markdown("---")
    
    # Menú de navegación modular
    modulo_seleccionado = st.sidebar.selectbox(
        "Seleccione un Módulo:",
        [
            "Module 0: Foreword & Regulatory Framework",
            "Module 1: Scope & Field Assembly Procedures (Sec. 1-10)",
            "Module 2: Pre-Assembly Inspection (Sec. 4-6 / App. C-E)",
            "Module 3: Engineering & Components Data (App. H, L, M, N)",
            "Module 4: Target Torque Engine (Sec. 9-11 / App. J, K, O, Q)",
            "Module 5: Testing & Disassembly (Sec. 12, 14)",
            "Module 6: Records & Troubleshooting (Sec. 13 / App. P, R)"
        ]
    )
    
    # Enrutador central a archivos independientes
    if modulo_seleccionado == "Module 0: Foreword & Regulatory Framework":
        render_module_0()
    elif modulo_seleccionado == "Module 1: Scope & Field Assembly Procedures (Sec. 1-10)":
        render_module_1()
    else:
        st.title(modulo_seleccionado)
        st.info("Estructura modular lista. Próximamente se integrará el archivo correspondiente en la carpeta /modules.")

if __name__ == "__main__":
    main()
    
