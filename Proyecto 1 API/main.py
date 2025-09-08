
from ui.interfaz import pedir_datos_usuario, mostrar_resultado
from api.consultas import consulta_completa

def main():
    departamento, municipio, cultivo, numero_registros = pedir_datos_usuario()

    resultado = consulta_completa(
        departamento=departamento,
        municipio=municipio,
        cultivo=cultivo,
        numero_registros=numero_registros
    )

    mostrar_resultado(resultado)

if __name__ == "__main__":
    main()