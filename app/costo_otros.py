class CostoOtros:
    costo_chapa = 16200
    costo_esquinas = 4310

    def __init__(self, nave):
        self.nave = nave

    def calcular(self):
        # Calculamos basado en el tipo de ventana
        # Asumimos que cada ventana lleva una chapa y esquinas
        return CostoOtros.costo_chapa + 4 * CostoOtros.costo_esquinas