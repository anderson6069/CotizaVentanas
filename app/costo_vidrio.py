class CostoVidrio:
    precios_vidrio = {
        'Transparente': 8.25,
        'Bronce': 9.15,
        'Azul': 12.75
    }
    
    precio_esmerilado = 5.20

    def __init__(self, nave, tipo_vidrio, esmerilado=False):
        self.nave = nave
        self.tipo_vidrio = tipo_vidrio
        self.esmerilado = esmerilado

    def calcular(self):
        area_cm2 = self.nave.calcular_area()
        costo_por_cm2 = CostoVidrio.precios_vidrio.get(self.tipo_vidrio, 0)
        costo_vidrio = area_cm2 * costo_por_cm2
        
        if self.esmerilado:
            costo_vidrio += CostoVidrio.precio_esmerilado
            
        return costo_vidrio
