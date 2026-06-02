# modules/module_6.py
import streamlit as st
from datetime import date

def render_module_6():
    st.title("📊 Module 6: QA/QC Records & Troubleshooting")
    st.caption("Gestión de Registros Técnicos de Montaje e Historial de Fugas (ASME PCC-1-2022 Sec. 13 & App. R, P)")

    # Matriz de Matriz de Criticidad para definir nivel de registro (Sec. 13.b)
    st.header("1. Evaluación de Probabilidad y Consecuencia de Fuga")
    st.info("El nivel de detalle del registro técnico se determina en base a la probabilidad y consecuencia de falla (Apéndice R, para. R-2.2).")
    
    col1, col2 = st.columns(2)
    with col1:
        probabilidad = st.select_slider("Probabilidad de Fuga:", options=["Baja", "Media", "Alta"])
    with col2:
        consecuencia = st.select_slider("Consecuencia de Fuga (HSE / Costo):", options=["Menor", "Moderada", "Crítica"])

    # Determinar longitud del registro
    if probabilidad == "Baja" and consecuencia == "Menor":
        record_type = "Short Assembly Record (Registro Corto - Tabla R-2.2-2)"
    elif probabilidad == "Alta" or Consecuencia == "Crítica":
        record_type = "Long Assembly Record (Registro Largo Completo - Tabla R-2.2-1)"
    else:
        record_type = "Medium-Length Assembly Record (Registro Mediano - Tabla R-2.2-3)"

    st.warning(f"📋 **Tipo de Registro Técnico Exigido:** {record_type}")

    st.markdown("---")
    st.header("2. Formulario Digital de Registro de Montaje")
    
    with st.form("qa_record_form"):
        col_a, col_b = st.columns(2)
        with col_a:
            joint_id = st.text_input("Identificación / Tag de la Junta:", value="FLG-101-NPS26")
            joint_class = st.text_input("Clase / Rating (Ej: Class 300 / 600):", value="Class 300")
            inspector = st.text_input("Inspector de QA/QC Responsable:", value="Fabricio Pizzolato")
            activity_date = st.date_input("Fecha de la Actividad:", date.today())
        with col_b:
            tool_data = st.text_input("Herramienta Utilizada (Modelo / No. Serie / Calibración):", value="Hytorc XL-2000 / Cal-2026")
            target_prestress = st.number_input("Esfuerzo Objetivo de Pre-carga Aplicado (ksi / MPa):", min_value=0, value=45)
            problems = st.text_area("Problemas Imprevistos y Soluciones (Cold spring, tuercas engranadas, etc.):", value="Ninguno. Ajuste uniforme.")

        st.markdown("#### Historial de Fugas Previo (Leak History - Sec. 13.b.8):")
        has_leak_history = st.checkbox("¿Esta unión bridada posee historial previo de fugas?")
        
        # Botón de envío del formulario
        submit_record = st.form_submit_with_submission_id if hasattr(st, "form_submit_with_submission_id") else st.form_submit_button
        submitted = submit_record("Guardar Registro Técnico en Base de Datos")
        
        if submitted:
            st.success(f"💾 Registro guardado exitosamente bajo los lineamientos del **Appendix R** de la ASME PCC-1-2022.")
            st.json({
                "Tag": joint_id, "Clase": joint_class, "Inspector": inspector, "Fecha": str(activity_date),
                "Herramienta": tool_data, "Prestress": target_prestress, "Comentarios": problems, "Nivel_Registro": record_type
            })
