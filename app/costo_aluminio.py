class CostoAluminio:
    precios_acabado = {
        'Pulido': 50700,
        'Lacado Brillante': 54200,
        'Lacado Mate': 53600,
        'Anodizado': 57300
    }

    def __init__(self, nave, tipo_acabado):
        self.nave = nave
        self.tipo_acabado = tipo_acabado

    def calcular(self):
        costo_por_cm_lineal = CostoAluminio.precios_acabado.get(self.tipo_acabado, 0)
        total_cm_lineal = 2 * (self.nave.ancho + self.nave.alto)
        return costo_por_cm_lineal * total_cm_lineal
