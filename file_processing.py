from datetime import datetime
import pandas as pd

# Calcular los trabajadores indeterminados cercanos a cumplir 3 años
def calculated_three_years_workers(df):
    # Calcular días trabajados
    today = pd.Timestamp.today()
    df['DIAS_TRABAJADOS'] = (today - df['FECINGRESO_A']).dt.days

    # Días que faltan para 3 años (1095 días)
    df['DIAS_FALTANTES'] = 1095 - df['DIAS_TRABAJADOS']

    # Clasificar solo entre 7 y 30 días antes de cumplir 3 años
    def clasificar_rango(dias_faltantes):
        if 0 < dias_faltantes <= 7:
            return '< 7 dias'
        elif 7 < dias_faltantes <= 30:
            return '< 1 mes'
        else:
            return None

    df['RANGO_ALERTA'] = df['DIAS_FALTANTES'].apply(clasificar_rango)

    # Filtrar solo los que estén cerca de cumplir 3 años
    df = df[df['RANGO_ALERTA'].notna()]

    less_than_a_week = (df['RANGO_ALERTA'] == '< 7 dias').any()

    return df, less_than_a_week

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
        if days < 10:
            return '< 10 dias'
        elif days < 30:
            return '< 1 mes'
        elif days < 90:
            return '< 3 meses'
        else:
            return None

    df['RANGO_ALERTA'] = df['DIAS_RESTANTES'].apply(clasificar_rango)
    df = df[df['RANGO_ALERTA'].notna()]

    less_than_10_days = (df['RANGO_ALERTA'] == '< 10 dias').any()

    return df, less_than_10_days

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
