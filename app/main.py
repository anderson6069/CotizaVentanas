from ventana import Ventana

def main():
    # Solicitar datos del usuario
    ancho = float(input("Ingrese el ancho de la ventana (cm): "))
    alto = float(input("Ingrese el alto de la ventana (cm): "))
    estilo = input("Ingrese el estilo de la ventana (O, XO, OXXO): ")
    acabado = input("Ingrese el tipo de acabado (Pulido, Lacado Brillante, Lacado Mate, Anodizado): ")
    vidrio = input("Ingrese el tipo de vidrio (Transparente, Bronce, Azul): ")
    esmerilado = input("¿El vidrio tiene esmerilado? (sí/no): ")
    cantidad = int(input("Ingrese la cantidad de ventanas: "))

    ventana = Ventana(ancho, alto, estilo, acabado, vidrio, esmerilado, cantidad)
    costo_total = ventana.calcular_costo_total()

    print(f"El costo total para {cantidad} ventanas es: ${costo_total:,.2f}")

if __name__ == "__main__":
    main()
