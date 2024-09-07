from costo_aluminio import CostoAluminio
from costo_vidrio import CostoVidrio
from costo_otros import CostoOtros
from descuento import Descuento


class Ventana:
    def __init__(self, ancho, alto, estilo, tipo_acabado, tipo_vidrio, esmerilado=False, cantidad=1):
        self.ancho = ancho
        self.alto = alto
        self.estilo = estilo
        self.tipo_acabado = tipo_acabado
        self.tipo_vidrio = tipo_vidrio
        self.esmerilado = esmerilado
        self.cantidad = cantidad

    def calcular_costo(self):
        # Crear instancias de las clases de costos
        costo_aluminio = CostoAluminio(
            self.ancho, self.alto, self.estilo, self.tipo_acabado)
        costo_vidrio = CostoVidrio(
            self.ancho, self.alto, self.tipo_vidrio, self.esmerilado)
        costo_otros = CostoOtros(self.estilo)
        descuento = Descuento(self.cantidad)

        # Calcular costos
        costo_total_aluminio = costo_aluminio.calcular()
        costo_total_vidrio = costo_vidrio.calcular()
        costo_total_otros = costo_otros.calcular()
        descuento_aplicado = descuento.calcular(self.cantidad)

        costo_total = (costo_total_aluminio + costo_total_vidrio +
                       costo_total_otros) * self.cantidad
        costo_total -= descuento_aplicado

        return costo_total
