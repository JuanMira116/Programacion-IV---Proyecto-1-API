import pandas as pd
from api import datos

def filtrar_registros(departamento: str, municipio: str, cultivo: str, numero_registros: int = 10) -> pd.DataFrame:
    df = datos.cargar_datos()

    df_filtrado = df[
        (df["Departamento"].str.upper() == departamento.upper()) &
        (df["Municipio"].str.upper() == municipio.upper()) &
        (df["Cultivo"].str.upper() == cultivo.upper())
    ]

    return df_filtrado.head(numero_registros)

def calcular_mediana(df):
    columnas_edaficas = [
        "pH agua:suelo 2,5:1,0",
        "Fósforo (P) Bray II mg/kg",
        "Potasio (K) intercambiable cmol(+)/kg"
    ]

    df[columnas_edaficas] = df[columnas_edaficas].apply(pd.to_numeric, errors="coerce")

    medianas = df[columnas_edaficas].median()

    return {
        "Mediana pH": medianas.get("pH agua:suelo 2,5:1,0"),
        "Mediana Fósforo (P)": medianas.get("Fósforo (P) Bray II mg/kg"),
        "Mediana Potasio (K)": medianas.get("Potasio (K) intercambiable cmol(+)/kg")
    }

def consulta_completa(departamento: str, municipio: str, cultivo: str, numero_registros: int = 10) -> pd.DataFrame:
    df_filtrado = filtrar_registros(departamento, municipio, cultivo, numero_registros)
    medianas = calcular_mediana(df_filtrado)

    resumen = pd.DataFrame({
        "Departamento": [departamento],
        "Municipio": [municipio],
        "Cultivo": [cultivo],
        "Topografia": list(df_filtrado["Topografia"].unique())[:1],
        "Mediana pH": [medianas.get("Mediana pH", None)],
        "Mediana Fósforo (P)": [medianas.get("Mediana Fósforo (P)", None)],
        "Mediana Potasio (K)": [medianas.get("Mediana Potasio (K)", None)]
    })

    return resumen