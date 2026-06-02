# modules/module_2.py
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def render_module_2():
    st.title("🔍 Module 2: Pre-Assembly Inspection & Flange Face Defects")
    st.caption("Evaluación Analítica y Gráfica de Imperfecciones en la Superficie de Asentamiento (ASME PCC-1-2022 App. D)")

    st.markdown("""
    Este módulo evalúa las imperfecciones mecánicas (rayas, golpes, picaduras) presentes en la cara de asiento de la brida. 
    De acuerdo con la **Sección 5.1 y el Apéndice D**, los defectos radiales que atraviesan la superficie de sellado son de máxima criticidad.
    """)

    # -------------------------------------------------------------------------
    # PARTE 1: ENTRADA DE DATOS TÉCNICOS
    # -------------------------------------------------------------------------
    st.header("1. Parámetros Geométricos del Defecto")
    
    col1, col2 = st.columns(2)
    with col1:
        gasket_type = st.selectbox(
            "Tipo de Junta Seleccionada (Determina la tolerancia, App. C/D):",
            ["Spiral Wound (Espiralada con Grafito)", "Ring Joint (RTJ Metálica)", "Soft Sheet (PTFE / Grafito Plano)"]
        )
        defect_direction = st.radio(
            "Orientación de la Imperfección / Raya:",
            ["Radial (Cruza los canales de sellado)", "Circunferencial (Sigue la dirección del mecanizado)"],
            horizontal=True
        )

    with col2:
        defect_depth = st.number_input("Profundidad máxima medida del defecto (mm):", min_value=0.0, max_value=5.0, value=0.15, step=0.05)
        defect_length = st.number_input("Longitud radial o extensión del defecto (mm):", min_value=0.0, max_value=100.0, value=12.0, step=1.0)

    # -------------------------------------------------------------------------
    # PARTE 2: MOTOR DE EVALUACIÓN DE ACUERDO A LAS LÍMITES ASME PCC-1-2022
    # -------------------------------------------------------------------------
    st.markdown("---")
    st.header("2. Evaluación Normativa Automática")

    # Establecemos límites de corte teóricos basados en las tablas del Appendix D (Ej: Tabla D-3)
    max_allowable_depth = 0.76 if "Spiral" in gasket_type else 0.13 if "Ring" in gasket_type else 0.50
    
    # Penalización por defecto radial
    if defect_direction == "Radial (Cruza los canales de sellado)":
        max_allowable_depth = max_allowable_depth * 0.5  # La norma es mucho más estricta con fallas radiales
        is_radial = True
    else:
        is_radial = False

    # Lógica de Dictamen
    if defect_depth > max_allowable_depth:
        status_color = "red"
        status_text = "❌ BRIDA RECHAZADA (Requiere Reparación / Mecanizado según ASME PCC-2 Art. 305)"
        is_approved = False
    else:
        status_color = "green"
        status_text = "✔️ BRIDA ACEPTADA (Imperfección dentro de tolerancias permisibles)"
        is_approved = True

    st.markdown(f"<h3 style='color:{status_color}; text-align:center;'>{status_text}</h3>", unsafe_allow_html=True)

    # Métricas informativas en pantalla
    col_m1, col_m2 = st.columns(2)
    col_m1.metric("Profundidad Medida", f"{defect_depth} mm", delta=f"{round(defect_depth - max_allowable_depth, 3)} mm vs Límite", delta_color="inverse")
    col_m2.metric("Límite Máximo Permitido", f"{round(max_allowable_depth, 3)} mm")

    # -------------------------------------------------------------------------
    # PARTE 3: GENERACIÓN GRÁFICA DEL DEFECTO (DIGITAL TWIN DE LA CARA)
    # -------------------------------------------------------------------------
    st.markdown("---")
    st.header("3. Simulación Gráfica de la Cara de la Brida")
    st.write("Representación esquemática tridimensional/mecanizada del defecto sobre el área de asentamiento de la junta:")

    # Creación del gráfico con Matplotlib
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Dibujar los límites de la superficie de asentamiento (Dos círculos concéntricos)
    r_envolvente_ext = 50
    r_envolvente_int = 30
    
    circle_ext = plt.Circle((0, 0), r_envolvente_ext, color='gray', fill=False, linestyle='--', linewidth=2, label="Límite Externo Asentamiento")
    circle_int = plt.Circle((0, 0), r_envolvente_int, color='gray', fill=False, linestyle='--', linewidth=2, label="Límite Interno Asentamiento")
    ax.add_patch(circle_ext)
    ax.add_patch(circle_int)

    # Dibujar las ranuras de mecanizado fonográfico de fondo (textura de la brida)
    for r in np.linspace(r_envolvente_int, r_envolvente_ext, 10):
        ax.add_patch(plt.Circle((0, 0), r, color='#e0e0e0', fill=False, linestyle='-', linewidth=0.5))

    # Dibujar el defecto simulado en base a los inputs del usuario
    defect_color = 'red' if not is_approved else 'orange'
    
    if is_radial:
        # Falla radial: Línea gruesa que atraviesa de adentro hacia afuera
        # Usamos la longitud provista por el usuario de forma proporcional
        x_coords = [r_envolvente_int + 2, r_envolvente_int + 2 + defect_length]
        y_coords = [0, 0]
        ax.plot(x_coords, y_coords, color=defect_color, linewidth=4, label=f"Defecto Radial ({defect_depth}mm prof.)")
        # Sombreado de afectación
        ax.fill_between(x_coords, [-2, -2], [2, 2], color=defect_color, alpha=0.3)
    else:
        # Falla circunferencial: Un arco que sigue la ranura
        theta = np.linspace(-0.2, 0.4, 50)
        r_defect = (r_envolvente_ext + r_envolvente_int) / 2
        x_coords = r_defect * np.cos(theta)
        y_coords = r_defect * np.sin(theta)
        ax.plot(x_coords, y_coords, color=defect_color, linewidth=4, label=f"Defecto Circunferencial ({defect_depth}mm)")

    # Configuraciones estéticas del plano de la brida
    ax.set_xlim(-60, 60)
    ax.set_ylim(-60, 60)
    ax.set_aspect('equal')
    ax.axis('off') # Remover ejes para apariencia limpia de hardware
    ax.set_title(f"Mapeo de Superficie: {'RECHAZO' if not is_approved else 'APROBADO'}", color=defect_color, fontsize=12, fontweight='bold')
    ax.legend(loc="upper right", fontsize='small')
    
    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)
    
    # Advertencias de reparación si no se aprueba
    if not is_approved:
        st.error("""
        ⚠️ **Acción Recomendada por el Simulador:** Debido a que el defecto excede las tolerancias de la edición 2022, 
        se debe emitir una orden de mecanizado en sitio (*Field Machining*) utilizando una herramienta de refrentado de bridas, 
        asegurando restablecer el acabado fonográfico estándar (serrated finish) de entre 3.2 μm y 6.3 μm Ra (125 a 250 μin AARH).
        """)
