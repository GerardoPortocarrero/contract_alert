# HTML para alertar de contratos cerca a finalizar (10 dias)
def generate_determined_html(df_determined, indetermined, LOGO_AYA):
    colores = {
        '< 10 dias': '#e74c3c',
        '< 1 mes': '#f1c40f',
        '< 3 meses': '#1bc724',
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
            table {{
                width: 100%;
                border-collapse: collapse;
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
            h3 {{
                margin: 20px 0 5px 0;
                padding: 10px;
                color: white;
                border-radius: 5px;
                font-size: 15px;
                text-align: center;
            }}
            .section-title {{
                text-align: center;
                font-size: 20px;
                color: #34495e;
                font-weight: bold;
                margin: 40px 0 10px;
                position: relative;
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
            .divider {{
                margin: 40px auto;
                width: 80%;
                height: 1px;
                background-color: #e0e0e0;
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
        </style>
    </head>
    <body>
        <div class="container">

            <!-- Encabezado con logo y título -->
            <table width="100%" cellpadding="0" cellspacing="0" style="margin-bottom: 10px;">
                <tr>
                    <td width="130" align="left" valign="middle" style="border: none;">
                        <img src="cid:{LOGO_AYA}" alt="Logo" width="200" style="display: block; border: 0; outline: none; text-decoration: none;">
                    </td>
                    <td align="center" valign="middle" style="border: none;">
                        <h1 style="margin: 0; font-size: 28px; color: #2c3e50;">Alerta de Contratos</h1>
                        <p style="margin: 6px 0 0; font-size: 15px; color: #7f8c8d;">Se detectó personal a una semana de finalizar su contrato.</p>
                    </td>
                </tr>
            </table>

            <!-- Separador visual -->
            <div class="divider"></div>

            <!-- Sección: Contratos Próximos a Finalizar -->
            <div class="section-title">📌 Contratos Próximos a Finalizar</div>
    """

    for rango in ['< 10 dias', '< 1 mes', '< 3 meses']:
        df_rango = df_determined[df_determined['RANGO_ALERTA'] == rango]
        if df_rango.empty:
            continue
        columnas = ['PERSONA', 'TIPO_CONTRATO', 'DIAS_RESTANTES']
        tabla_html = df_rango[columnas].to_html(index=False, border=0)
        html += f"""
            <h3 style="background-color:{colores[rango]};">{rango.upper()}</h3>
            {tabla_html}
        """

    html += f"""
            <!-- Separador visual -->
            <div class="divider"></div>

            <!-- Sección: Imagen Contratos Indeterminados -->
            <div class="section-title">📌 Contratos Indeterminados</div>
            <div class="full-width-image-wrapper">
                <img src="cid:{indetermined}" alt="Contratos Indeterminados">
            </div>

        </div>
    </body>
    </html>
    """

    return html


# HTML para alertar de contratos indeterminados (mas de 3 años)
def generate_indetermined_html(df_determined, df_indetermined, indetermined, LOGO_AYA):
    colores = {
        '< 7 dias': '#e74c3c',
        '< 10 dias': '#e74c3c',
        '< 1 mes': '#f1c40f',
        '< 3 meses': '#1bc724',
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
            table {{
                width: 100%;
                border-collapse: collapse;
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
            h3 {{
                margin: 20px 0 5px 0;
                padding: 10px;
                color: white;
                border-radius: 5px;
                font-size: 15px;
                text-align: center;
            }}
            .section-title {{
                text-align: center;
                font-size: 20px;
                color: #34495e;
                font-weight: bold;
                margin: 40px 0 10px;
                position: relative;
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
            .divider {{
                margin: 40px auto;
                width: 80%;
                height: 1px;
                background-color: #e0e0e0;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <!-- Encabezado con logo y título -->
            <table width="100%" cellpadding="0" cellspacing="0" style="margin-bottom: 10px;">
                <tr>
                    <td width="130" align="left" valign="middle" style="border: none;">
                        <img src="cid:{LOGO_AYA}" alt="Logo" width="200" style="display: block; border: 0; outline: none; text-decoration: none;">
                    </td>
                    <td align="center" valign="middle" style="border: none;">
                        <h1 style="margin: 0; font-size: 28px; color: #2c3e50;">Alerta de Contratos</h1>
                        <p style="margin: 6px 0 0; font-size: 15px; color: #7f8c8d;">Se detectó personal a una semana de finalizar su contrato.</p>
                    </td>
                </tr>
            </table>

            <!-- Separador visual -->
            <div class="divider"></div>

            <!-- Sección: Por Cumplir 3 Años -->
            <div class="section-title">📌 Por Cumplir 3 Años</div>
    """

    for rango in ['< 7 dias', '< 1 mes']:
        df_rango = df_indetermined[df_indetermined['RANGO_ALERTA'] == rango]
        if df_rango.empty:
            continue
        columnas = ['PERSONA', 'TIPO_CONTRATO', 'DIAS_TRABAJADOS', 'DIAS_FALTANTES']
        tabla_html = df_rango[columnas].to_html(index=False, border=0)
        html += f"""
            <h3 style="background-color:{colores[rango]};">{rango.upper()}</h3>
            {tabla_html}
        """

    html += f"""
            <!-- Separador visual -->
            <div class="divider"></div>

            <!-- Sección: Contratos Indeterminados -->
            <div class="section-title">📌 Contratos Indeterminados</div>
            <div style="text-align: center;">
                <img src="cid:{indetermined}" alt="Contratos Indeterminados" style="width: 100%; max-width: 100%; height: auto; border-radius: 8px;">
            </div>

            <!-- Separador visual -->
            <div class="divider"></div>

            <!-- Sección: Contratos Determinados -->
            <div class="section-title">📌 Contratos Determinados por Vencer</div>
    """

    for rango in ['< 10 dias', '< 1 mes', '< 3 meses']:
        df_rango = df_determined[df_determined['RANGO_ALERTA'] == rango]
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

