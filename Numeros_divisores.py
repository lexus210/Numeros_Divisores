def es_numero_natural(entrada):
    try:
        numero = int(entrada)
        if numero == 0:
            raise ValueError("El número no puede ser cero. Los números naturales son mayores que cero.")
        if numero < 0:
            raise ValueError("El número no es un número natural. Debe ser mayor que cero.")
        return numero
    except ValueError as error:
        print(f"Error: {error}")
        return None


def obtener_divisores(numero):
    divisores = [i for i in range(1, numero + 1) if numero % i == 0]
    return divisores


def main():
    while True:
        entrada = input("Ingrese un número natural: ")
        numero = es_numero_natural(entrada)
        if numero is not None:
            break

    divisores = obtener_divisores(numero)
    print(f"Los divisores de {numero} son: {divisores}")


if __name__ == "__main__":
    main()
