import pandas as pd

# Ajustar datos del archivo
def adjust_data_file(df):
    # Tomar la fila 1 como nombres de columns
    df.columns = df.iloc[0]
    df.columns = df.columns.str.strip()

    # Eliminar filas innecesarias
    df = df.iloc[1:].reset_index(drop=True)

    return df

# Eliminar todas las columnas excepto las relevantes
def get_relevant_columns(df, file):
    return df[file['relevant_columns']]

# Normalizar fechas para su futuro procesamiento
def normalize_dates(df):
    df['FECINGRESO_A'] = pd.to_datetime(df['FECINGRESO_A'], errors='coerce', dayfirst=False)
    df['FECHAFINCONTRATO'] = pd.to_datetime(df['FECHAFINCONTRATO'], errors='coerce', dayfirst=True)

    return df

# Preparar archivo para analizar
def main(file_address, document):
    df = pd.read_excel(file_address, sheet_name=document['sheet_name'], header=None)

    df = adjust_data_file(df)
    
    df = get_relevant_columns(df, document)

    df = normalize_dates(df)

    return df