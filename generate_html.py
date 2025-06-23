# HTML para alertar de contratos cerca a finalizar (10 dias)
def generate_determined_html(df_determined, indetermined, LOGO_AYA):
    colores = {
        '< 10 dias': '#e74c3c',
        '< 1 mes': '#f1c40f',
        '< 3 meses': '#1bc724',
    }

    html = f"""
    <html>
    <body style="margin: 0; padding: 0; background-color: #f4f6f8;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#f4f6f8">
      <tr>
        <td align="center" style="padding: 30px;">

          <!-- Contenedor principal -->
          <table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#ffffff" style="border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.05);">
            <tr>
              <td align="center" style="padding: 20px;">
                <img src="cid:{LOGO_AYA}" alt="Logo" width="180" style="display: block;">
              </td>
            </tr>

            <tr>
            <td align="center" style="padding: 0 30px;">
                <h1 style="margin: 0; font-size: 26px; color: #2c3e50;">Alerta de Contratos</h1>
                <p style="margin: 6px 0 12px; font-size: 14px; color: #7f8c8d;">
                Se detectó personal a menos de una semana de finalizar contrato.
                </p>
                <table width="40" height="1" bgcolor="#e0e0e0" style="margin: 0 auto 20px auto;"><tr><td></td></tr></table>
            </td>
            </tr>

            <tr>
              <td style="padding: 0 30px;">
                <table width="100%" cellpadding="0" cellspacing="0" border="0">
                  <tr>
                    <td style="font-size: 18px; color: #34495e; font-weight: bold; text-align: center; padding: 20px 0 10px;">
                      📌 Contratos Próximos a Finalizar
                    </td>
                  </tr>
                  <tr>
                    <td align="center">
                      <table width="60" height="3" bgcolor="#3498db" style="border-radius: 2px;"><tr><td></td></tr></table>
                    </td>
                  </tr>
                </table>
    """

    for rango in ['< 10 dias', '< 1 mes', '< 3 meses']:
        df_rango = df_determined[df_determined['RANGO_ALERTA'] == rango]
        if df_rango.empty:
            continue

        html += f"""
                <h3 style="background-color:{colores[rango]}; color: white; padding: 10px; border-radius: 6px; font-size: 15px; text-align: center; margin: 30px 0 10px;">{rango.upper()}</h3>
                <table width="100%" cellpadding="6" cellspacing="0" style="border-collapse: collapse; font-size: 13px; margin-bottom: 30px;">
                  <tr style="background-color: #2c3e50; color: white;">
                    <th style="border: 1px solid #ccc;">PERSONA</th>
                    <th style="border: 1px solid #ccc;">TIPO CONTRATO</th>
                    <th style="border: 1px solid #ccc;">DÍAS RESTANTES</th>
                  </tr>
        """

        for _, row in df_rango.iterrows():
            html += f"""
                  <tr>
                    <td style="border: 1px solid #ccc; text-align: center;">{row['PERSONA']}</td>
                    <td style="border: 1px solid #ccc; text-align: center;">{row['TIPO_CONTRATO']}</td>
                    <td style="border: 1px solid #ccc; text-align: center;">{row['DIAS_RESTANTES']}</td>
                  </tr>
            """

        html += "</table>"

    html += f"""
                <table width="100%" cellpadding="0" cellspacing="0" border="0">
                  <tr>
                    <td style="font-size: 18px; color: #34495e; font-weight: bold; text-align: center; padding: 20px 0 10px;">
                      📌 Contratos Indeterminados
                    </td>
                  </tr>
                  <tr>
                    <td align="center">
                      <table width="60" height="3" bgcolor="#3498db" style="border-radius: 2px;"><tr><td></td></tr></table>
                    </td>
                  </tr>
                  <tr>
                    <td align="center" style="padding: 20px;">
                      <img src="cid:{indetermined}" alt="Contratos Indeterminados" width="100%" style="display: block; border: 0;">
                    </td>
                  </tr>
                </table>
              </td>
            </tr>

          </table>
        </td>
      </tr>
    </table>
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
    <body style="margin: 0; padding: 0; background-color: #f4f6f8;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#f4f6f8">
      <tr>
        <td align="center" style="padding: 30px;">

          <!-- Contenedor principal -->
          <table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#ffffff" style="border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.05);">
            <tr>
              <td align="center" style="padding: 20px;">
                <img src="cid:{LOGO_AYA}" alt="Logo" width="180" style="display: block;">
              </td>
            </tr>

            <tr>
            <td align="center" style="padding: 0 30px;">
                <h1 style="margin: 0; font-size: 26px; color: #2c3e50;">Alerta de Aniversario</h1>
                <p style="margin: 6px 0 12px; font-size: 14px; color: #7f8c8d;">
                Se detectó personal a una semana de cumplir 3 años.
                </p>
                <table width="40" height="1" bgcolor="#e0e0e0" style="margin: 0 auto 20px auto;"><tr><td></td></tr></table>
            </td>
            </tr>

            <tr>
              <td style="padding: 0 30px;">
                <table width="100%" cellpadding="0" cellspacing="0" border="0">
                  <tr>
                    <td style="font-size: 18px; color: #34495e; font-weight: bold; text-align: center; padding: 20px 0 10px;">
                      📌 Por Cumplir 3 Años
                    </td>
                  </tr>
                  <tr>
                    <td align="center">
                      <table width="60" height="3" bgcolor="#3498db" style="border-radius: 2px;"><tr><td></td></tr></table>
                    </td>
                  </tr>
                </table>
    """

    for rango in ['< 7 dias', '< 1 mes']:
        df_rango = df_indetermined[df_indetermined['RANGO_ALERTA'] == rango]
        if df_rango.empty:
            continue
        html += f"""
                <h3 style="background-color:{colores[rango]}; color: white; padding: 10px; border-radius: 6px; font-size: 15px; text-align: center; margin: 30px 0 10px;">{rango.upper()}</h3>
                <table width="100%" cellpadding="6" cellspacing="0" style="border-collapse: collapse; font-size: 13px; margin-bottom: 30px;">
                  <tr style="background-color: #2c3e50; color: white;">
                    <th style="border: 1px solid #ccc;">PERSONA</th>
                    <th style="border: 1px solid #ccc;">TIPO CONTRATO</th>
                    <th style="border: 1px solid #ccc;">DÍAS TRABAJADOS</th>
                    <th style="border: 1px solid #ccc;">DÍAS FALTANTES</th>
                  </tr>
        """
        for _, row in df_rango.iterrows():
            html += f"""
                  <tr>
                    <td style="border: 1px solid #ccc; text-align: center;">{row['PERSONA']}</td>
                    <td style="border: 1px solid #ccc; text-align: center;">{row['TIPO_CONTRATO']}</td>
                    <td style="border: 1px solid #ccc; text-align: center;">{row['DIAS_TRABAJADOS']}</td>
                    <td style="border: 1px solid #ccc; text-align: center;">{row['DIAS_FALTANTES']}</td>
                  </tr>
            """
        html += "</table>"

    html += f"""
                <table width="100%" cellpadding="0" cellspacing="0" border="0">
                  <tr>
                    <td style="font-size: 18px; color: #34495e; font-weight: bold; text-align: center; padding: 20px 0 10px;">
                      📌 Contratos Indeterminados
                    </td>
                  </tr>
                  <tr>
                    <td align="center">
                      <table width="60" height="3" bgcolor="#3498db" style="border-radius: 2px;"><tr><td></td></tr></table>
                    </td>
                  </tr>
                  <tr>
                    <td align="center" style="padding: 20px;">
                      <img src="cid:{indetermined}" alt="Contratos Indeterminados" width="100%" style="display: block; border: 0;">
                    </td>
                  </tr>
                </table>

                <table width="100%" cellpadding="0" cellspacing="0" border="0">
                  <tr>
                    <td style="font-size: 18px; color: #34495e; font-weight: bold; text-align: center; padding: 20px 0 10px;">
                      📌 Contratos Determinados por Vencer
                    </td>
                  </tr>
                  <tr>
                    <td align="center">
                      <table width="60" height="3" bgcolor="#3498db" style="border-radius: 2px;"><tr><td></td></tr></table>
                    </td>
                  </tr>
                </table>
    """

    for rango in ['< 10 dias', '< 1 mes', '< 3 meses']:
        df_rango = df_determined[df_determined['RANGO_ALERTA'] == rango]
        if df_rango.empty:
            continue
        html += f"""
                <h3 style="background-color:{colores[rango]}; color: white; padding: 10px; border-radius: 6px; font-size: 15px; text-align: center; margin: 30px 0 10px;">{rango.upper()}</h3>
                <table width="100%" cellpadding="6" cellspacing="0" style="border-collapse: collapse; font-size: 13px; margin-bottom: 30px;">
                  <tr style="background-color: #2c3e50; color: white;">
                    <th style="border: 1px solid #ccc;">PERSONA</th>
                    <th style="border: 1px solid #ccc;">TIPO CONTRATO</th>
                    <th style="border: 1px solid #ccc;">DÍAS RESTANTES</th>
                  </tr>
        """
        for _, row in df_rango.iterrows():
            html += f"""
                  <tr>
                    <td style="border: 1px solid #ccc; text-align: center;">{row['PERSONA']}</td>
                    <td style="border: 1px solid #ccc; text-align: center;">{row['TIPO_CONTRATO']}</td>
                    <td style="border: 1px solid #ccc; text-align: center;">{row['DIAS_RESTANTES']}</td>
                  </tr>
            """
        html += "</table>"

    html += """
              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
    </body>
    </html>
    """

    return html
