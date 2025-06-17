def generar_html_responsive_final(df, cid_imagen):
    colores = {
        '< 1 semana': '#e74c3c',
        '< 1 mes': '#f1c40f',
        '< 3 meses': '#00ff0d7a',
    }

    html = f"""
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                font-family: Arial, sans-serif;
                font-size: 14px;
                background-color: #f5f6fa;
                margin: 0;
                padding: 0;
            }}
            .container {{
                max-width: 850px;
                margin: auto;
                background-color: #fff;
                padding: 15px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0,0,0,0.05);
            }}
            h2 {{
                text-align: center;
                margin-bottom: 20px;
                color: #2c3e50;
            }}
            .image-wrapper {{
                text-align: center;
                margin-bottom: 25px;
            }}
            .image-wrapper img {{
                max-width: 100%;
                height: auto;
                border-radius: 8px;
            }}
            h3 {{
                margin: 20px 0 5px 0;
                padding: 10px;
                color: white;
                border-radius: 5px;
                font-size: 15px;
                text-align: center;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 30px;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: center;
                font-size: 13px;
            }}
            th {{
                background-color: #2c3e50;
                color: white;
            }}
            @media only screen and (max-width: 770px) {{
                body {{
                    font-size: 13px;
                }}
                h3 {{
                    font-size: 14px;
                }}
                .container {{
                    padding: 10px;
                }}
                th, td {{
                    font-size: 12px;
                    padding: 6px;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>📌 Contratos Próximos a Finalizar</h2>

            <div class="image-wrapper">
                <img src="cid:{cid_imagen}" alt="Gráfico de Contratos">
            </div>
    """

    for rango in ['< 1 semana', '< 1 mes', '< 3 meses']:
        df_rango = df[df['RANGO_ALERTA'] == rango]
        if df_rango.empty:
            continue
        columnas = ['PERSONA', 'TIPO_CONTRATO', 'DIAS_RESTANTES']
        tabla_html = df_rango[columnas].to_html(index=False, border=0)

        html += f"""
            <h3 style="background-color:{colores[rango]};">{rango.upper()}</h3>
            {tabla_html}
        """

    html += """
        </div>
    </body>
    </html>
    """
    return html
