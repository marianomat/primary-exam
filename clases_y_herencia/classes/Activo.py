class Activo:
    def __init__(self, valor, anios_amortizacion):
        self._valor = valor
        self._anios_amortizacion = anios_amortizacion
        
    def get_valor(self):
        return self._valor


    def set_valor(self, valor):
        self._valor = valor

    def get_anios_amortizacion(self):
        return self._anios_amortizacion

    def set_anios_amortizacion(self, anios_amortizacion):
        self._anios_amortizacion = anios_amortizacion

