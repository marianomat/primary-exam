from clases_y_herencia.classes.Activo import Activo
from clases_y_herencia.classes.Vehiculo import Vehiculo


class Automovil(Activo, Vehiculo):
    def __init__(self, puertas, marca, color, velocidad, valor, anios_amortizacion):
        Activo.__init__(self, valor, anios_amortizacion)
        Vehiculo.__init__(self, color, velocidad)
        self._puertas = puertas
        self._marca = marca

    def __str__(self) -> str:
           return f"Automóvil de {self.get_puertas()} puertas, marca {self.get_marca()}, color {self.get_color()}, velocidad {self.get_velocidad()}, con un valor de ${self.get_valor()} y un periodo amortizable de {self.get_anios_amortizacion()}"

    def __eq__(self, obj):
        # checking both objects of same class
        if isinstance(obj, Automovil):
            if self.get_velocidad() == obj.get_velocidad():
                return f"{self} es mas veloz"
            else:
                return f"{obj} es mas veloz"

    @classmethod
    def crear_automovil(cls):
        return Automovil(4, "Peugeot", "Rojo", 170, 600000, "5 años")

    def get_puertas(self):
        return self._puertas

    def set_puertas(self, puertas):
        self._puertas = puertas

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca
