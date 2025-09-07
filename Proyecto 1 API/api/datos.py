import pandas as pd

EXCEL_PATH = "resultado_laboratorio_suelo.xlsx"

def cargar_datos():
    try:
        df = pd.read_excel(EXCEL_PATH)
        df.columns = [col.strip() for col in df.columns]

        return df
    except Exception as e:
        print("Error al cargar el archivo Excel:", e)
        return None


def listar_departamentos(df):
    return df["Departamento"].dropna().unique().tolist()


def listar_municipios(df, departamento=None):
    if departamento:
        return (
            df[df["Departamento"].str.upper() == departamento.upper()]["Municipio"]
            .dropna()
            .unique()
            .tolist()
        )
    return df["Municipio"].dropna().unique().tolist()


def listar_cultivos(df, municipio=None):
    if municipio:
        return (
            df[df["Municipio"].str.upper() == municipio.upper()]["Cultivo"]
            .dropna()
            .unique()
            .tolist()
        )
    return df["Cultivo"].dropna().unique().tolist()