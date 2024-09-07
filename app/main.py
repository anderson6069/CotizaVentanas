from ventana import Ventana

def obtener_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("El valor debe ser mayor que cero.")
            return value
        except ValueError as e:
            print(f"Entrada inválida: {e}. Inténtalo de nuevo.")

def obtener_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError("El valor debe ser mayor que cero.")
            return value
        except ValueError as e:
            print(f"Entrada inválida: {e}. Inténtalo de nuevo.")

def obtener_opcion(prompt, opciones):
    while True:
        value = input(prompt).strip()
        if value not in opciones:
            print(f"Entrada inválida. Debe ser una de las siguientes opciones: {', '.join(opciones)}")
        else:
            return value

def main():
    ancho = obtener_float("Ingrese el ancho de la ventana (cm): ")
    alto = obtener_float("Ingrese el alto de la ventana (cm): ")
    estilo = obtener_opcion("Ingrese el estilo de la ventana (O, XO, OXXO): ", ["O", "XO", "OXXO"])
    acabado = obtener_opcion("Ingrese el tipo de acabado (Pulido, Lacado Brillante, Lacado Mate, Anodizado): ", 
                             ["Pulido", "Lacado Brillante", "Lacado Mate", "Anodizado"])
    vidrio = obtener_opcion("Ingrese el tipo de vidrio (Transparente, Bronce, Azul): ", 
                            ["Transparente", "Bronce", "Azul"])
    esmerilado = obtener_opcion("¿El vidrio tiene esmerilado? (si/no): ", ["si", "no"])
    cantidad = obtener_int("Ingrese la cantidad de ventanas: ")

    ventana = Ventana(ancho, alto, estilo, acabado, vidrio, esmerilado, cantidad)
    costo_total = ventana.calcular_costo_total()

    print(f"El costo total para {cantidad} ventanas es: ${costo_total:,.2f}")

if __name__ == "__main__":
    main()
