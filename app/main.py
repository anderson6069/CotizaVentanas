import sys
from ventana import Ventana

def main():
    # Leer datos de la entrada del usuario
    try:
        ancho = float(input("Ingrese el ancho de la ventana (cm): "))
        alto = float(input("Ingrese el alto de la ventana (cm): "))
        estilo = input("Ingrese el estilo de la ventana (O, XO, OXXO): ")
        tipo_acabado = input("Ingrese el tipo de acabado (Pulido, Lacado Brillante, Lacado Mate, Anodizado): ")
        tipo_vidrio = input("Ingrese el tipo de vidrio (Transparente, Bronce, Azul): ")
        esmerilado = input("¿El vidrio tiene esmerilado? (sí/no): ").strip().lower() == 'sí'
        cantidad = int(input("Ingrese la cantidad de ventanas: "))
    except ValueError as e:
        print(f"Error en los datos ingresados: {e}")
        sys.exit(1)

    # Crear instancia de Ventana
    ventana = Ventana(ancho, alto, estilo, tipo_acabado, tipo_vidrio, esmerilado, cantidad)
    
    # Calcular costo
    costo_total = ventana.calcular_costo()
    
    # Mostrar resultado
    print(f'El costo total para {cantidad} ventanas es: ${costo_total:,.2f}')

if __name__ == '__main__':
    main()