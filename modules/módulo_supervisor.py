# =============================================================================
# MÓDULO SUPERVISOR: AUDITORÍA Y LIBERACIÓN DE UNIONES (ASME PCC-1)
# Autoría y Propiedad de la Documentación: Fabricio Pizzolato
# Institución: MENFA- CAPACITACIONES 
# =============================================================================
import streamlit as st

def render_module_supervisor():
    st.title("👨‍💼 Módulo Supervisor / Inspector QA-QC")
    st.caption("Auditoría Técnica, Validación Normativa y Aprobación de Uniones Bridadas")

    st.subheader("📊 Panel de Estado del Torque en Obra")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Bridas Intervenidas", "24")
    m2.metric("Aprobadas QC", "21", "+3 hoy")
    m3.metric("Con Observaciones", "2", delta="-1", delta_color="inverse")
    m4.metric("Rechazadas", "1", delta_color="inverse")

    st.markdown("---")

    st.subheader("🔎 Hoja de Liberación y Firma Digital de Junta (Flange Sign-off)")
    
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        tag_brida = st.selectbox("Seleccione Tag de Brida a Auditar:", ["FLG-401-B (Línea Principal)", "FLG-102-A (Entrada Torre)", "FLG-805-C (Intercambiador)"])
        inspector = st.text_input("Nombre del Inspector QC:", value="Ing. Fabricio Pizzolato")
        empresa_qc = st.text_input("Empresa / UTN / IPCL MENFA:", value="IPCL MENFA - Inspección")

    with col_s2:
        st.markdown("**Criterios Norma ASME PCC-1 Auditados:**")
        v1 = st.checkbox("Alineación dentro de tolerancia (Apéndice E)", value=True)
        v2 = st.checkbox("Target Torque calculado según Apéndice O", value=True)
        v3 = st.checkbox("Control de Gaps entre caras verificado (Apéndice J-2)", value=True)
        v4 = st.checkbox("Certificado de Calibración de Herramienta VIGENTE", value=True)

    st.markdown("---")
    st.subheader("📝 Dictamen del Inspector")
    
    observaciones = st.text_area("Observaciones o Comentarios de Liberación:", value="Alineación verificada según Apéndice E. Torque pleno de 650 ft-lb aplicado en 4 pases sin desvíos de gap.")

    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("✅ APROBAR Y LIBERAR UNIÓN (Sign-off)", use_container_width=True):
            if v1 and v2 and v3 and v4:
                st.success(f"✔️ **BRIDA {tag_brida} APROBADA Y LIBERADA.** Registro firmado por {inspector}.")
            else:
                st.error("❌ No se puede liberar la unión: Hay verificaciones normativas pendientes.")

    with col_btn2:
        if st.button("🚫 RECHAZAR / REQUERIR RE TRABAJO", use_container_width=True):
            st.error(f"🚨 **BRIDA {tag_brida} RECHAZADA.** Se ha notificado al equipo de montaje para desarme o mecanizado.")
