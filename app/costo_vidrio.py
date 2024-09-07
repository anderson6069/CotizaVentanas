class CostoAluminio:
    precios_acabado = {
        'Pulido': 50700,
        'Lacado Brillante': 54200,
        'Lacado Mate': 53600,
        'Anodizado': 57300
    }

    def __init__(self, ancho, alto, estilo, tipo_acabado):
        self.ancho = ancho
        self.alto = alto
        self.estilo = estilo
        self.tipo_acabado = tipo_acabado

    def calcular(self):
        # Aquí debes implementar la lógica para calcular el costo basado en el tipo de acabado y dimensiones
        # Por ejemplo:
        costo_por_cm_lineal = CostoAluminio.precios_acabado.get(
            self.tipo_acabado, 0)
        # Cálculo ficticio para ejemplo
        total_cm_lineal = 2 * (self.ancho + self.alto)
        return costo_por_cm_lineal * total_cm_lineal
