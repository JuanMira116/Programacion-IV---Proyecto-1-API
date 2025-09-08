
import pandas as pd
from api import datos

def filtrar_registros(departamento: str, municipio: str, cultivo: str, numero_registros: int) -> pd.DataFrame:
    base_de_datos = datos.cargar_datos()

    registros_filtrados = base_de_datos[
        (base_de_datos["Departamento"].str.upper() == departamento.upper()) &
        (base_de_datos["Municipio"].str.upper() == municipio.upper()) &
        (base_de_datos["Cultivo"].str.upper() == cultivo.upper())
    ]
    
    return registros_filtrados.head(numero_registros)

def calcular_mediana(registros_filtrados):
    columnas_edaficas = [
        "pH agua:suelo 2,5:1,0",
        "Fósforo (P) Bray II mg/kg",
        "Potasio (K) intercambiable cmol(+)/kg"
    ]

    registros_filtrados[columnas_edaficas] = registros_filtrados[columnas_edaficas].apply(pd.to_numeric, errors="coerce")
    medianas = registros_filtrados[columnas_edaficas].median()

    return {
    "Mediana pH": medianas["pH agua:suelo 2,5:1,0"],
    "Mediana Fósforo (P)": medianas["Fósforo (P) Bray II mg/kg"],
    "Mediana Potasio (K)": medianas["Potasio (K) intercambiable cmol(+)/kg"]
    }

def consulta_completa(departamento: str, municipio: str, cultivo: str, numero_registros: int) -> pd.DataFrame:
    registros_filtrados = filtrar_registros(departamento, municipio, cultivo, numero_registros)
    medianas = calcular_mediana(registros_filtrados)

    resumen = pd.DataFrame({
        "Departamento": [departamento],
        "Municipio": [municipio],
        "Cultivo": [cultivo],
        "Topografia": list(registros_filtrados["Topografia"].unique())[:1],
        "Mediana pH": [medianas.get("Mediana pH", None)],
        "Mediana Fósforo (P)": [medianas.get("Mediana Fósforo (P)", None)],
        "Mediana Potasio (K)": [medianas.get("Mediana Potasio (K)", None)]
    })

    return resumen