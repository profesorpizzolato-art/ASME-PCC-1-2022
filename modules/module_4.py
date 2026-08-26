# =============================================================================
# MÓDULO 4: TARGET TORQUE & TIGHTENING ENGINE (ASME PCC-1-2022 SEC. 10 & 11)
# Autoría y Propiedad de la Documentación: Fabricio Pizzolato
# Institución: MENFA-CAPACITACIONES
# =============================================================================
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def calcular_target_torque(diametro_nom_in, hilos_por_pulgada, sy_psi, pct_sy, nut_factor_k):
    """
    Cálculo de Target Torque (ASME PCC-1 Apéndice O / Short-form relation)
    T = (K * D * F) / 12  [ft-lbs]
    """
    D = diametro_nom_in
    # Área de esfuerzo de tensión en roscas UNC / 8UN (sq in)
    a_b = 0.7854 * (D - (0.9743 / hilos_por_pulgada)) ** 2
    
    # Carga de tensión objetivo (lbs)
    target_stress = sy_psi * (pct_sy / 100.0)
    F_preload = target_stress * a_b
    
    # Torque en ft-lbs y N·m
    torque_ft_lbs = (nut_factor_k * D * F_preload) / 12.0
    torque_nm = torque_ft_lbs * 1.35582
    
    return a_b, F_preload, torque_ft_lbs, torque_nm

def dibujar_secuencia_brida(num_pernos=8):
    """ Genera el diagrama de secuencia en cruz para N pernos """
    angles = np.linspace(0, 2 * np.pi, num_pernos, endpoint=False)
    
    fig, ax = plt.subplots(figsize=(4.5, 4.5))
    
    # Cuerpo de la brida
    circle_outer = plt.Circle((0, 0), 1.2, color='#cbd5e1', fill=True)
    circle_inner = plt.Circle((0, 0), 0.6, color='white', fill=True)
    ax.add_patch(circle_outer)
    ax.add_patch(circle_inner)

    # Coordenadas y representación de pernos
    x = 0.9 * np.sin(angles)
    y = 0.9 * np.cos(angles)

    for i in range(num_pernos):
        ax.plot(x[i], y[i], 'o', color='#1e293b', markersize=16)
        ax.text(x[i], y[i], str(i + 1), color='white', weight='bold',
                ha='center', va='center', fontsize=9)

    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.4, 1.4)
    ax.set_aspect('equal')
    ax.axis('off')
    
    return fig

def render_module_4():
    st.title("⚙️ Module 4: Target Torque & Tightening Engine")
    st.caption("Control de Carga, Patrones de Ajuste e Incrementos de Pases (ASME PCC-1-2022 Sec. 10 & 11)")

    # -------------------------------------------------------------------------
    # SECCIÓN DE CÁLCULO DE TARGET TORQUE (APÉNDICE O)
    # -------------------------------------------------------------------------
    st.header("1. Calculadora de Torque Objetivo (*Target Torque* - Apéndice O)")
    st.info("Cálculo del torque objetivo basado en la geometría del espárrago, tensión admisible y condición de fricción.")
    
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        diametro = st.selectbox("Diámetro del Perno (in):", [0.75, 0.875, 1.0, 1.125, 1.25, 1.5], index=2)
        tpi = st.number_input("Hilos por pulgada (TPI / Pitch):", min_value=4, max_value=14, value=8)
        grado_perno = st.selectbox("Material / Grado del Perno:", [
            "ASTM A193 B7 (Sy = 105,000 psi)",
            "ASTM A193 B8 Cl. 1 (Sy = 30,000 psi)",
            "ASTM A320 L7 (Sy = 105,000 psi)"
        ])
        sy = 105000 if ("B7" in grado_perno or "L7" in grado_perno) else 30000

    with col_t2:
        pct_target = st.slider("Precarga Objetivo (% Sy):", 30, 70, 50, help="ASME PCC-1 recomienda típicamente entre 40% y 60%")
        condicion_lub = st.selectbox("Condición de Lubricación (Nut Factor K):", [
            "Excelente - Pasta Anti-seize nueva (K ≈ 0.12)",
            "Buena - Aceite ligero de máquina (K ≈ 0.15)",
            "Regular - Sin lubricante / Seco (K ≈ 0.20)",
            "Mala - Rosca corroída / Usada (K ≈ 0.25)"
        ])
        if "0.12" in condicion_lub: k_factor = 0.12
        elif "0.15" in condicion_lub: k_factor = 0.15
        elif "0.20" in condicion_lub: k_factor = 0.20
        else: k_factor = 0.25

    # Ejecutar cálculo del Apéndice O
    area, precarga, calc_torque_ftlb, calc_torque_nm = calcular_target_torque(diametro, tpi, sy, pct_target, k_factor)

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Área Tensión Rosca", f"{area:.4f} in²")
    m2.metric("Precarga Objetivo", f"{precarga:,.0f} lbs")
    m3.metric("Torque (ft-lbs)", f"{calc_torque_ftlb:,.1f} ft-lb")
    m4.metric("Torque (N·m)", f"{calc_torque_nm:,.1f} N·m")

    if k_factor >= 0.20:
        st.warning("⚠️ **Advertencia de Fricción:** Un factor K elevado consume más del 80% del torque en vencer el rozamiento, reduciendo peligrosamente la precarga efectiva del perno.")

    st.markdown("---")

    # -------------------------------------------------------------------------
    # SECCIÓN A: SELECCIÓN DE MÉTODO DE CONTROL DE CARGA (Sec. 10.a.1)
    # -------------------------------------------------------------------------
    st.header("2. Método de Ajuste y Control de Carga")
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

    if "Elongation" in tightening_method or "Alargamiento" in tightening_method:
        st.info("💡 **Práctica Opcional (Sec. 11.b / App. J-3):** Requiere micrómetros de profundidad o ultrasonido para medir el estiramiento físico del espárrago.")
    elif "Tensionado" in tightening_method:
        st.warning("⚠️ **Nota de Longitud (Sec. 9.a.2):** Para tensionado hidráulico, la longitud del espárrago debe sobresalir al menos un diámetro nominal por encima de la tuerca.")

    st.markdown("---")

    # -------------------------------------------------------------------------
    # SECCIÓN B: ENTRADAS DE LA BRIDA Y DIAGRAMA DE SECUENCIA (Apéndice E)
    # -------------------------------------------------------------------------
    st.header("3. Geometría, Agrupamiento y Patrones (Apéndice E)")
    col3, col4 = st.columns([1, 1])
    
    with col3:
        total_bolts = st.number_input("Cantidad total de pernos en la brida:", min_value=4, max_value=120, value=24, step=4)
        
        if total_bolts >= 48:
            st.error(f"🚨 **ALERTA REQUISITO CRÍTICO (Sec. 10.a.2.b / App. J-5):** Brida con {total_bolts} pernos. Se REQUIERE agrupamiento de pernos (Grouped Bolting) para mitigar la interacción elástica.")
            grouped_bolting = st.checkbox("¿Aplicar procedimiento de agrupamiento (Grouped Bolting)?", value=True)
        else:
            st.success(f"✔️ Cantidad de pernos ({total_bolts}) estándar. No requiere agrupamiento mandatorio por tamaño.")
            grouped_bolting = False

    with col4:
        st.markdown("**Esquema de Numeración de Pernos:**")
        fig_brida = dibujar_secuencia_brida(min(total_bolts, 16))
        st.pyplot(fig_brida)
        if total_bolts > 16:
            st.caption("*Representación gráfica simplificada para las primeras 16 posiciones.")

    st.markdown("---")

    # -------------------------------------------------------------------------
    # SECCIÓN C: PROTOCOLO DE PASES E INCREMENTOS DE CARGA (Sec. 10.a.2.c)
    # -------------------------------------------------------------------------
    st.header("4. Definición del Protocolo de Pases (Tightening Passes)")
    
    gasket_type = st.selectbox(
        "Seleccione el Tipo de Junta (Sec. 10.a.2.e):",
        ["Hard Gasket (Espiralada con anillo, RTJ, Metálica)", "Soft Gasket (Grafito puro, PTFE, Elastómero)"]
    )
    
    st.markdown("### Valores Objetivo Aplicados")
    col5, col6 = st.columns(2)
    with col5:
        target_torque = st.number_input(
            "Torque Objetivo Final Utilizado ($T_{target}$) [ft-lb]:",
            min_value=1.0,
            value=float(round(calc_torque_ftlb, 1)),
            help="Sincronizado automáticamente con el cálculo del Apéndice O."
        )
    with col6:
        gap_measurement = st.checkbox("¿Se requiere medición de Gaps entre pases? (Sec. 10.a.2.d / App. J-2)", value=False)

    st.markdown("#### Tabla Dinámica de Pases Automática según Norma")
    
    pass_1 = round(target_torque * 0.30, 1)
    pass_2 = round(target_torque * 0.60, 1)
    pass_3 = round(target_torque, 1)
    
    pasos_datos = [
        {"Pase": "Pase de Contacto (Snug)", "Carga / Torque Recomendado": "15 a 30 N·m (Max 10% de la carga)", "Patrón Sugerido": "Cruz / Cruz Modificado", "Control de Gap": "Visual"},
        {"Pase": "Pase 1", "Carga / Torque Recomendado": f"20% a 30% del Target ({pass_1} ft-lb)", "Patrón Sugerido": "Cruz / Cuadrante", "Control de Gap": "Recomendado" if gap_measurement else "N/A"},
        {"Pase": "Pase 2", "Carga / Torque Recomendado": f"50% a 70% del Target ({pass_2} ft-lb)", "Patrón Sugerido": "Cruz / Cuadrante", "Control de Gap": "Recomendado" if gap_measurement else "N/A"},
        {"Pase": "Pase 3", "Carga / Torque Recomendado": f"100% del Target ({pass_3} ft-lb)", "Patrón Sugerido": "Cruz / Cuadrante", "Control de Gap": "Obligatorio" if gap_measurement else "N/A"},
    ]
    
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

    st.markdown("---")
    if st.button("Generar Procedimiento Escrito de Ajuste (Instrucción Técnica)"):
        st.success("📝 **INSTRUCCIÓN GENERADA DE ACUERDO A ASME PCC-1-2022 SECCIÓN 10 & 11**")
        
        texto_procedimiento = f"""
        * **MÉTODO DE CONTROL:** {tightening_method} ({tool_qty}).  
        * **TORQUE TARGET CALCULADO (APP. O):** {target_torque} ft-lb ({calc_torque_nm:.1f} N·m) | Factor K: {k_factor}.  
        * **AJUSTE DE CONTACTO:** Snug-up inicial entre 15 y 30 N·m.  
        * **SECUENCIA DE APRIETE (APP. E):** { "Aplicar agrupamiento de pernos (Apéndice J-5)" if grouped_bolting else "Ajuste estándar en cruz / estrella" }.  
        * **TIPO DE JUNTA:** {gasket_type}. Se ejecutarán un total de {len(pasos_datos)} pases secuenciales.  
        """
        st.write(texto_procedimiento)
