# app.py
import streamlit as st

# Importación completa de los módulos del ecosistema ASME PCC-1
from modules.module_0 import render_module_0
from modules.module_1 import render_module_1
from modules.module_2 import render_module_2  
from modules.module_3 import render_module_3  # <-- ¡Módulo nuevo importado!
from modules.module_4 import render_module_4
from modules.module_5 import render_module_5  
from modules.module_6 import render_module_6  

st.set_page_config(
    page_title="Simulador ASME PCC-1-2022",
    page_icon="🔧",
    layout="wide"
)

def main():
    st.sidebar.title("🔧 Simulador ASME PCC-1-2022")
    st.sidebar.caption("Autoría del Software: Fabricio Pizzolato")
    st.sidebar.markdown("---")
    
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
        render_module_2()  
    elif modulo_seleccionado == "Module 3: Engineering & Components Data (App. H, L, M, N)":
        render_module_3()  # <-- ¡Nueva ruta activa!
    elif modulo_seleccionado == "Module 4: Target Torque Engine (Sec. 9-11 / App. J, K, O, Q)":
        render_module_4()
    elif modulo_seleccionado == "Module 5: Testing & Disassembly (Sec. 12, 14)":
        render_module_5()
    elif modulo_seleccionado == "Module 6: Records & Troubleshooting (Sec. 13 / App. P, R)":
        render_module_6()

if __name__ == "__main__":
    main()
