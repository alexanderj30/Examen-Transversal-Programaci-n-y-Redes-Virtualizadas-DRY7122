# as_checker.py

def verificar_as(asn):
    if 64512 <= asn <= 65534:
        return "AS privado"
    else:
        return "AS público"

if __name__ == "__main__":
    try:
        as_input = int(input("Ingrese el número de Sistema Autónomo (AS): "))
        resultado = verificar_as(as_input)
        print("Resultado:", resultado)
    except ValueError:
        print("Error: Debe ingresar un número entero.")
