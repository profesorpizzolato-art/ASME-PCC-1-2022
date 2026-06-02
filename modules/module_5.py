# modules/module_5.py
import streamlit as st

def render_module_5():
    st.title("🧪 Module 5: Testing & Disassembly Operations")
    st.caption("Pruebas de Presión y Desarmado Seguro según ASME PCC-1-2022 Sec. 12 & 14")

    tab1, tab2 = st.tabs(["Sec 12. Pruebas de Presión (Testing)", "Sec 14. Desarmado Mecánico (Disassembly)"])

    # --- SECCIÓN 12: TESTING ---
    with tab1:
        st.header("Control de Juntas en Pruebas de Presión")
        st.info("💡 Las pruebas de estanqueidad comúnmente siguen los lineamientos generales de ASME PCC-2, Artículo 501.")
        
        gasket_test_type = st.radio(
            "¿Qué tipo de junta se utilizará para la prueba de presión hidráulica/neumática?",
            ["Junta Definitiva (Diseñada para el servicio final)", "Junta Sustituta / Temporal (Solo para la prueba)"]
        )

        if gasket_test_type == "Junta Sustituta / Temporal (Solo para la prueba)":
            st.error("""
            ⚠️ **ALERTA DE SEGURIDAD CRÍTICA (Sec. 12.b):** El uso de juntas temporales ha causado históricamente **Gasket Blowout** (reventón de junta). 
            La junta o fragmentos de ella pueden convertirse en **proyectiles de alta velocidad**.
            """)
            
            replaced_gasket = st.checkbox("¿Confirmas que la junta temporal SERÁ REEMPLAZADA por la junta definitiva antes de poner el equipo en servicio operativo?")
            if not replaced_gasket:
                st.error("❌ REQUISITO MANDATORIO: No se puede habilitar la planta si no se asegura el reemplazo de la junta temporal por la apta para servicio.")
            else:
                st.success("✔️ Compromiso de reemplazo registrado bajo procedimiento.")
        else:
            st.success("✔️ Excelente práctica. Minimiza el riesgo de fugas en la puesta en marcha.")

    # --- SECCIÓN 14: DISASSEMBLY ---
    with tab2:
        st.header("Evaluación de Desarmado Controlado (Controlled Disassembly)")
        st.write("Ingrese los parámetros mecánicos de la unión para determinar si la norma **exige** un procedimiento controlado:")

        col1, col2, col3 = st.columns(3)
        with col1:
            nps = st.number_input("Tamaño de la Brida (NPS en pulgadas):", min_value=0.5, max_value=60.0, value=26.0, step=1.0)
        with col2:
            thickness = st.number_input("Espesor de la Brida (mm):", min_value=10, max_value=300, value=130, step=5)
        with col3:
            bolt_dia = st.selectbox("Diámetro de los Pernos / Espárragos:", ["Menor a M45 (1-3/4 in.)", "M45 (1-3/4 in.) o Mayor"])

        problematic_history = st.checkbox("¿La junta posee historial de engrane de roscas (Galling) o desarmado problemático? (Sec. 14.a.2)")
        glass_lined = st.checkbox("¿El equipo tiene revestimiento interno delicado (Glass-lined / Lens ring)? (Sec. 14.a.3)")

        # Algoritmo de decisión ASME Sec. 14(a)
        rule_1 = (nps > 24) and (thickness > 125) and (bolt_dia == "M45 (1-3/4 in.) o Mayor")
        
        st.markdown("### 📊 Dictamen del Procedimiento de Desarmado:")
        if rule_1 or problematic_history or glass_lined:
            st.error("🚨 **DESARMADO CONTROLADO MANDATORIO (Sec. 14.a):** Esta unión cumple con los criterios de criticidad. Se DEBE emitir un procedimiento formal de desarmado controlado (Ver Apéndice J, Sección J-7).")
        else:
            st.success("✔️ **Desarmado Estándar:** La junta no cumple los criterios de alta peligrosidad mecánica estructural. Se puede proceder con el protocolo estándar.")

        st.markdown("---")
        st.subheader("⚠️ Instrucciones Obligatorias de Campo para el Técnico (Sec. 14.b):")
        st.markdown("""
        * **Alivio de Tensión:** Mantener un número suficiente de tuercas flojas colocadas hasta que **toda la tensión** haya sido relevada para evitar movimientos bruscos de la tubería (*Pipe Spring*).
        * **Dirección de Escape:** Seleccionar los primeros pernos a aflojar en ubicaciones que **dirijan cualquier liberación de presión residual LEJOS del técnico** (para bridas verticales, comenzar por la parte **superior**, luego la inferior para drenar).
        """)
