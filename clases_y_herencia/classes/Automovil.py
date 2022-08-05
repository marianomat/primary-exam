from clases_y_herencia.classes.Vehiculo import Vehiculo


class Automovil(Vehiculo):
    def __init__(self, puertas, marca, color, velocidad):
        super().__init__(color, velocidad)
        self._puertas = puertas
        self._marca = marca

    def __str__(self) -> str:
           return f"Automóvil de {self.get_puertas()} puertas, marca {self.get_marca()}, color {self.get_color()}, velocidad {self.get_velocidad()}"

    def __eq__(self, obj):
        # checking both objects of same class
        if isinstance(obj, Automovil):
            if self.get_velocidad() == obj.get_velocidad():
                return f"{self} es mas veloz"
            else:
                return f"{obj} es mas veloz"

    @classmethod
    def crear_automovil(cls):
        return Automovil(4, "Peugeot", "Rojo", 170)

    def get_puertas(self):
        return self._puertas

    def set_puertas(self, puertas):
        self._puertas = puertas

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca
