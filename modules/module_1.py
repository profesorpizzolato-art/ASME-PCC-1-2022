# =============================================================================
# MÓDULO 1: PROCEDIMIENTOS DE CAMPO Y REGISTRO DE ASAMBLEA (ASME PCC-1-2022)
# Autoría y Propiedad de la Documentación: Fabricio Pizzolato
# Institución: MENFA- Capacitaciones
# =============================================================================
import streamlit as st
from datetime import date

def render_module_1():
    st.title("📋 Módulo 1: Alcance, Procedimientos de Campo y Registro R-2.2-2")
    st.caption("Validación de Requisitos de Campo según ASME PCC-1-2022 Secciones 1 a 10 y Apéndice R")
    
    st.header("1. Contexto de la Junta y Responsabilidades")
    col_a, col_b = st.columns(2)
    
    with col_a:
        owner = st.text_input("Propietario de la Instalación (Owner):", value="IPCL MENFA")
        gasket_inside = st.radio(
            "¿La junta de anillo está enteramente dentro del círculo de pernos sin contacto exterior? (Sec. 1 Scope)",
            ["Sí (Aplica ASME PCC-1 plenamente)", "No (Requiere evaluación de ingeniería adaptada)"]
        )
        if "No" in gasket_inside:
            st.warning("⚠️ Los principios se pueden aplicar selectivamente, pero la geometría requiere revisión de ingeniería externa.")
            
    with col_b:
        assembler = st.text_input("Nombre del Armador / Técnico (Assembler):", value="Fabricio Pizzolato")
        has_written_proc = st.checkbox("¿Existe un procedimiento de montaje escrito aprobado por el Owner? (Sec. 2a)", value=True)
        if not has_written_proc:
            st.error("❌ REQUISITO CRÍTICO: El usuario debe desarrollar procedimientos escritos basados en los requerimientos del dueño.")

    st.markdown("---")
    
    # Pestañas de control operativo e inspección de campo + Apéndice R
    tab_clean, tab_mech, tab_align, tab_gasket, tab_lubric, tab_record = st.tabs([
        "Sec 4. Limpieza", 
        "Sec 5. Inspección Mecánica", 
        "Sec 6. Alineación", 
        "Sec 7. Junta (Gasket)", 
        "Sec 8-10. Lubricación y Pre-ajuste",
        "📋 Sec R. Registro R-2.2-2"
    ])
    
    with tab_clean:
        st.subheader("Limpieza de Superficies de Asentamiento")
        c_1 = st.checkbox("¿Se removieron todos los residuos de juntas anteriores?", value=True)
        brush_type = st.selectbox("Tipo de cepillo / solvente a utilizar:", ["Cepillo de alambre blando (Inox/Bronce)", "Cepillo de acero al carbono", "Solvente químico aprobado"])
        material_flange = st.selectbox("Material de la Brida:", ["Acero Inoxidable (SS)", "Acero al Carbono"])
        
        if material_flange == "Acero Inoxidable (SS)" and brush_type == "Cepillo de acero al carbono":
            st.error("❌ VIOLACIÓN DE LA NORMA (Sec. 4.b.2): No usar cepillos de acero al carbono en bridas de acero inoxidable.")
        else:
            st.success("✔️ Combinación de limpieza conforme.")

    with tab_mech:
        st.subheader("Examen de Superficies y Espárragos")
        coating_thickness = st.number_input("Espesor del recubrimiento en la superficie de apoyo de la tuerca (μm):", min_value=0, value=50, step=10)
        if coating_thickness > 130:
            st.error(f"❌ VIOLACIÓN DE LA NORMA (Sec. 5.4.b.1): El recubrimiento excede los 130 μm (5 mils).")
        else:
            st.success("✔️ Espesor de recubrimiento aceptable.")

    with tab_align:
        st.subheader("Alineación de la Unión Bridada")
        align_check = st.checkbox("¿Se evaluó la alineación inicial y final?", value=True)
        align_rectified = st.radio("¿La desalineación se rectifica con cargas aceptables?", ["Sí", "No"])
        if align_rectified == "No":
            st.error("❌ REQUISITO OBLIGATORIO (Sec. 6.b.3): Reportar para disposición aprobada por ingeniería.")

    with tab_gasket:
        st.subheader("Instalación de la Junta de Sellado")
        gasket_damage = st.checkbox("¿Nueva junta libre de defectos?", value=True)
        gasket_protrusion = st.checkbox("¿La junta sobresale dentro de la trayectoria del flujo?", value=False)
        use_grease = st.checkbox("¿Se aplicó grasa o pasta selladora sobre la junta?", value=False)
        
        if gasket_protrusion:
            st.error("❌ ERROR: La junta no debe proyectarse en la trayectoria del flujo (Sec. 7.b.4).")
        if use_grease:
            st.error("❌ VIOLACIÓN CRÍTICA (Sec. 7.b.9): NO aplicar grasa ni pasta selladora en la junta.")

    with tab_lubric:
        st.subheader("Lubricación e Instalación de Pernos")
        lubric_gasket = st.checkbox("¿Se aplicó lubricante sobre la junta?", value=False)
        if lubric_gasket:
            st.error("❌ VIOLACIÓN DE LA NORMA (Sec. 8.b.5): NO aplicar lubricante en la junta.")
            
        snug_torque = st.number_input("Torque inicial de contacto aplicado (Snug Up) [N·m]:", min_value=0, value=20)
        st.info("💡 **Sec. 9.b.5:** Rango estándar de 15 N·m a 30 N·m, sin exceder el 10% de la carga objetivo.")

    # -------------------------------------------------------------------------
    # PESTAÑA APÉNDICE R: TABLA R-2.2-2 (REGISTRO CORTO DE ASAMBLEA)
    # -------------------------------------------------------------------------
    with tab_record:
        st.subheader("📋 Joint Assembly Record - Short Form (Tabla R-2.2-2)")
        st.caption("Planilla oficial de campo estandarizada para archivo de calidad (QA/QC)")
        
        col_r1, col_r2, col_r3 = st.columns(3)
        with col_r1:
            id_junta = st.text_input("ID / Tag de la Unión (*Joint ID*):", value="FLG-2026-001")
            tag_equipo = st.text_input("Tag del Equipo / Línea:", value="L-3012-8\"-C150")
            
        with col_r2:
            planta_unidad = st.text_input("Planta / Unidad:", value="Planta de Procesos MENFA")
            fecha_asamblea = st.date_input("Fecha de Ensamblaje:", value=date.today())
            
        with col_r3:
            norma_brida = st.text_input("Especificación de Brida:", value="ASME B16.5 Cl 300 WN")
            tipo_componente = st.selectbox(
                "Tipo de Componente:",
                ["Tubería a Tubería (Pipe-to-Pipe)", "Tubería a Válvula", "Tubería a Equipo (Boquilla)", "Tapa Ciega / Blind"]
            )

        st.markdown("---")
        st.markdown("##### Especificación Técnica de Insumos")
        col_i1, col_i2, col_i3 = st.columns(3)
        
        with col_i1:
            tipo_junta = st.selectbox("Tipo de Junta:", ["Espiralada (Spiral Wound - SWG)", "Kammprofile", "RTJ", "Fibra Comprimida / PTFE"])
            mat_junta = st.text_input("Material de Junta / Relleno:", value="SS316L / Grafito")
            
        with col_i2:
            mat_pernos = st.selectbox("Material Espárragos:", ["ASTM A193 B7", "ASTM A193 B16", "ASTM A193 B8", "ASTM A320 L7"])
            cant_tamano = st.text_input("Cantidad x Diámetro - Hilos:", value="8x 3/4\" - 10 UNC")
            
        with col_i3:
            lubricante_app = st.text_input("Lubricante Aprobado (K-factor):", value="Anti-seize base Níquel (K=0.16)")
            metodo_ajuste = st.selectbox("Herramienta de Torque:", ["Torquímetro Manual", "Torquímetro Hidráulico", "Tensionador Hidráulico"])

        st.markdown("---")
        st.markdown("##### Control de Torque y Protocolo de Pases")
        col_t1, col_t2 = st.columns(2)
        
        with col_t1:
            target_tq = st.number_input("Target Torque Aplicado [ft-lb / N·m]:", value=220)
            patron_secuencia = st.selectbox("Patrón de Ajuste:", ["Star Pattern (Estrella ASME PCC-1 Table 3)", "Circular Pass (Pase 4 y 5)"])
            
        with col_t2:
            pases_ok = st.checkbox("¿Se ejecutaron todos los pases requeridos (20%, 60%, 100%, 100% Final)?", value=True)
            check_inspeccion = st.checkbox("¿Inspección dimensional de caras y alineación aprobadas?", value=align_check)

        st.markdown("---")
        st.markdown("##### Responsables y Dictamen Final (Sign-off)")
        col_f1, col_f2 = st.columns(2)
        
        with col_f1:
            st.text_input("Operador Armador:", value=assembler, disabled=True)
            observaciones_campo = st.text_area("Observaciones de Ensamblaje:", value="Montaje ejecutado conforme a especificación sin desviaciones.")
            
        with col_f2:
            supervisor_qa = st.text_input("Inspector QA/QC:", value="Inspector QA/QC - UTN")
            dictamen = st.radio("Dictamen Final de Asamblea:", ["APROBADO (Release)", "RECHAZADO"], index=0)

        if st.button("💾 Guardar Registro Corto R-2.2-2"):
            st.success(f"✅ Registro oficial para la junta {id_junta} guardado en el historial de inspección.")

    st.markdown("---")
    
    # -------------------------------------------------------------------------
    # VALIDACIÓN GLOBAL DE CAMPO Y EVALUACIÓN NORMATIVA
    # -------------------------------------------------------------------------
    if st.button("Validar Procedimiento de Campo", type="primary"):
        es_inoxidable_valido = not (material_flange == "Acero Inoxidable (SS)" and brush_type == "Cepillo de acero al carbono")
        
        if (not use_grease and 
            not lubric_gasket and 
            coating_thickness <= 130 and 
            has_written_proc and 
            not gasket_protrusion and 
            es_inoxidable_valido and 
            align_rectified == "Sí"):
            
            st.success(f"✔️ Procedimiento de campo APROBADO para **{owner}** por **{assembler}**. Cumple plenamente con ASME PCC-1-2022 Secciones 1-10.")
        else:
            st.error("❌ Procedimiento RECHAZADO. Revisá los errores resaltados en las pestañas antes de emitir la aprobación.")

if __name__ == "__main__":
    render_module_1()
