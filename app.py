# app.py
import streamlit as st

# Configuración de la página de Streamlit
st.set_page_config(
    page_title="Simulador ASME PCC-1-2022",
    page_icon="🔧",
    layout="wide"
)

# -----------------------------------------------------------------------------
# MÓDULO 0: FOREWORD, REGULATORY FRAMEWORK & SUMMARY OF CHANGES
# -----------------------------------------------------------------------------
def render_module_0():
    st.title("📘 Module 0: Foreword & Regulatory Framework")
    
    st.markdown("""
    Bienvenido al **Simulador de Integridad de Uniones Bridadas**. Este software opera bajo los lineamientos estrictos del estándar 
    **ASME PCC-1-2022** (*Pressure Boundary Bolted Flange Joint Assembly*).
    """)
    
    # Alerta de Actualización de la Norma
    st.warning("""
    **📢 CAMBIO DE PARADIGMA (Edición 2022):** El título oficial eliminó la frase *'Guidelines for'*. 
    El texto principal se revisó en su totalidad y las recomendaciones ahora se estructuran como **Requisitos Obligatorios**.
    """, icon="⚠️")
    
    # Pestañas del Módulo 0
    tab1, tab2, tab3, tab4 = st.tabs([
        "Ecosistema Post-Construcción", 
        "Sintaxis Semántica", 
        "Resumen de Cambios (2022)",
        "Historia del Estándar"
    ])
    
    with tab1:
        st.subheader("Integración de Estándares Industriales")
        st.write("ASME PCC-1 interactúa con otros códigos durante la vida operativa del equipo:")
        st.table({
            "Fase Operativa": ["Montaje y Torque", "Planificación de Inspección", "Evaluación de Defectos/Rayas", "Reparación Mecánica"],
            "Norma Aplicable": ["ASME PCC-1-2022", "ASME PCC-3 (Risk-Based)", "API 579-1 / ASME FFS-1 (Fitness-for-Service)", "ASME PCC-2"],
            "Estatus en este Simulador": ["ACTIVO (Motor de Cálculo)", "Informativo", "Vinculado al Módulo de Inspección", "Informativo"]
        })
        
    with tab2:
        st.subheader("Criterio Semántico de Cumplimiento")
        st.info("El simulador evalúa tus pasos de montaje según la terminología oficial de ASME:")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.error("🔴 **SHALL (Debe)**\n\nDenota un **requisito obligatorio** para el montaje. Ignorarlo invalida el procedimiento.")
        with col2:
            st.warning("🟡 **SHOULD (Debería)**\n\nDenota una **recomendación de buena práctica** de ingeniería.")
        with col3:
            st.success("🟢 **MAY (Puede)**\n\nDenota **permiso o discrecionalidad** del operador.")

    with tab3:
        st.subheader("🛠️ Cambios Clave Incorporados en el Código del Simulador")
        st.write("De acuerdo con el *Summary of Changes* oficial de ASME PCC-1-2022, el motor del software se diseñó bajo las siguientes modificaciones:")
        
        # Grid visual de los cambios que afectan los cálculos del software
        col_left, col_right = st.columns(2)
        
        with col_left:
            st.markdown("""
            * **Rediseño de Apéndices:** Los antiguos Apéndices A al Q ahora se clasifican explícitamente como **Nonmandatory** (No mandatorios pero regulatorios).
            * **Nueva Terminología de Superficie:** Se migró el término *'Contact surface'* a **'Seating surface'** (Superficie de asentamiento) en todo el sistema y tablas (Ej. Tabla C-1).
            * **Inspección de Defectos (Apéndice D):** Se actualizaron por completo los criterios de evaluación de tolerancias para rayas, golpes y picaduras en bridas.
            * **Calificación de Personal:** El **Appendix A** fue reescrito por completo (*Revised in its entirety*).
            """)
            
        with col_right:
            st.markdown("""
            * **Fórmulas del Apéndice O (Target Torque):** Se aplicaron las revisiones analíticas sobre las ecuaciones de torque (`eq. O-3`), diámetros de junta ($G_{W}$ y $G_{O.D.}$) y límites de tensión elasto-plástica.
            * **Tablas de Torque Indexadas:** Actualización de las tablas de referencia críticas `O-3.2-1` y `O-3.2-1M` para aceros de baja aleación.
            * **Nuevos Reportes de Gestión (Apéndice R):** Se agregó la estructura del nuevo Apéndice R para la administración de registros de montaje (*Assembly Records Management*).
            """)
            
        # Tabla de trazabilidad para auditoría del software
        with st.expander("Ver bitácora de trazabilidad de cambios (ASME vs Software)"):
            st.dataframe([
                {"Ubicación ASME": "Mandatory Appendix I", "Cambio 2022": "Añadido (Definiciones)", "Módulo Software": "Módulo 1 & 3"},
                {"Ubicación ASME": "Nonmandatory Appendix A", "Cambio 2022": "Revisado por completo", "Módulo Software": "Módulo 1 (Calificación)"},
                {"Ubicación ASME": "Nonmandatory Appendix D", "Cambio 2022": "Secciones D-1 a D-3 revisadas", "Módulo Software": "Módulo 2 (Tolerancias)"},
                {"Ubicación ASME": "Nonmandatory Appendix O", "Cambio 2022": "Ecuaciones y límites modificados", "Módulo Software": "Módulo 4 (Motor de Torque)"},
                {"Ubicación ASME": "Nonmandatory Appendix R", "Cambio 2022": "Añadido por completo", "Módulo Software": "Módulo 6 (Reportes QA/QC)"},
            ], use_container_width=True)

    with tab4:
        st.subheader("Línea de Tiempo del Estándar")
        st.text("""
        • 1993: Formación del Grupo Ad Hoc de Post-Construcción de ASME.
        • 2000: Primera edición de ASME PCC-1 (Guidelines).
        • 2013: Inclusión de Calificación de Personal (Apéndice A).
        • 2019: Adopción del Target Torque Index (Apéndice O) y Herramientas de Potencia (Apéndice Q).
        • 2022: Transición completa de Guía a Estándar de Requisitos Obligatorios (Edición Actual).
        """)

# -----------------------------------------------------------------------------
# ORQUESTADOR CENTRAL / MENÚ DE NAVEGACIÓN
# -----------------------------------------------------------------------------
def main():
    # El título del software refleja el cambio de título de la norma 2022
    st.sidebar.title("🔧 Simulador ASME PCC-1-2022")
    st.sidebar.caption("Pressure Boundary Bolted Flange Joint Assembly")
    
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
