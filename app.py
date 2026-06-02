# app.py
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
            st.warning("**Evolución:** En 2013 se llamaba *'Contact Surface'*. Se cambió para diferenciarla con precisión de las caras de apoyo de las tuarcas.")
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

    # Gráfico de la cara de la brida y defecto
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

    st.metric("Cantidad de Pernos Detectados automáticamente por Norma:", f"{num_bolts} Pernos")

    # Gráfico del Círculo de Pernos y secuencia de torque
    def get_sequence(n):
        if n == 4: return [1, 3, 2, 4]
        if n == 8: return [1, 5, 3, 7, 2, 6, 4, 8]
        if n == 12: return [1, 7, 4, 10, 2, 8, 5, 11, 3, 9, 6, 12]
        return list(range(1, n + 1))

    secuencia = get_sequence(num_bolts)
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.add_patch(plt.Circle((0, 0), 100, color='#cfd8dc', fill=True))
    ax.add_patch(plt.Circle((0, 0), 40, color='#ffffff', fill=True))
    
    angulos = np.linspace(0, 2 * np.pi, num_bolts, endpoint=False) + np.pi/2
    for i, theta in enumerate(angulos):
        x, y = 75 * np.cos(theta), 75 * np.sin(theta)
        ax.add_patch(plt.Circle((x, y), 7, color='#37474f', fill=True))
        orden = secuencia.index(i + 1) + 1
        ax.text(x * 1.25, y * 1.25, f"P{i+1}\n(#{orden})", color='blue', fontsize=8, ha='center', va='center', bbox=dict(facecolor='white', alpha=0.7))
        
    ax.set_xlim(-130, 130); ax.set_ylim(-130, 130); ax.set_aspect('equal'); ax.axis('off')
    st.pyplot(fig)

# =============================================================================
# MÓDULO 4: MOTOR DE TORQUE OBJETIVO Y PASES DE CARGA
# =============================================================================
def render_module_4():
    st.title("⚙️ Module 4: Target Torque & Tightening Engine")
    st.caption("Control de Carga, Patrones de Ajuste e Incrementos de Pases (ASME PCC-1-2022 Sec. 10 & 11)")

    col1, col2 = st.columns(2)
    with col1:
        tightening_method = st.selectbox("Método de Ajuste:", ["Torque Controlado", "Tensionado Hidráulico", "Medición de Alargamiento"])
        total_bolts = st.number_input("Cantidad total de pernos:", min_value=4, value=24)
    with col2:
        gasket_type = st.selectbox("Tipo de Junta (Sec. 10.a.2.e):", ["Hard Gasket (RTJ, Metálica)", "Soft Gasket (Grafito, PTFE)"])
        target_torque = st.number_input("Torque Objetivo Final (ft-lb):", min_value=1, value=250)

    if total_bolts >= 48:
        st.error("🚨 ALERTA (Sec. 10.a.2.b / App. J-5): Brida ≥ 48 pernos REQUIERE Agrupamiento (Grouped Bolting).")

    # Tabla dinámica de pases
    p1, p2 = round(target_torque * 0.3), round(target_torque * 0.6)
    pasos = [
        {"Pase": "Pase de Contacto (Snug)", "Torque": "15 a 30 N-m", "Patrón": "Cruz"},
        {"Pase": "Pase 1", "Torque": f"{p1} ft-lb (30%)", "Patrón": "Cruz"},
        {"Pase": "Pase 2", "Torque": f"{p2} ft-lb (60%)", "Patrón": "Cruz"},
        {"Pase": "Pase 3", "Torque": f"{target_torque} ft-lb (100%)", "Patrón": "Cruz"},
    ]
    if "Soft" in gasket_type:
        pasos.append({"Pase": "Pase 4 (Limpieza)", "Torque": f"{target_torque} ft-lb (100%)", "Patrón": "Circular Continuo"})
        st.warning("📢 Exigencia Sec. 10.a.2.e: Junta blanda activa pase circular extra para compensar relajación elástica.")
        
    st.table(pasos)

# =============================================================================
# MÓDULO 5: PRUEBAS DE PRESIÓN Y DESARMADO CRÍTICO
# =============================================================================
def render_module_5():
    st.title("🧪 Module 5: Testing & Disassembly Operations")
    st.caption("Pruebas de Presión y Desarmado Seguro según ASME PCC-1-2022 Sec. 12 & 14")

    tab1, tab2 = st.tabs(["Sec 12. Pruebas de Presión", "Sec 14. Desarmado Mecánico"])
    
    with tab1:
        gasket_test = st.radio("Junta para la prueba de presión:", ["Junta Definitiva", "Junta Temporal / Sustituta"])
        if "Temporal" in gasket_test:
            st.error("⚠️ RIESGO CRÍTICO (Sec. 12.b): Las juntas temporales causan históricamente Gasket Blowout (Proyectiles balísticos).")

    with tab2:
        nps = st.number_input("NPS de la brida:", value=26)
        thickness = st.number_input("Espesor de la brida (mm):", value=130)
        problematic = st.checkbox("¿Historial de engrane de roscas (Galling) o problemas?")
        
        if nps > 24 and thickness > 125 or problematic:
            st.error("🚨 DESARMADO CONTROLADO MANDATORIO (Sec. 14.a): Requierre procedimiento formal de ingeniería (App. J-7).")

# =============================================================================
# MÓDULO 6: CONTROL DE CALIDAD (QA/QC) Y REGISTROS
# =============================================================================
def render_module_6():
    st.title("📊 Module 6: QA/QC Records & Troubleshooting")
    st.caption("Gestión de Registros Técnicos de Montaje (ASME PCC-1-2022 Sec. 13 & App. R)")

    probabilidad = st.select_slider("Probabilidad de Fuga:", options=["Baja", "Media", "Alta"])
    consecuencia = st.select_slider("Consecuencia de Fuga:", options=["Menor", "Moderada", "Crítica"])

    if probabilidad == "Baja" and consecuencia == "Menor":
        record_type = "Short Assembly Record (Registro Corto)"
    elif probabilidad == "Alta" or consecuencia == "Crítica":
        record_type = "Long Assembly Record (Registro Largo Completo)"
    else:
        record_type = "Medium Assembly Record"

    st.warning(f"📋 Tipo de Registro Exigido: {record_type}")

    with st.form("qa_form"):
        joint_id = st.text_input("Tag de la Junta:", value="FLG-101-NPS26")
        inspector = st.text_input("Inspector de QA/QC Responsable:", value="Fabricio Pizzolato")
        submitted = st.form_submit_button("Guardar Registro Técnico")
        if submitted:
            st.success("💾 Registro guardado en la base de datos bajo lineamientos del Appendix R.")
            st.json({"Tag": joint_id, "Inspector": inspector, "Tipo_Registro": record_type, "Fecha": str(date.today())})

# =============================================================================
# MÓDULO 7: MATRIZ DE REFERENCIAS Y NORMAS CRUZADAS (NUEVO)
# =============================================================================
def render_module_7():
    st.title("📚 Module 7: Standards & Reference Matrix")
    st.caption("Filtro Dinámico de Especificaciones Técnicas Cruzadas (ASME PCC-1-2022 Sec. 15)")
    
    st.markdown("""
    De acuerdo con la **Sección 15 de la norma**, el diseño e integridad de una unión empernada depende de múltiples publicaciones
    referenciadas de entidades como **API, ASME y ASTM**. A continuación, interactúe con la matriz para auditar materiales y dimensiones.
    """)
    
    cat_norma = st.selectbox(
        "Seleccione la categoría de consulta normativa (Sec. 15):",
        ["Materiales de Pernos y Tuercas (ASME BPVC Sec II / ASTM)", "Dimensiones de Bridas y Juntas (ASME B16)", "Prácticas de Inspección y Refrentado (API / ASME PCC-2)"]
    )
    
    if "Materiales" in cat_norma:
        st.subheader("Especificaciones de Materiales para Alta Presión / Temperatura")
        mat_sel = st.selectbox(
            "Seleccione el componente para ver su norma de fabricación obligatoria:",
            ["Espárragos de Aleación de Acero (High-Temp)", "Tuercas de Acero al Carbono / Aleado", "Forjas de Acero al Carbono (Bridas comunes)"]
        )
        if "Espárragos" in mat_sel:
            st.info("📌 **Norma de Referencia:** **ASME BPVC Section II - SA-193 / SA-193M**")
            st.write("Aplica a materiales de empernado de aleación y acero inoxidable para servicios de alta presión o temperatura (Ejemplo: Grado B7).")
        elif "Tuercas" in mat_sel:
            st.info("📌 **Norma de Referencia:** **ASME BPVC Section II - SA-194 / SA-194M**")
            st.write("Especificación obligatoria para tuercas aptas para servicios de alta presión y/o alta temperatura (Ejemplo: Grado 2H).")
        elif "Forjas" in mat_sel:
            st.info("📌 **Norma de Referencia:** **ASME BPVC Section II - SA-105 / SA-105M**")
            st.write("Aplica a componentes de tuberías de acero al carbono forjado, incluyendo bridas comunes utilizadas en la industria petrolera.")
            
    elif "Dimensiones" in cat_norma:
        st.subheader("Estándares Dimensionales y Geométricos")
        dim_sel = st.radio(
            "Seleccione el rango de Diámetro Nominal (NPS):",
            ["NPS 1/2 hasta NPS 24", "NPS 26 hasta NPS 60", "Juntas Metálicas / Espiraladas"],
            horizontal=True
        )
        if "NPS 1/2" in dim_sel:
            st.success("📐 **Estándar Mandatorio:** **ASME B16.5** (Pipe Flanges and Flanged Fittings)")
            st.write("Regula las dimensiones, tolerancias y clasificaciones de presión (Class 150 a 2500) para diámetros pequeños y medianos.")
        elif "NPS 26" in dim_sel:
            st.success("📐 **Estándar Mandatorio:** **ASME B16.47** (Large Diameter Steel Flanges)")
            st.write("Regula bridas de gran diámetro utilizadas frecuentemente en equipos de refinerías y torres de proceso.")
        elif "Juntas" in dim_sel:
            st.success("📐 **Estándar Mandatorio:** **ASME B16.20** (Metallic Gaskets for Pipe Flanges)")
            st.write("Especifica las dimensiones de juntas espiraladas (Spiral Wound), chaquetas metálicas y anillos RTJ.")
            
    elif "Inspección" in cat_norma:
        st.subheader("Límites de Acabado y Reparaciones Mecánicas")
        st.markdown("""
        * **Rugosidad de la Cara (Sec. 15.3):** Conforme a **ASME B46.1** (*Surface Texture*), el acabado de la cara de asiento debe cumplir los límites Ra para garantizar que la junta no experimente cizallamiento ni fuga capilar.
        * **Mecanizado en Sitio (Sec. 15.3):** Si los defectos evaluados en el *Módulo 2* exceden los límites, el procedimiento de refrentado mecánico en campo se ejecuta bajo **ASME PCC-2, Artículo 305**.
        * **Instalación de Maquinaria:** Para uniones en equipos rotativos o críticos, se cruzan datos con **API Recommended Practice 686**.
        """)

# =============================================================================
# ENRUTADOR CENTRAL (MAIN ROUTING ENGINE)
# =============================================================================
def main():
    st.sidebar.title("🔧 Simulador ASME PCC-1-2022")
    st.sidebar.caption("Autoría del Software: Fabricio Pizzolato")
    st.sidebar.markdown("---")
    
    modulo_seleccionado = st.sidebar.selectbox(
        "Seleccione un Módulo:",
        [
            "Module 0: Foreword, Glossary & Safety",
            "Module 1: Scope & Field Assembly Procedures (Sec. 1-10)",
            "Module 2: Pre-Assembly Inspection (Sec. 4-6 / App. C-E)",
            "Module 3: Engineering & Components Data (App. H, L, M, N)",
            "Module 4: Target Torque Engine (Sec. 9-11 / App. J, K, O, Q)",
            "Module 5: Testing & Disassembly (Sec. 12, 14)",
            "Module 6: Records & Troubleshooting (Sec. 13 / App. P, R)",
            "Module 7: Standards & Reference Matrix (Sec. 15)"  # <-- Nueva pestaña activa
        ]
    )
    
    if modulo_seleccionado == "Module 0: Foreword, Glossary & Safety":
        render_module_0()
    elif modulo_seleccionado == "Module 1: Scope & Field Assembly Procedures (Sec. 1-10)":
        render_module_1()
    elif modulo_seleccionado == "Module 2: Pre-Assembly Inspection (Sec. 4-6 / App. C-E)":
        render_module_2()
    elif modulo_seleccionado == "Module 3: Engineering & Components Data (App. H, L, M, N)":
        render_module_3()
    elif modulo_seleccionado == "Module 4: Target Torque Engine (Sec. 9-11 / App. J, K, O, Q)":
        render_module_4()
    elif modulo_seleccionado == "Module 5: Testing & Disassembly (Sec. 12, 14)":
        render_module_5()
    elif modulo_seleccionado == "Module 6: Records & Troubleshooting (Sec. 13 / App. P, R)":
        render_module_6()
    elif modulo_seleccionado == "Module 7: Standards & Reference Matrix (Sec. 15)":
        render_module_7()

if __name__ == "__main__":
    main()
