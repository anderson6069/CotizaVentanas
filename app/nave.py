class Nave:
    def __init__(self, ancho_cm, alto_cm):
        self.ancho_cm = ancho_cm
        self.alto_cm = alto_cm

    def calcular_perimetro(self):
        return 2 * (self.ancho_cm + self.alto_cm) / 100  # Convertir a metros

    def calcular_area_vidrio(self):
        return (self.ancho_cm - 1.5 * 2) * (self.alto_cm - 1.5 * 2)  # Restar 1.5 cm de cada lado
