
import pandas as pd

ubicacion_excel = "resultado_laboratorio_suelo.xlsx"

def cargar_datos():
    try:
        base_de_datos = pd.read_excel(ubicacion_excel)
        base_de_datos.columns = [col.strip() for col in base_de_datos.columns]

        return base_de_datos
    
    except Exception as e:
        print("Error al cargar el archivo Excel:", e)

        return None

def listar_departamentos(base_de_datos):
    return base_de_datos["Departamento"].dropna().unique().tolist()

def listar_municipios(base_de_datos, departamento=None):
    if departamento:
        return (
            base_de_datos[base_de_datos["Departamento"].str.upper() == departamento.upper()]["Municipio"].dropna().unique().tolist()
        )
    
    return base_de_datos["Municipio"].dropna().unique().tolist()

def listar_cultivos(base_de_datos, municipio=None):
    if municipio:
        return (
            base_de_datos[base_de_datos["Municipio"].str.upper() == municipio.upper()]["Cultivo"].dropna().unique().tolist()
        )
    
    return base_de_datos["Cultivo"].dropna().unique().tolist()