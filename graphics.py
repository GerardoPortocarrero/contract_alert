import matplotlib.pyplot as plt
import os

def circle_graphic(
        project_address,
        graphic_name,
        df,
        circle_width,
        circle_height,
        circle_label,
        circle_fontsize,
        color_1,
        color_2,
        color_3
    ):
    # Conteo por rango en orden específico
    conteo_rangos = df['RANGO_ALERTA'].value_counts().reindex(
        ['< 3 meses', '< 1 mes', '< 1 semana'], fill_value=0
    )

    # Explosión y colores estilo semáforo Coca-Cola
    explode = [0.03, 0.06, 0.1]  # último (más urgente) más separado
    colors = [color_1, color_2, color_3]  # asumido ya definidos

    # 🧠 Visualización mejorada
    fig, ax = plt.subplots(figsize=(circle_width, circle_height))
    wedges, texts, autotexts = ax.pie(
        conteo_rangos,
        colors=colors,
        autopct='%1.1f%%',
        explode=explode,
        startangle=190,
        shadow=False,
        textprops=dict(color="black", fontsize=circle_fontsize),
        wedgeprops=dict(width=0.45, edgecolor='white')  # anillo + separación blanca
    )

    # 💬 Etiquetas más separadas visualmente
    for autotext in autotexts:
        autotext.set_fontsize(circle_fontsize)
        autotext.set_color('black')
        autotext.set_weight('bold')

    # 🏷️ Leyenda clara si se quiere
    ax.legend(
        wedges,
        conteo_rangos.index,
        loc="center left",
        bbox_to_anchor=(0.92, 0.5),
        fontsize=circle_label
    )

    # Espacio para título
    plt.tight_layout(rect=[0, 0, 1, 0.93])

    # Guardar imagen si se desea
    plt.savefig(os.path.join(project_address, graphic_name), dpi=300, bbox_inches='tight', facecolor='white')

    #plt.show()
