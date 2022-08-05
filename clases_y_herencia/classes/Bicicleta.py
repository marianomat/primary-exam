from clases_y_herencia.classes.Vehiculo import Vehiculo


class Bicicleta(Vehiculo):
    def __init__(self, rodado, tipo, color, velocidad):
        super().__init__(color, velocidad)
        self._rodado = rodado
        self._tipo = tipo

    def __str__(self) -> str:
        return f"Bicicleta {self.get_tipo()} rodado {self.get_rodado()}, color {self.get_color()}, velocidad {self.get_velocidad()}"

    def __eq__(self, obj):
        # checking both objects of same class
        if isinstance(obj, Bicicleta):
            if self.get_velocidad() == obj.get_velocidad():
                return f"{self} es mas veloz"
            else:
                return f"{obj} es mas veloz"

    @classmethod
    def crear_bicicleta(cls):
        return Bicicleta(21, "playera", "roja", 20)

    def get_rodado(self):
        return self._rodado

    def set_rodado(self, rodado):
        self._rodado = rodado

    def get_tipo(self):
        return self._tipo

    def set_tipo(self, tipo):
        self._tipo = tipo

