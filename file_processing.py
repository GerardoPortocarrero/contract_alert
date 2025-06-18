from datetime import datetime
import pandas as pd

# Calcular dias trabajados para contratos indeterminados
def calculate_days_worked(df):
    # Calculamos días trabajados
    today = pd.Timestamp.today()
    df['DIAS_TRABAJADOS'] = (today - df['FECINGRESO_A']).dt.days

    return df

# Calcular days faltantes para contratos determinados
def calculate_left_days(df):
    df['FECHAFINCONTRATO'] = pd.to_datetime(df['FECHAFINCONTRATO'])
    today = datetime.today()
    df['DIAS_RESTANTES'] = (df['FECHAFINCONTRATO'] - today).dt.days

    # Clasificar en rangos
    def clasificar_rango(days):
        if days < 7:
            return '< 1 semana'
        elif days < 30:
            return '< 1 mes'
        elif days < 90:
            return '< 3 meses'
        else:
            return None

    df['RANGO_ALERTA'] = df['DIAS_RESTANTES'].apply(clasificar_rango)
    df = df[df['RANGO_ALERTA'].notna()]

    less_than_a_week = (df['RANGO_ALERTA'] == '< 1 semana').any()

    return df, less_than_a_week

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
