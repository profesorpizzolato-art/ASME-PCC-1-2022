# modules/module_4.py
import streamlit as st

def render_module_4():
    st.title("⚙️ Module 4: Target Torque & Tightening Engine")
    st.caption("Control de Carga, Patrones de Ajuste e Incrementos de Pases (ASME PCC-1-2022 Sec. 10 & 11)")

    # -------------------------------------------------------------------------
    # SECCIÓN A: SELECCIÓN DE MÉTODO DE CONTROL DE CARGA (Sec. 10.a.1)
    # -------------------------------------------------------------------------
    st.header("1. Método de Ajuste y Control de Carga")
    col1, col2 = st.columns(2)
    
    with col1:
        tightening_method = st.selectbox(
            "Seleccione el Método de Ajuste:",
            [
                "Torque Controlado (Torquímetro Manual/Hidráulico)", 
                "Tensionado Hidráulico (Bolt Tensioning)", 
                "Medición de Alargamiento (Bolt Elongation / Stretch)",
                "Células de Carga Directa (Load-Control Measurement)"
            ]
        )
    
    with col2:
        tool_qty = st.radio(
            "Configuración de Herramientas (Sec. 10.a.2.a):",
            ["Single-Tool (Una sola herramienta)", "Multi-Tool (Múltiples herramientas en simultáneo)"],
            horizontal=True
        )

    # Lógica condicional según el método seleccionado
    if "Elongation" in tightening_method or "Alargamiento" in tightening_method:
        st.info("💡 **Práctica Opcional (Sec. 11.b / App. J-3):** Requiere micrómetros de profundidad o ultrasonido para medir el estiramiento físico del espárrago en caliente/frío.")
    elif "Tensionado" in tightening_method:
        st.warning("⚠️ **Nota de Longitud (Sec. 9.a.2):** Recuerde que para tensionado hidráulico, la longitud del espárrago debe sobresalir al menos un diámetro nominal por encima de la tuerca del lado del tensionador.")

    st.markdown("---")

    # -------------------------------------------------------------------------
    # SECCIÓN B: ENTRADAS DE LA BRIDA Y AGRUPAMIENTO DE PERNOS (Sec. 10.a.2.b)
    # -------------------------------------------------------------------------
    st.header("2. Geometría y Agrupamiento de Pernos")
    col3, col4 = st.columns(2)
    
    with col3:
        total_bolts = st.number_input("Cantidad total de pernos en la brida:", min_value=4, max_value=120, value=24, step=4)
    
    with col4:
        # Lógica estricta para bridas grandes (48 o más pernos) según Sec. 10.a.2.b y Apéndice J-5
        if total_bolts >= 48:
            st.error(f"🚨 **ALERTA REQUISITO CRÍTICO (Sec. 10.a.2.b / App. J-5):** Esta brida posee {total_bolts} pernos. Para bridas ≥ 48 pernos se REQUIERE aplicar agrupamiento de pernos (Grouped Bolting) para mitigar la interacción elástica durante el ajuste.")
            grouped_bolting = st.checkbox("¿Aplicar procedimiento de agrupamiento (Grouped Bolting)?", value=True)
        else:
            st.success(f"✔️ Cantidad de pernos ({total_bolts}) estándar. No requiere agrupamiento mandatorio por tamaño.")
            grouped_bolting = False

    st.markdown("---")

    # -------------------------------------------------------------------------
    # SECCIÓN C: PROTOCOLO DE PASES E INCREMENTOS DE CARGA (Sec. 10.a.2.c)
    # -------------------------------------------------------------------------
    st.header("3. Definición del Protocolo de Pases (Tightening Passes)")
    
    gasket_type = st.selectbox(
        "Seleccione el Tipo de Junta (Sec. 10.a.2.e):",
        ["Hard Gasket (Espiralada con anillo, RTJ, Metálica)", "Soft Gasket (Grafito puro, PTFE, Elastómero)"]
    )
    
    st.markdown("### Valores Objetivo Simulados (Apéndice O)")
    col5, col6 = st.columns(2)
    with col5:
        target_torque = st.number_input("Torque Objetivo Final Calculado ($T_{target}$) [ft-lb]:", min_value=1, value=250)
    with col6:
        gap_measurement = st.checkbox("¿Se requiere medición de Gaps entre pases? (Sec. 10.a.2.d / App. J-2)", value=False)

    st.markdown("#### Tabla Dinámica de Pases Automática según Norma")
    
    # Construcción de la matriz de pases estándar (ASME PCC-1 Legacy/Alternative)
    pass_1 = round(target_torque * 0.30)
    pass_2 = round(target_torque * 0.60)
    pass_3 = target_torque
    
    pasos_datos = [
        {"Pase": "Pase de Contacto (Snug)", "Carga / Torque Recomendado": "15 a 30 N·m (Max 10% de la carga)", "Patrón Sugerido": "Cruz / Cruz Modificado", "Control de Gap": "Visual"},
        {"Pase": "Pase 1", "Carga / Torque Recomendado": f"20% a 30% del Target ({pass_1} ft-lb)", "Patrón Sugerido": "Cruz / Cuadrante", "Control de Gap": "Recomendado" if gap_measurement else "N/A"},
        {"Pase": "Pase 2", "Carga / Torque Recomendado": f"50% a 70% del Target ({pass_2} ft-lb)", "Patrón Sugerido": "Cruz / Cuadrante", "Control de Gap": "Recomendado" if gap_measurement else "N/A"},
        {"Pase": "Pase 3", "Carga / Torque Recomendado": f"100% del Target ({pass_3} ft-lb)", "Patrón Sugerido": "Cruz / Cuadrante", "Control de Gap": "Obligatorio" if gap_measurement else "N/A"},
    ]
    
    # Agregar pase extra obligatorio si es Soft Gasket (Sec. 10.a.2.e)
    if gasket_type == "Soft Gasket (Grafito puro, PTFE, Elastómero)":
        pasos_datos.append({
            "Pase": "Pase 4 (Pase de Limpieza Circular)", 
            "Carga / Torque Recomendado": f"100% del Target ({pass_3} ft-lb)", 
            "Patrón Sugerido": "Circular Continuo (Sentido Horario)", 
            "Control de Gap": "Verificación Final"
        })
        st.warning("📢 **Exigencia Sec. 10.a.2.e:** Al utilizar una junta blanda (*Soft Gasket*), se activa un pase circular adicional a torque pleno para compensar la alta relajación térmica y mecánica del material.")
    else:
        pasos_datos.append({
            "Pase": "Pase 4 (Pase de Verificación)", 
            "Carga / Torque Recomendado": f"100% del Target ({pass_3} ft-lb)", 
            "Patrón Sugerido": "Circular Continuo", 
            "Control de Gap": "N/A"
        })

    st.table(pasos_datos)

    # -------------------------------------------------------------------------
    # SECCIÓN D: PRÁCTICAS OPCIONALES ADICIONALES (Sec. 11)
    # -------------------------------------------------------------------------
    st.subheader("⚙️ Prácticas Opcionales Habilitadas para el Procedimiento:")
    col7, col8 = st.columns(2)
    with col7:
        retorque_startup = st.checkbox("¿Incluir Retorque de Arranque en Caliente (Start-up retorque)? (Sec. 11.c / App. J-4)")
    with col8:
        if retorque_startup:
            st.info("💡 **Nota App. J-4:** El retorque en caliente se debe realizar antes de que el sistema alcance la temperatura de operación completa y sin presión residual peligrosa.")

    # Generación de la instrucción formal
    st.markdown("---")
    if st.button("Generar Procedimiento Escrito de Ajuste (Instrucción Técnica)"):
        st.success("📝 **INSTRUCCIÓN GENERADA DE ACUERDO A ASME PCC-1-2022 SECCIÓN 10 & 11**")
        
        texto_procedimiento = f"""
        **MÉTODO DE CONTROL:** {tightening_method} ({tool_qty}).  
        **AJUSTE DE CONTACTO:** Snug-up inicial entre 15 y 30 N-m.  
        **SECUENCIA DE APRIETE:** { "Aplicar agrupamiento de pernos (Apéndice J-5)" if grouped_bolting else "Ajuste estándar en cruz / estrella" }.  
        **TIPO DE JUNTA:** {gasket_type}. Se ejecutarán un total de {len(pasos_datos)} pases secuenciales.  
        """
        st.write(texto_procedimiento)
