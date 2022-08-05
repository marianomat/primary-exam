from clases_y_herencia.classes.Vehiculo import Vehiculo


class Avion(Vehiculo):
    def __init__(self, capacidad, horas_vuelo, color, velocidad):
        super().__init__(color, velocidad)
        self._capacidad = capacidad
        self._horas_vuelo = horas_vuelo

    def __str__(self) -> str:
        return f"AVión con {self.get_horas_vuelo()} horas de vuelo y una capacidad de {self.get_capacidad()}, color {self.get_color()}, velocidad {self.get_velocidad()}"

    def __eq__(self, obj):
        # checking both objects of same class
        if isinstance(obj, Avion):
            if self.get_velocidad() == obj.get_velocidad():
                return f"{self} es mas veloz"
            else:
                return f"{obj} es mas veloz"

    @classmethod
    def crear_avion(cls):
        return Avion(100, 15000, "blanco", 800)

    def get_capacidad(self):
        return self._capacidad

    def set_capacidad(self, capacidad):
        self._capacidad = capacidad

    def get_horas_vuelo(self):
        return self._horas_vuelo

    def set_horas_vuelo(self, horas_vuelo):
        self._horas_vuelo = horas_vuelo


