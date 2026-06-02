# modules/module_1.py
import streamlit as st

def render_module_1():
    st.title("📋 Module 1: Scope & Field Assembly Procedures")
    st.caption("Validación de Requisitos de Campo según ASME PCC-1-2022 Secciones 1 a 10")
    
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
    
    tab_clean, tab_mech, tab_align, tab_gasket, tab_lubric = st.tabs([
        "Sec 4. Limpieza", 
        "Sec 5. Inspección Mecánica", 
        "Sec 6. Alineación", 
        "Sec 7. Junta (Gasket)", 
        "Sec 8-10. Lubricación y Pre-ajuste"
    ])
    
    with tab_clean:
        st.subheader("Limpieza de Superficies de Asentamiento")
        c_1 = st.checkbox("¿Se removieron todos los residuos de juntas anteriores?")
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
        align_check = st.checkbox("¿Se evaluó la alineación inicial y final?")
        align_rectified = st.radio("¿La desalineación se rectifica con cargas aceptables?", ["Sí", "No"])
        if align_rectified == "No":
            st.error("❌ REQUISITO OBLIGATORIO (Sec. 6.b.3): Reportar para disposición aprobada por ingeniería.")

    with tab_gasket:
        st.subheader("Instalación de la Junta de Sellado")
        gasket_damage = st.checkbox("¿Nueva junta libre de defectos?")
        gasket_protrusion = st.checkbox("¿La junta sobresale dentro de la trayectoria del flujo?")
        use_grease = st.checkbox("¿Se aplicó grasa o pasta selladora sobre la junta?")
        
        if gasket_protrusion:
            st.error("❌ ERROR: La junta no debe proyectarse en la trayectoria del flujo (Sec. 7.b.4).")
        if use_grease:
            st.error("❌ VIOLACIÓN CRÍTICA (Sec. 7.b.9): NO aplicar grasa ni pasta selladora en la junta.")

    with tab_lubric:
        st.subheader("Lubricación e Instalación de Pernos")
        lubric_gasket = st.checkbox("¿Se aplicó lubricante sobre la junta?")
        if lubric_gasket:
            st.error("❌ VIOLACIÓN DE LA NORMA (Sec. 8.b.5): NO aplicar lubricante en la junta.")
            
        snug_torque = st.number_input("Torque inicial de contacto aplicado (Snug Up) [N·m]:", min_value=0, value=20)
        st.info("💡 **Sec. 9.b.5:** Rango estándar de 15 N·m a 30 N·m, sin exceder el 10% de la carga objetivo.")

    st.markdown("---")
    if st.button("Validar Procedimiento de Campo"):
        if not use_grease and not lubric_gasket and coating_thickness <= 130 and has_written_proc and not gasket_protrusion:
            st.success(f"✔️ Procedimiento de campo aprobado para {owner} por {assembler}.")
        else:
            st.error("❌ Procedimiento rechazado. Revisa las alertas en rojo.")
