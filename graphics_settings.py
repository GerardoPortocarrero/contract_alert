import importlib
import graphics as myg

# REPORTES
def report_configuration(project_address, graphic_name, df):
    # CONFIGURACION GENERAL
    bar_label = 12
    bar_fontsize = 20
    circle_width = 9
    circle_height = 9
    circle_label = 17
    circle_fontsize = 20
    color_1 = "#00ff0d7a"
    color_2 = "#f1c40f"
    color_3 = "#e74c3c"

    if graphic_name == 'determined_graphic.png':
        myg.circle_graphic(
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
        )
    else:
        myg.barh_graphic(
            project_address,
            graphic_name,
            df,
            bar_label,
            bar_fontsize,
        )

# Funcion principal
def main(project_address, graphic_name, df, document):
    importlib.reload(myg)
    
    # Calling graphic generators
    for report in document['reports']:
        report_configuration(project_address, graphic_name, df)