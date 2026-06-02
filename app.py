# app.py
import streamlit as st

# Importación completa de los módulos del ecosistema ASME PCC-1
from modules.module_0 import render_module_0
from modules.module_1 import render_module_1
from modules.module_2 import render_module_2  # <-- ¡Módulo nuevo de gráficos importado!
from modules.module_4 import render_module_4
from modules.module_5 import render_module_5  
from modules.module_6 import render_module_6  

# Configuración inicial de la plataforma
st.set_page_config(
    page_title="Simulador ASME PCC-1-2022",
    page_icon="🔧",
    layout="wide"
)

def main():
    # Autoría del software fijada
    st.sidebar.title("🔧 Simulador ASME PCC-1-2022")
    st.sidebar.caption("Autoría del Software: Fabricio Pizzolato")
    st.sidebar.markdown("---")
    
    # Menú de selección e interconexión modular
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
    
    # Enrutador lógico (Routing Engine) de la arquitectura
    if modulo_seleccionado == "Module 0: Foreword & Regulatory Framework":
        render_module_0()
    elif modulo_seleccionado == "Module 1: Scope & Field Assembly Procedures (Sec. 1-10)":
        render_module_1()
    elif modulo_seleccionado == "Module 2: Pre-Assembly Inspection (Sec. 4-6 / App. C-E)":
        render_module_2()  # <-- ¡Nueva ruta gráfica activa!
    elif modulo_seleccionado == "Module 4: Target Torque Engine (Sec. 9-11 / App. J, K, O, Q)":
        render_module_4()
    elif modulo_seleccionado == "Module 5: Testing & Disassembly (Sec. 12, 14)":
        render_module_5()
    elif modulo_seleccionado == "Module 6: Records & Troubleshooting (Sec. 13 / App. P, R)":
        render_module_6()
    else:
        st.title(modulo_seleccionado)
        st.info("Estructura modular lista. Próximamente se integrará el archivo correspondiente en la carpeta /modules.")

if __name__ == "__main__":
    main()
