# =========================================================================
    # REVISÁ ESTA FUNCIÓN INTERNA: Todo su contenido debe llevar un nivel más de indentación
    # =========================================================================
    def get_sequence(n):
        if n == 4: 
            return [1, 3, 2, 4]
        if n == 8: 
            return [1, 5, 3, 7, 2, 6, 4, 8]
        if n == 12: 
            return [1, 7, 4, 10, 2, 8, 5, 11, 3, 9, 6, 12]
        if n == 16:
            return [1, 9, 5, 13, 3, 11, 7, 15, 2, 10, 6, 14, 4, 12, 8, 16]
        if n == 24:
            return [1, 13, 7, 19, 4, 16, 10, 22, 2, 14, 8, 20, 5, 17, 11, 23, 3, 15, 9, 21, 6, 18, 12, 24]
        return list(range(1, n + 1))
    # =========================================================================

    secuencia = get_sequence(num_bolts)
    
    # Generación gráfica del patrón de torque
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Dibujar la brida (círculo externo e interno)
    ax.add_patch(plt.Circle((0, 0), 1.2, color='#b0bec5', fill=True, zorder=1))
    ax.add_patch(plt.Circle((0, 0), 0.6, color='white', fill=True, zorder=2))
    
    # Círculo de centros de pernos
    angles = np.linspace(0, 2 * np.pi, num_bolts, endpoint=False)
    # Ajuste para que el perno 1 empiece arriba (90 grados)
    angles = angles + (np.pi / 2) - angles[0]
    
    x_bolts = 0.9 * np.cos(angles)
    y_bolts = 0.9 * np.sin(angles)
    
    # Dibujar pernos y numeración de secuencia
    for i in range(num_bolts):
        # Dibujar el perno físico
        ax.add_patch(plt.Circle((x_bolts[i], y_bolts[i]), 0.08, color='#37474f', fill=True, zorder=3))
        # Colocar el número de secuencia de apriete
        ax.text(
            x_bolts[i] * 1.15, y_bolts[i] * 1.15, 
            str(secuencia[i]), 
            color='#d32f2f', weight='bold', fontsize=12,
            ha='center', va='center', zorder=4
        )
        # Identificador físico de posición de perno (pequeño y sutil)
        ax.text(
            x_bolts[i], y_bolts[i], 
            f"P{i+1}", 
            color='white', fontsize=7,
            ha='center', va='center', zorder=5
        )

    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')
    st.pyplot(fig)
    
    st.info("💡 **Nota pedagógica:** Los números en **rojo** indican la secuencia de ajuste recomendada (Patrón de Estrella Cruzada).")
