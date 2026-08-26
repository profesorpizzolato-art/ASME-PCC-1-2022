# =============================================================================
# MÓDULO OPERADOR: GUÍA PASO A PASO Y EJECUCIÓN EN SITIO (ASME PCC-1)
# Autoría y Propiedad de la Documentación: Fabricio Pizzolato
# Institución: MENFA- CAPACITACIONES 
# =============================================================================
import streamlit as st

def render_module_operador():
    st.title("👷 Módulo Operador: Ejecución y Control en Sitio")
    st.caption("Guía Operativa Paso a Paso para el Personal Técnico de Montaje")

    st.subheader("📲 Modo Trabajo en Campo")
    
    # Datos Rápidos del Trabajo
    col1, col2 = st.columns(2)
    with col1:
        tag_linea = st.text_input("Tag de la Línea / Equipo:", value="FLG-401-B")
        torquista = st.text_input("Nombre / ID del Torquista:", value="Operador - Legajo #402")
    with col2:
        herramienta_id = st.text_input("ID / Calibración del Torquímetro:", value="HYT-023 (Cal. Venc: 12/2026)")
        torque_target = st.number_input("Torque Objetivo Configurado [ft-lb]:", value=650.0)

    st.markdown("---")

    # Lista de Chequeo Previo (Pre-Bolting Checklist)
    st.markdown("### 1. Verification Previa (Pre-Assembly Checklist)")
    
    c1, c2 = st.columns(2)
    with c1:
        chk1 = st.checkbox("¿Cara de brida limpia, libre de óxido y sin rayas radiales?", value=True)
        chk2 = st.checkbox("¿Junta nueva verificada (Tipo, clase y dimensiones correctas)?", value=True)
        chk3 = st.checkbox("¿Rosca de espárragos lubricada con pasta anti-seize autorizada?", value=True)
    with c2:
        chk4 = st.checkbox("¿Las tuercas giran suavemente con la mano en toda la longitud?", value=True)
        chk5 = st.checkbox("¿Boca/Socket del tamaño correcto para tuerca pesada (Heavy Hex)?", value=True)
        chk6 = st.checkbox("¿Mangueras e hidráulica sin fugas ni daños de seguridad?", value=True)

    if not (chk1 and chk2 and chk3 and chk4 and chk5 and chk6):
        st.warning("⚠️ **ATENCIÓN OPERADOR:** No inicie el apriete hasta completar todos los chequeos previos de seguridad y limpieza.")

    st.markdown("---")

    # Guía de Pases y Control por Pernos
    st.markdown("### 2. Control de Pases y Torques Aplicados")
    
    pase_actual = st.selectbox("Seleccione el Pase en Ejecución:", [
        "Pase de Contacto (Snug-up: 15 - 30 N·m)",
        "Pase 1 (30% Target - " + str(round(torque_target * 0.3)) + " ft-lb)",
        "Pase 2 (60% Target - " + str(round(torque_target * 0.6)) + " ft-lb)",
        "Pase 3 (100% Target - " + str(round(torque_target)) + " ft-lb)",
        "Pase 4 (Circular Continuo - 100% Target)"
    ])

    st.info("💡 **Recordatorio de Patrón:** Siga la secuencia en cruz / estrella indicada en el diagrama antes de pasar al apriete circular.")

    # Matriz de Marcación Rápida
    num_pernos = st.number_input("Cantidad de Pernos en esta Brida:", min_value=4, max_value=48, value=8, step=4)
    
    st.markdown("**Marcación de Pernos Completados en este Pase:**")
    pernos_completados = 0
    cols = st.columns(4)
    for i in range(1, num_pernos + 1):
        with cols[(i - 1) % 4]:
            if st.checkbox(f"Perno #{i}", key=f"op_perno_{i}"):
                pernos_completados += 1

    progreso = pernos_completados / num_pernos
    st.progress(progreso, text=f"Progreso del Pase: {pernos_completados}/{num_pernos} pernos listos ({int(progreso*100)}%)")

    if pernos_completados == num_pernos:
        st.success("🎉 **Pase Completado.** Avance al siguiente pase según el procedimiento.")
