# Función para calcular el área de un círculo dado su radio


def area_circulo(radio):
    import math

    if radio < 0:
        raise ValueError("El radio no puede ser negativo")
    return math.pi * radio**2


# Ejemplo de uso
if __name__ == "__main__":
    radio = 5
    print(f"El área del círculo con radio {radio} es {area_circulo(radio)}")
