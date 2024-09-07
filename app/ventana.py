from nave import Nave

class Ventana:
    def __init__(self, ancho_cm, alto_cm, estilo, acabado, vidrio, esmerilado, cantidad):
        self.nave = Nave(ancho_cm, alto_cm)
        self.estilo = estilo
        self.acabado = acabado
        self.vidrio = vidrio
        self.esmerilado = esmerilado
        self.cantidad = cantidad

    def calcular_costo_acabado(self):
        acabados = {
            "Pulido": 50700,
            "Lacado Brillante": 54200,
            "Lacado Mate": 53600,
            "Anodizado": 57300
        }
        return self.nave.calcular_perimetro() * acabados[self.acabado]

    def calcular_costo_vidrio(self):
        vidrios = {
            "Transparente": 8.25,
            "Bronce": 9.15,
            "Azul": 12.75
        }
        precio_vidrio = vidrios[self.vidrio]
        if self.esmerilado.lower() == 'sí':
            precio_vidrio += 5.20
        return self.nave.calcular_area_vidrio() * precio_vidrio

    def calcular_costo_esquinas(self):
        return 4 * 4310  # 4 esquinas por ventana

    def calcular_costo_total(self):
        costo_acabado = self.calcular_costo_acabado()
        costo_vidrio = self.calcular_costo_vidrio()
        costo_esquinas = self.calcular_costo_esquinas()
        costo_total_ventana = costo_acabado + costo_vidrio + costo_esquinas
        if self.cantidad > 100:
            costo_total_ventana *= 0.90  # Aplicar descuento del 10%
        return costo_total_ventana * self.cantidad
