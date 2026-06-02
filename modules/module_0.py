# modules/module_0.py
import streamlit as st

def render_module_0():
    st.title("📘 Module 0: Foreword & Regulatory Framework")
    
    st.markdown("""
    Bienvenido al **Simulador de Integridad de Uniones Bridadas**. Este software opera bajo los lineamientos estrictos del estándar 
    **ASME PCC-1-2022** (*Pressure Boundary Bolted Flange Joint Assembly*).
    """)
    
    st.warning("""
    **📢 CAMBIO DE PARADIGMA (Edición 2022):** El título oficial eliminó la frase *'Guidelines for'*. 
    El texto principal se revisó en su totalidad y las recomendaciones ahora se estructuran como **Requisitos Obligatorios**.
    """, icon="⚠️")
    
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
        
        col_left, col_right = st.columns(2)
        with col_left:
            st.markdown("""
            * **Rediseño de Apéndices:** Los antiguos Apéndices A al Q ahora se clasifican explícitamente como **Nonmandatory**.
            * **Nueva Terminología de Superficie:** Se migró el término *'Contact surface'* a **'Seating surface'** (Superficie de asentamiento) en todo el sistema.
            """)
        with col_right:
            st.markdown("""
            * **Fórmulas del Apéndice O (Target Torque):** Se aplicaron las precisiones analíticas sobre las ecuaciones de torque (`eq. O-3`).
            * **Nuevos Reportes de Gestión (Apéndice R):** Estructura del nuevo Apéndice R para la administración de registros de montaje.
            """)

    with tab4:
        st.subheader("Línea de Tiempo del Estándar")
        st.text("1993 a 2022: Evolución de Guía de recomendaciones a Estándar de Requisitos Obligatorios.")
