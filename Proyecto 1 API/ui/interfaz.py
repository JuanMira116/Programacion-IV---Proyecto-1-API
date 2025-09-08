
def pedir_datos_usuario():
    print("=== CONSULTA DE INFORMACIÓN EDÁFICA ===")
    departamento = input("Ingrese el departamento: ").strip()
    municipio = input("Ingrese el municipio: ").strip()
    cultivo = input("Ingrese el cultivo: ").strip()
    
    while True:
        try:
            numero_registros = int(input("Ingrese el número de registros a consultar: ").strip())
            if numero_registros <= 0:
                print("Debe ser un número positivo. Intente de nuevo.")
            else:
                break
        except ValueError:
            print("Debe ingresar un número válido.")

    return departamento, municipio, cultivo, numero_registros


def mostrar_resultado(resultado):
    print("\n=== RESULTADO CONSULTA ===")
    print(resultado.to_string(index=False))
    print()