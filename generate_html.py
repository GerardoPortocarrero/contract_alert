def generate_html(df, determined, indetermined):
    colores = {
        '< 10 dias': '#e74c3c',
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
                background-color: #f4f6f8;
                margin: 0;
                padding: 0;
            }}
            .container {{
                max-width: 900px;
                margin: auto;
                padding: 20px 30px;
                background-color: #ffffff;
                border-radius: 12px;
                box-shadow: 0 0 15px rgba(0,0,0,0.08);
            }}
            h1 {{
                text-align: center;
                font-size: 30px;
                color: #2c3e50;
                margin-bottom: 5px;
            }}
            .description {{
                text-align: center;
                font-size: 16px;
                color: #7f8c8d;
                margin-bottom: 30px;
            }}
            .section {{
                margin-top: 30px;
                padding-top: 20px;
                border-top: 2px solid #ecf0f1;
            }}
            .section-title {{
                text-align: center;
                font-size: 22px;
                color: #34495e;
                position: relative;
                margin-bottom: 25px;
            }}
            .section-title::after {{
                content: "";
                display: block;
                width: 60px;
                height: 3px;
                background-color: #3498db;
                margin: 8px auto 0 auto;
                border-radius: 2px;
            }}
            .main-content {{
                display: flex;
                flex-wrap: wrap;
                gap: 20px;
                justify-content: center;
                align-items: flex-start;
                border-bottom: 1px solid #ddd;
                padding-bottom: 25px;
            }}
            .image-wrapper {{
                flex: 1 1 300px;
                max-width: 400px;
                text-align: center;
                padding-top: 16px;
            }}
            .image-wrapper img {{
                width: 100%;
                height: auto;
                border-radius: 8px;
            }}
            .tables-wrapper {{
                flex: 1 1 300px;
                max-width: 500px;
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
                margin-bottom: 25px;
            }}
            th, td {{
                border: 1px solid #ccc;
                padding: 6px;
                text-align: center;
                font-size: 13px;
            }}
            th {{
                background-color: #2c3e50;
                color: white;
            }}
            .full-width-image-wrapper {{
                width: 100%;
                text-align: center;
                margin-top: 10px;
            }}
            .full-width-image-wrapper img {{
                width: 100%;
                max-width: 100%;
                height: auto;
                border-radius: 8px;
            }}
            @media only screen and (max-width: 768px) {{
                .main-content {{
                    flex-direction: column;
                    align-items: center;
                }}
                .image-wrapper, .tables-wrapper {{
                    max-width: 100%;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📊 Alerta de Contratos</h1>
            <p class="description">Se detectó personal a una semana de finalizar su contrato.</p>

            <div class="section">
                <div class="section-title">📌 Contratos Próximos a Finalizar</div>
                <div class="main-content">
                    <div class="image-wrapper">
                        <img src="cid:{determined}" alt="Gráfico de Contratos">
                    </div>
                    <div class="tables-wrapper">
    """

    for rango in ['< 10 dias', '< 1 mes', '< 3 meses']:
        df_rango = df[df['RANGO_ALERTA'] == rango]
        if df_rango.empty:
            continue
        columnas = ['PERSONA', 'TIPO_CONTRATO', 'DIAS_RESTANTES']
        tabla_html = df_rango[columnas].to_html(index=False, border=0)
        html += f"""
                        <h3 style="background-color:{colores[rango]};">{rango.upper()}</h3>
                        {tabla_html}
        """

    html += f"""
                    </div>
                </div>
            </div>

            <div class="section">
                <div class="section-title">📌 Contratos Indeterminados</div>
                <div class="full-width-image-wrapper">
                    <img src="cid:{indetermined}" alt="Contratos Indeterminados">
                </div>
            </div>

        </div>
    </body>
    </html>
    """

    return html
