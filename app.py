# app.py
import streamlit as st

# Configuración de la página (Debe ser la primera línea de Streamlit)
st.set_page_config(
    page_title="Simulador ASME PCC-1-2022",
    page_icon="🔧",
    layout="wide"
)

# -----------------------------------------------------------------------------
# MÓDULO 0: FOREWORD & REGULATORY FRAMEWORK
# -----------------------------------------------------------------------------
def render_module_0():
    st.title("📘 Module 0: Foreword & Regulatory Framework")
    
    st.markdown("""
    Bienvenido al **Simulador de Integridad de Uniones Bridadas**. Este software opera bajo los lineamientos estrictos del estándar 
    **ASME PCC-1-2022** (*Pressure Boundary Bolted Flange Joint Assembly*).
    """)
    
    # Caja de advertencia sobre el cambio de la norma
    st.warning("""
    **📢 NOTA DE ACTUALIZACIÓN CRÍTICA (Edición 2022):** A diferencia de las versiones anteriores (2010, 2013, 2019), la edición **2022** ya no es una 'Guía de recomendaciones'. 
    Se han reemplazado las pautas por **Requisitos Obligatorios**. El título oficial eliminó la frase *'Guidelines for'*.
    """, icon="⚠️")
    
    # Pestañas de navegación interna
    tab1, tab2, tab3 = st.tabs(["Ecosistema Post-Construcción", "Sintaxis Obligatoria (Shall/Should/May)", "Historia del Estándar"])
    
    with tab1:
        st.subheader("Integración de Estándares Industriales")
        st.write("ASME PCC-1 interactúa con otros códigos durante la vida operativa del equipo:")
        
        st.table({
            "Fase Operativa": ["Montaje y Torque", "Planificación de Inspección", "Evaluación de Defectos/Rayas", "Reparación Mecánica"],
            "Norma Aplicable": ["ASME PCC-1-2022", "ASME PCC-3 (Risk-Based)", "API 579-1 / ASME FFS-1 (Fitness-for-Service)", "ASME PCC-2"],
            "Estatus en este Simulador": ["ACTIVO (Motor de Cálculo)", "Informativo", "Vinculado al Módulo de Inspección", "Informativo"]
        })
        
    with tab2:
        st.subheader("Criterio Jurídico y Técnico del Lenguaje")
        st.info("El simulador evalúa tus pasos de montaje según la semántica oficial de ASME:")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.error("🔴 **SHALL (Debe)**\n\nDenota un **requisito obligatorio** para el montaje. Ignorarlo invalida el procedimiento.")
        with col2:
            st.warning("🟡 **SHOULD (Debería)**\n\nDenota una **recomendación de buena práctica** de ingeniería.")
        with col3:
            st.success("🟢 **MAY (Puede)**\n\nDenota **permiso o discrecionalidad** del operador.")

    with tab3:
        st.subheader("Línea de Tiempo del Estándar")
        st.text("""
        • 1993: Formación del Grupo Ad Hoc de Post-Construcción de ASME.
        • 2000: Primera edición de ASME PCC-1.
        • 2013: Inclusión del Apéndice A (Calificación mandatoria de personal).
        • 2019: Adopción del Target Torque Index (Apéndice O) y Herramientas de Potencia (Apéndice Q).
        • 2022: Transición completa de Guía a Estándar Normativo (Edición Actual).
        """)

# -----------------------------------------------------------------------------
# ORQUESTADOR CENTRAL / MENÚ DE NAVEGACIÓN
# -----------------------------------------------------------------------------
def main():
    st.sidebar.image("https://via.placeholder.com/150", caption="Simulador MENFA", use_container_width=True)
    st.sidebar.title("Navegación ASME PCC-1")
    
    # Selector de módulos
    modulo_seleccionado = st.sidebar.selectbox(
        "Seleccione un Módulo:",
        [
            "Module 0: Foreword & Regulatory Framework",
            "Module 1: Scope & Personnel Qualification (Sec. 1-3 / App. A)",
            "Module 2: Pre-Assembly Inspection (Sec. 4-6 / App. C-E)",
            "Module 3: Engineering & Components Data (App. H, L, M, N)",
            "Module 4: Target Torque Engine (Sec. 9-11 / App. J, K, O, Q)",
            "Module 5: Testing & Disassembly (Sec. 12, 14)",
            "Module 6: Records & Troubleshooting (Sec. 13 / App. P, R)"
        ]
    )
    
    # Lógica de ruteo
    if modulo_seleccionado == "Module 0: Foreword & Regulatory Framework":
        render_module_0()
    else:
        st.title(modulo_seleccionado)
        st.info("Próximamente: Desarrollo de la lógica y tablas específicas de esta sección según ASME PCC-1-2022.")

if __name__ == "__main__":
    main()
