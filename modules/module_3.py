# modules/module_3.py
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def render_module_3():
    st.title("🔩 Module 3: Engineering & Components Data")
    st.caption("Base de Datos de Bridas ASME B16.5 / Pernos ASME PCC-1-2022 y Gráfico de Distribución")

    st.markdown("""
    Este módulo centraliza las dimensiones mecánicas y estructurales de la unión bridada. Al seleccionar el diámetro y la serie, 
    el simulador parametriza los datos de ingeniería requeridos para los cálculos de torque del Módulo 4.
    """)

    # -------------------------------------------------------------------------
    # PARTE 1: BASE DE DATOS MAESTRA (Muestra representativa industrial)
    # -------------------------------------------------------------------------
    # Diccionario indexado: (NPS, Class) -> (Num_Pernos, Diam_Perno_In_Nominal, Area_Esfuerzo_sq_in)
    db_bridas = {
        ("2", "150"): {"pernos": 4, "diam": "5/8", "area_indiv": 0.202},
        ("2", "300"): {"pernos": 8, "diam": "5/8", "area_indiv": 0.202},
        ("4", "150"): {"pernos": 8, "diam": "5/8", "area_indiv": 0.202},
        ("4", "300"): {"pernos": 8, "diam": "3/4", "area_indiv": 0.302},
        ("8", "150"): {"pernos": 8, "diam": "3/4", "area_indiv": 0.302},
        ("8", "300"): {"pernos": 12, "diam": "7/8", "area_indiv": 0.419},
        ("12", "300"): {"pernos": 16, "diam": "1-1/8", "area_indiv": 0.693},
        ("24", "300"): {"pernos": 24, "diam": "1-1/2", "area_indiv": 1.294},
    }

    st.header("1. Selección de Componentes Estandarizados")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        nps_sel = st.selectbox("Diámetro Nominal de la Tubería (NPS - Pulgadas):", ["2", "4", "8", "12", "24"])
    with col2:
        class_sel = st.selectbox("Clase de Presión (Rating / Class):", ["150", "300"])
    with col3:
        bolt_material = st.selectbox("Material del Espárrago (ASTM Spec):", ["A193 Grade B7 (Alta resistencia)", "A193 Grade B8 (Inoxidable)"])

    # Búsqueda en la base de datos interna
    key = (nps_sel, class_sel)
    if key in db_bridas:
        data = db_bridas[key]
        num_bolts = data["pernos"]
        bolt_diam = data["diam"]
        root_area = data["area_indiv"]
    else:
        # Failsafe si la combinación no está mapeada en el ejemplo preliminar
        st.warning("⚠️ Combinación no pre-cargada. Usando valores genéricos de ingeniería.")
        num_bolts = 16
        bolt_diam = "1"
        root_area = 0.551

    # Límites elásticos según material (A193 B7 Yield Strength aprox 105 ksi, B8 aprox 30 ksi)
    sy = 105000 if "B7" in bolt_material else 30000 # psi
    max_bolt_load_psi = sy * 0.50 # Límite recomendado del 50% del Yield para torque inicial
    total_area_brida = num_bolts * root_area

    # Presentación de datos técnicos filtrados
    st.markdown("### 📋 Ficha Técnica Estructural de la Unión")
    col_a, col_b, col_c, col_d = st.columns(4)
    col_a.metric("Cantidad de Pernos", f"{num_bolts} u.")
    col_b.metric("Diámetro del Espárrago", f"{bolt_diam} in")
    col_c.metric("Área de Esfuerzo (Total)", f"{round(total_area_brida, 3)} in²")
    col_d.metric("Límite de Carga (50% Sy)", f"{round((max_bolt_load_psi * root_area)/1000, 1)} kips/perno")

    # -------------------------------------------------------------------------
    # PARTE 2: SIMULACIÓN GRÁFICA DEL PATRÓN DE PERNOS Y ORDEN DE TORQUE
    # -------------------------------------------------------------------------
    st.markdown("---")
    st.header("2. Plano de Distribución Geométrica y Patrón de Ajuste")
    st.write("A continuación se genera el plano técnico de la brida con la numeración de apriete recomendada en Cruz (Legacy Cross-Pattern):")

    # Algoritmo de generación de secuencia en cruz simplificado para la gráfica
    def generar_secuencia_cruz(n):
        if n == 4: return [1, 3, 2, 4]
        if n == 8: return [1, 5, 3, 7, 2, 6, 4, 8]
        if n == 12: return [1, 7, 4, 10, 2, 8, 5, 11, 3, 9, 6, 12]
        # Para más pernos, una secuencia secuencial distribuida aproximada
        return list(range(1, n + 1))

    secuencia = generar_secuencia_cruz(num_bolts)

    # Creación del gráfico con Matplotlib
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Dibujar cuerpo de la brida
    r_brida = 100
    r_bc = 75 # Bolt Circle Radius (Círculo de pernos)
    r_interno = 40
    
    brida_body = plt.Circle((0, 0), r_brida, color='#cfd8dc', fill=True, label="Cuerpo Brida")
    pipe_center = plt.Circle((0, 0), r_interno, color='#ffffff', fill=True, label="Diámetro Interno")
    bolt_circle = plt.Circle((0, 0), r_bc, color='black', fill=False, linestyle=':', linewidth=1)
    
    ax.add_patch(brida_body)
    ax.add_patch(pipe_center)
    ax.add_patch(bolt_circle)

    # Calcular posiciones angulares exactas para cada perno
    angulos = np.linspace(0, 2 * np.pi, num_bolts, endpoint=False)
    # Desplazar 90 grados para que el primer perno esté arriba
    angulos = angulos + np.pi/2

    for i, theta in enumerate(angulos):
        x = r_bc * np.cos(theta)
        y = r_bc * np.sin(theta)
        
        # Dibujar el agujero/perno
        perno_g = plt.Circle((x, y), 8, color='#37474f', fill=True)
        centro_g = plt.Circle((x, y), 2, color='white', fill=True)
        ax.add_patch(perno_g)
        ax.add_patch(centro_g)
        
        # Colocar el número de orden de torque en el patrón
        orden_torque = secuencia.index(i + 1) + 1
        ax.text(x * 1.22, y * 1.22, f"P{i+1}\n(#{orden_torque})", 
                color='#1a237e', fontsize=9, fontweight='bold',
                ha='center', va='center',
                bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.2'))

    # Configuración de estética gráfica
    ax.set_xlim(-140, 140)
    ax.set_ylim(-140, 140)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(f"Brida NPS {nps_sel}\" Class {class_sel} - {num_bolts} Pernos\nNúmeros en (#) indican la secuencia de ajuste", 
                 fontsize=11, fontweight='bold', color='#263238')
    
    st.pyplot(fig)

    st.success("✔️ Datos geométricos listos. El Módulo 4 consumirá estos parámetros automáticamente para calcular los ft-lb o N·m finales.")
