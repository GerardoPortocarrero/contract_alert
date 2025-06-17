import matplotlib.pyplot as plt
import os

# Grafico para personas con contrato 'A PLAZO INDETERMINADO'
def format_ym(dias):
    años = dias // 365
    meses = (dias % 365) // 30
    return f"{años}años {meses}meses"

def barh_graphic(
        project_address,
        graphic_name,
        df,
        bar_label,
        bar_fontsize,
):
    # Validación
    if 'DIAS_TRABAJADOS' not in df.columns:
        raise ValueError("Falta la columna 'DIAS_TRABAJADOS'. Ejecuta calculate_days_worked(df) antes.")

    # Top 10
    top10 = df.sort_values(by='DIAS_TRABAJADOS', ascending=False).head(10).copy()
    top10['ETIQUETA_TIEMPO'] = top10['DIAS_TRABAJADOS'].apply(format_ym)

    # Gráfico
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor('white')

    bars = ax.barh(
        top10['PERSONA'],
        top10['DIAS_TRABAJADOS'],
        color='#E41C23',         # Coca-Cola rojo
        edgecolor='none',
        height=0.6
    )

    # Etiquetas al lado derecho
    for bar, etiqueta in zip(bars, top10['ETIQUETA_TIEMPO']):
        ax.text(
            bar.get_width() + 100,
            bar.get_y() + bar.get_height() / 2,
            etiqueta,
            va='center',
            fontsize=bar_fontsize,
            color='#333333'
        )

    # Estética
    ax.set_yticks(range(len(top10)))
    ax.set_yticklabels(top10['PERSONA'], fontsize=bar_label)
    ax.invert_yaxis()
    ax.grid(axis='x', linestyle='--', alpha=0.3)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    plt.tight_layout()

    # Guardar
    if project_address and graphic_name:
        path = f"{project_address}/{graphic_name}.png"
        plt.savefig(path, dpi=300, bbox_inches='tight', facecolor='white')

    plt.show()

# Grafico para personas con contrato 'POR NECESIDADES DEL MERCADO'
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
    explode = [0.03, 0.06, 0.1]
    colors = [color_1, color_2, color_3]

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

    # Estilo de los porcentajes
    for autotext in autotexts:
        autotext.set_fontsize(circle_fontsize)
        autotext.set_color('black')
        autotext.set_weight('bold')

    # Leyenda arriba centrada
    fig.legend(
        wedges,
        conteo_rangos.index,
        loc='upper center',
        bbox_to_anchor=(0.5, 1.05),  # justo encima del círculo
        ncol=3,
        fontsize=circle_label,
        frameon=True,
        fancybox=True,
        shadow=True,
        borderpad=1
    )

    # Ajuste de layout
    plt.subplots_adjust(top=0.9)

    # Guardar imagen
    plt.savefig(os.path.join(project_address, graphic_name), dpi=300, bbox_inches='tight', facecolor='white')
