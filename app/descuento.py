class Descuento:
    umbral = 100
    porcentaje_descuento = 0.10

    def __init__(self, cantidad):
        self.cantidad = cantidad

    def calcular(self, costo_total):
        if self.cantidad > Descuento.umbral:
            return costo_total * Descuento.porcentaje_descuento
        return 0