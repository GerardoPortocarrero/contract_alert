from datetime import datetime
import pandas as pd

# Calcular dias faltantes para contratos determinados
def calculate_left_days(df):
    df['FECHAFINCONTRATO'] = pd.to_datetime(df['FECHAFINCONTRATO'])
    hoy = datetime.today()
    df['DIAS_RESTANTES'] = (df['FECHAFINCONTRATO'] - hoy).dt.days

    # Clasificar en rangos
    def clasificar_rango(dias):
        if dias < 7:
            return '< 1 semana'
        elif dias < 30:
            return '< 1 mes'
        elif dias < 90:
            return '< 3 meses'
        else:
            return None

    df['RANGO_ALERTA'] = df['DIAS_RESTANTES'].apply(clasificar_rango)
    df = df[df['RANGO_ALERTA'].notna()]

    return df

# Juntar columnas para formar nombre completo
def join_name_and_lastname(df):
    # Limpieza de columnas
    df['TRABAJADOR'] = df['TRABAJADOR'].astype(str).str.replace(r'[^a-zA-Z\s]', '', regex=True).str.strip()
    df['NRODOCIDEN'] = df['NRODOCIDEN'].astype(str).str.replace(r'[^a-zA-Z\s]', '', regex=True).str.strip()

    # Combinar en nueva columna
    df['PERSONA'] = df['NRODOCIDEN'] + " " + df['TRABAJADOR']

    # Elimina columnas originales
    df.drop(['NRODOCIDEN', 'TRABAJADOR'], axis=1, inplace=True)

    return df

# Preparar archivo para procesar
def main(df):
    df = join_name_and_lastname(df)

    return df
