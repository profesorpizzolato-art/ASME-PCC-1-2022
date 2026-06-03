# =============================================================================
# SIMULADOR COMPLETO ASME PCC-1-2022
# Autoría y Propiedad de la Documentación: Fabricio Pizzolato
# Institución: IPCL MENFA - UTN
# =============================================================================
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from datetime import date

# Configuración de página inicial de la plataforma
st.set_page_config(
    page_title="Simulador ASME PCC-1-2022",
    page_icon="🔧",
    layout="wide"
)

# =============================================================================
# MÓDULO 0: PRÓLOGO, GLOSARIO Y SEGURIDAD OPERATIVA
# =============================================================================
def render_module_0():
    st.title("📘 Module 0: Foreword, Glossary & Operational Safety")
    st.caption("Marco Normativo, Terminología ASME PCC-1 y Protocolos de Seguridad Crítica")
    
    st.markdown("""
    Bienvenido al **Simulador de Integridad de Uniones Bridadas**. Este software opera bajo los lineamientos del estándar 
    **ASME PCC-1-2022** (*Pressure Boundary Bolted Flange Joint Assembly*), incorporando las lecciones operativas del histórico ASME PCC-1-2013.
    """)
    
    st.warning("""
    **📢 CAMBIO DE PARADIGMA (Edición 2022):** El título oficial eliminó la frase *'Guidelines for'*. 
    El texto principal se revisó en su totalidad y las recomendaciones ahora se estructuran como **Requisitos Obligatorios**.
    """, icon="⚠️")
    
    tab1, tab2, tab3 = st.tabs(["Ecosistema e Historia", "Glosario Técnico (2013 vs 2022)", "🚨 SEGURIDAD OPERATIVA"])
    
    with tab1:
        st.subheader("Integración de Estándares Industriales")
        st.table({
            "Fase Operativa": ["Montaje y Torque", "Planificación de Inspección", "Evaluación de Defectos", "Reparación Mecánica"],
            "Norma Aplicable": ["ASME PCC-1-2022", "ASME PCC-3 (Risk-Based)", "API 579-1 / ASME FFS-1", "ASME PCC-2"],
            "Estatus en este Simulador": ["ACTIVO (Motor de Cálculo)", "Informativo", "Vinculado al Módulo de Inspección", "Informativo"]
        })
        
    with tab2:
        st.subheader("Glosario Técnico Seleccionado")
        termino = st.selectbox(
            "Seleccione un término del Glosario para evaluar su evolución:",
            ["Seating Surface (Superficie de Asentamiento)", "Target Torque (Torque Objetivo)", "Assembler (Armador / Técnico)", "Elastic Interaction (Interacción Elástica)"]
        )
        if "Seating" in termino:
            st.info("**Definición (2022):** La superficie de la cara de la brida que entra en contacto con la junta para generar el sello.")
            st.warning("**Evolución:** En 2013 se llamaba *'Contact Surface'*. Se cambió para diferenciarla con precisión de las caras de apoyo de las tuercas.")
        elif "Target" in termino:
            st.info("**Definición:** El torque requerido en el pase final para lograr la precarga objetivo sin dañar componentes.")
            st.warning("**Evolución:** En 2013 eran recomendaciones. En 2022, si el Owner no provee valores, el cálculo del Apéndice O es obligatorio.")
        elif "Assembler" in termino:
            st.info("**Definición:** El técnico calificado responsable de la limpieza, inspección, alineación y ajuste en el campo.")
            st.warning("**Evolución:** La norma 2022 exige una certificación formal drástica (Apéndice A) con registro de entrenamiento.")
        elif "Elastic" in termino:
            st.info("**Definición:** Fenómeno donde el ajuste de un espárrago alivia la tensión de los adyacentes por deformación local.")

    with tab3:
        st.header("Protocolos de Seguridad Crítica en Campo")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🛡️ Prevención de Riesgos Mecánicos")
            st.markdown("""
            * **Línea de Fuego (Puntos de Pellizco):** Al usar torquímetros hidráulicos, el brazo de reacción ejerce fuerzas de toneladas métricas. **NUNCA** coloque las manos entre el brazo de reacción y la brida.
            * **Falla por Proyectil:** Un espárrago sobre-tensionado puede cortarse y salir disparado con energía balística. Ningún operario debe pararse de frente al eje del perno.
            """)
        with col2:
            st.subheader("☣️ Control de Fluidos y Presión Residual")
            st.markdown("""
            * **Gasket Blowout (Reventón):** Usar juntas temporales en pruebas de presión genera riesgo de falla catastrófica (Sec. 12). Fragmentos de la junta actúan como proyectiles de alta velocidad.
            * **Apertura Segura (Sec. 14):** Al desarmar, los primeros pernos a aflojar deben ser los del lado **opuesto** a usted, usando la brida como escudo deflector de fluidos atrapados.
            """)
            
        st.markdown("#### 📝 Check-list de Seguridad Obligatorio:")
        seg_1 = st.checkbox("¿El área de trabajo se encuentra vallada y señalizada por alta presión?")
        seg_2 = st.checkbox("¿Se verificó que los brazos de reacción tengan un punto de apoyo plano y seguro?")
        if seg_1 and seg_2:
            st.success("✔️ Controles de seguridad conformes. Puede operar el simulador.")
        else:
            st.error("❌ ALERTA: Prohibido iniciar maniobras de torque sin cumplir los controles de seguridad.")

# =============================================================================
# MÓDULO 1: PROCEDIMIENTOS OBLIGATORIOS DE CAMPO
# =============================================================================
def render_module_1():
    st.title("📋 Module 1: Scope & Field Assembly Procedures")
    st.caption("Validación de Requisitos de Campo según ASME PCC-1-2022 Secciones 1 a 10")
    
    col_a, col_b = st.columns(2)
    with col_a:
        owner = st.text_input("Propietario de la Instalación (Owner):", value="IPCL MENFA")
        gasket_inside = st.radio("¿La junta está enteramente dentro del círculo de pernos? (Sec. 1)", ["Sí", "No"])
    with col_b:
        assembler = st.text_input("Nombre del Armador / Técnico (Assembler):", value="Fabricio Pizzolato")
        has_written_proc = st.checkbox("¿Existe un procedimiento escrito aprobado por el Owner? (Sec. 2a)", value=True)

    st.markdown("---")
    tab_clean, tab_mech, tab_gasket = st.tabs(["Sec 4. Limpieza", "Sec 5. Espesores", "Sec 7. Junta"])
    
    with tab_clean:
        brush_type = st.selectbox("Tipo de cepillo:", ["Cepillo de alambre blando (Inox/Bronce)", "Cepillo de acero al carbono"])
        material_flange = st.selectbox("Material de la Brida:", ["Acero Inoxidable (SS)", "Acero al Carbono"])
        if material_flange == "Acero Inoxidable (SS)" and brush_type == "Cepillo de acero al carbono":
            st.error("❌ VIOLACIÓN (Sec. 4.b.2): No usar cepillos de acero al carbono en bridas de acero inoxidable por contaminación.")

    with tab_mech:
        coating_thickness = st.number_input("Espesor del recubrimiento en la superficie de la tuerca (μm):", min_value=0, value=50)
        if coating_thickness > 130:
            st.error("❌ VIOLACIÓN (Sec. 5.4.b.1): El recubrimiento excede los 130 μm (5 mils).")

    with tab_gasket:
        use_grease = st.checkbox("¿Se aplicó grasa o pasta selladora sobre la junta?")
        if use_grease:
            st.error("❌ VIOLACIÓN CRÍTICA (Sec. 7.b.9): NO aplicar grasa ni pasta selladora en la junta de servicio.")

# =============================================================================
# MÓDULO 2: INSPECCIÓN PRE-MONTAJE Y GRÁFICA DE DEFECTOS
# =============================================================================
def render_module_2():
    st.title("🔍 Module 2: Pre-Assembly Inspection & Flange Face Defects")
    st.caption("Evaluación Analítica y Gráfica de Imperfecciones en la Superficie de Asentamiento (ASME PCC-1-2022 App. D)")

    col1, col2 = st.columns(2)
    with col1:
        gasket_type = st.selectbox("Tipo de Junta Seleccionada:", ["Spiral Wound (Espiralada)", "Ring Joint (RTJ)", "Soft Sheet"])
        defect_direction = st.radio("Orientación del Defecto:", ["Radial", "Circunferencial"], horizontal=True)
    with col2:
        defect_depth = st.number_input("Profundidad máxima medida (mm):", min_value=0.0, max_value=5.0, value=0.15, step=0.05)
        defect_length = st.number_input("Longitud radial o extensión (mm):", min_value=0.0, max_value=100.0, value=12.0, step=1.0)

    max_allowable_depth = 0.76 if "Spiral" in gasket_type else 0.13 if "Ring" in gasket_type else 0.50
    if defect_direction == "Radial":
        max_allowable_depth *= 0.5
        is_radial = True
    else:
        is_radial = False

    is_approved = defect_depth <= max_allowable_depth
    status_text = "✔️ BRIDA ACEPTADA" if is_approved else "❌ BRIDA RECHAZADA (Requiere Reparación ASME PCC-2 Art. 305)"
    st.markdown(f"<h3 style='color:{'green' if is_approved else 'red'}; text-align:center;'>{status_text}</h3>", unsafe_allow_html=True)

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.add_patch(plt.Circle((0, 0), 50, color='gray', fill=False, linestyle='--', linewidth=2))
    ax.add_patch(plt.Circle((0, 0), 30, color='gray', fill=False, linestyle='--', linewidth=2))
    for r in np.linspace(30, 50, 8):
        ax.add_patch(plt.Circle((0, 0), r, color='#e0e0e0', fill=False, linewidth=0.5))
        
    color_d = 'red' if not is_approved else 'orange'
    if is_radial:
        ax.plot([32, 32 + defect_length], [0, 0], color=color_d, linewidth=4, label="Defecto Radial")
    else:
        theta = np.linspace(-0.2, 0.4, 50)
        ax.plot(40 * np.cos(theta), 40 * np.sin(theta), color=color_d, linewidth=4, label="Defecto Circunferencial")
        
    ax.set_xlim(-60, 60); ax.set_ylim(-60, 60); ax.set_aspect('equal'); ax.axis('off')
    st.pyplot(fig)

# =============================================================================
# MÓDULO 3: BASE DE DATOS DE INGENIERÍA Y GRÁFICA DE PERNOS
# =============================================================================
def render_module_3():
    st.title("🔩 Module 3: Engineering & Components Data")
    st.caption("Bases de Datos ASME B16.5 / Pernos PCC-1 y Patrones de Ajuste")

    db_bridas = {
        ("2", "150"): {"pernos": 4, "diam": "5/8", "area": 0.202},
        ("2", "300"): {"pernos": 8, "diam": "5/8", "area": 0.202},
        ("4", "150"): {"pernos": 8, "diam": "5/8", "area": 0.202},
        ("4", "300"): {"pernos": 8, "diam": "3/4", "area": 0.302},
        ("8", "150"): {"pernos": 8, "diam": "3/4", "area": 0.302},
        ("8", "300"): {"pernos": 12, "diam": "7/8", "area": 0.419},
        ("12", "300"): {"pernos": 16, "diam": "1-1/8", "area": 0.693},
        ("24", "300"): {"pernos": 24, "diam": "1-1/2", "area": 1.294},
    }

    col1, col2 = st.columns(2)
    with col1:
        nps_sel = st.selectbox("NPS (Pulgadas):", ["2", "4", "8", "12", "24"])
    with col2:
        class_sel = st.selectbox("Clase de Presión:", ["150", "300"])

    key = (nps_sel, class_sel)
    data = db_bridas.get(key, {"pernos": 16, "diam": "1", "area": 0.551})
    num_bolts = data["pernos"]
    key = (nps_sel, class_sel)
    data = db_bridas.get(key, {"pernos": 16, "diam": "1", "area": 0.551})
    num_bolts = data["pernos"]

    # ESTA ES LA LÍNEA 191 (Debe ir todo corrido sin saltos de línea internos)
    st.metric("Cantidad de Pernos Detectados automáticamente por Norma:", f"{num_bolts} Pernos")

    # Gráfico del Círculo de Pernos y secuencia de torque
    def get_sequence(n):

