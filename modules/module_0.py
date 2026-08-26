# =============================================================================
# MÓDULO 0: PRÓLOGO, MARCO REGULATORIO Y EVOLUCIÓN NORMATIVA (ASME PCC-1-2022)
# Autoría y Propiedad de la Documentación: Fabricio Pizzolato
# Institución: MENFA- Capacitaciones
# =============================================================================
import streamlit as st

def render_module_0():
    st.title("📘 Módulo 0: Prólogo y Marco Regulatorio Integrado")
    
    # Lectura del rol activo desde la sesión de Streamlit (gestionado por app.py)
    user_role = st.session_state.get("user_role", "Operador")
    
    st.markdown("""
    Bienvenido al **Simulador de Integridad de Uniones Bridadas**. Este software opera bajo los lineamientos estrictos del estándar 
    **ASME PCC-1-2022** (*Pressure Boundary Bolted Flange Joint Assembly*), articulado con los códigos internacionales de dimensionamiento, 
    manufactura de juntas y calificación de personal.
    """)
    
    st.warning("""
    **📢 CAMBIO DE PARADIGMA (Edición 2022):** El título oficial eliminó la frase *'Guidelines for'*. 
    El texto principal se revisó en su totalidad y las recomendaciones ahora se estructuran como **Requisitos Obligatorios**.
    """, icon="⚠️")
    
    # Estructura de pestañas organizadas
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🌐 Ecosistema Normativo", 
        "⚖️ Sintaxis Semántica", 
        "🛠️ Resumen de Cambios (2022)",
        "⏳ Historia del Estándar",
        "👨‍🔧 Control de Roles"
    ])
    
    # -------------------------------------------------------------------------
    # TAB 1: ECOSISTEMA NORMATIVO AMPLIADO
    # -------------------------------------------------------------------------
    with tab1:
        st.subheader("Integración de Estándares Industriales y Código de Uniones")
        st.write("ASME PCC-1 interactúa con otros códigos de ingeniería durante la fabricación, montaje y vida operativa del equipo:")
        
        st.table({
            "Fase Operativa / Aplicación": [
                "Montaje, Secuencia y Torque", 
                "Dimensiones y Rangos P-T de Brida", 
                "Tolerancias de Juntas y Anillos",
                "Competencia y Calificación de Personal",
                "Equipos de Cabezal de Pozo (Oil & Gas)",
                "Evaluación de Fitness-for-Service (FFS)",
                "Reparaciones Mecánicas Post-Construcción"
            ],
            "Norma Aplicable": [
                "ASME PCC-1-2022", 
                "ASME B16.5 / B16.47", 
                "ASME B16.20 (Spiral/RTJ)",
                "EN 1591-4 / ASME PCC-1 App. A",
                "API 6A / API 17D",
                "API 579-1 / ASME FFS-1",
                "ASME PCC-2"
            ],
            "Estatus en el Simulador": [
                "ACTIVO (Motor Principal de Cálculo)", 
                "Base de Datos (Módulo 3)", 
                "Validación de Tolerancias (Módulo 2)",
                "Matriz de Competencias y Roles",
                "Referencia para Bridas RTJ",
                "Informativo / Módulo de Inspección",
                "Informativo"
            ]
        })

    # -------------------------------------------------------------------------
    # TAB 2: SINTAXIS SEMÁNTICA
    # -------------------------------------------------------------------------
    with tab2:
        st.subheader("Criterio Semántico de Cumplimiento Normativo")
        st.info("El simulador evalúa las maniobras de montaje según la terminología legal/técnica de ASME:")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.error("🔴 **SHALL (Debe)**\n\nDenota un **requisito obligatorio**. Ignorarlo invalida el procedimiento y genera rechazo automático en el Registro R-2.2-2.")
        with col2:
            st.warning("🟡 **SHOULD (Debería)**\n\nDenota una **recomendación de buena práctica** de ingeniería que debe justificarse si no se aplica.")
        with col3:
            st.success("🟢 **MAY (Puede)**\n\nDenota **permiso o discrecionalidad** técnica otorgada al operador / armador calificado.")

    # -------------------------------------------------------------------------
    # TAB 3: CAMBIOS CLAVE 2022
    # -------------------------------------------------------------------------
    with tab3:
        st.subheader("🛠️ Cambios Clave Incorporados en la Edición 2022")
        st.write("De acuerdo con el *Summary of Changes* oficial de ASME PCC-1-2022, el motor del software se diseñó bajo las siguientes modificaciones:")
        
        col_left, col_right = st.columns(2)
        with col_left:
            st.markdown("""
            * **Reestructuración de Apéndices:** Los antiguos Apéndices A al Q ahora se clasifican explícitamente como **Nonmandatory Appendices**, manteniendo su peso técnico como guías metodológicas.
            * **Nueva Terminología de Superficie:** Se migró formalmente el término *'Contact surface'* a **'Seating surface'** (Superficie de asentamiento) para evitar confusiones de sello.
            """)
        with col_right:
            st.markdown("""
            * **Precisiones en Target Torque (Apéndice O):** Se ajustaron las fórmulas de fricción y carga objetivo de perno (`eq. O-3` a `eq. O-6`), considerando la disipación por relajación elástica.
            * **Gestión de Registros de Campo (Apéndice R):** Se introdujo la estandarización de planillas de aseguramiento de calidad (QA/QC) a través de la Tabla R-2.2-2.
            """)

    # -------------------------------------------------------------------------
    # TAB 4: LÍNEA DE TIEMPO DEL ESTÁNDAR
    # -------------------------------------------------------------------------
    with tab4:
        st.subheader("⏳ Evolución Histórica de ASME PCC-1")
        st.caption("De Guía de Buenas Prácticas a Estándar de Requisitos Obligatorios")

        # Representación mediante secuencia cronológica
        st.markdown("""
        * **1993 — Comienzo de Elaboración:** ASME crea el comité *Post Construction Committee* (PCC) para unificar criterios de mantenimiento e integridad en plantas procesadoras y campos petroleros.
        * **2000 — Primera Edición (ASME PCC-1-2000):** Se emite el primer documento enfocado como *Guidelines for Pressure Boundary Bolted Flange Joint Assembly*.
        * **2010 — Incorporación de Apéndices Técnicos (Edición 2010):** Se integran las metodologías analíticas de cálculo de torque (Apéndice O) y alineación de bridas.
        * **2013 — Calificación de Personal (Edición 2013):** Se amplía el Apéndice A (*Qualification and Training of Joint Assembly Personnel*) para alinearse con estándares europeos como EN 1591-4.
        * **2019 — Consolidación de Patrones de Ajuste (Edición 2019):** Se perfeccionan los métodos alternativos de torque (Pase Único y Grupos de Pernos) para reducir tiempos de parada.
        * **2022 — Eliminación de 'Guidelines' (ASME PCC-1-2022):** El estándar abandona el carácter opcional. Las secciones principales se transforman en **Mandatory Assembly Procedures**.
        """)

    # -------------------------------------------------------------------------
    # TAB 5: CONTROL DE ROLES Y MATRIZ DE RESPONSABILIDADES
    # -------------------------------------------------------------------------
    with tab5:
        st.subheader("👨‍🔧 Matriz de Permisos por Rol en la Plataforma")
        
        if user_role == "Supervisor":
            st.warning("🔒 **Perfil Actual: SUPERVISOR QA/QC - INGENIERÍA**")
            st.markdown("""
            **Atribuciones en el Simulador:**
            * Modificación de parámetros críticos de ingeniería (Factores K, % Yield de Pernos).
            * Firma digital y emisión del dictamen final en la planilla R-2.2-2.
            * Aprobación de desviaciones en tolerancias de caras de brida (Módulo 2).
            """)
        else:
            st.success("👷 **Perfil Actual: OPERADOR DE CAMPO / TÉCNICO ARMADOR**")
            st.markdown("""
            **Atribuciones en el Simulador:**
            * Carga de mediciones de campo (rugosidad, alineación, torque aplicado).
            * Ejecución de las listas de chequeo pre-ajuste y secuencias en estrella.
            * Registro preliminar de datos de inspección visual.
            """)

if __name__ == "__main__":
    render_module_0()
