from clases_y_herencia.classes.Vehiculo import Vehiculo


class Barco(Vehiculo):
    def __init__(self, eslora, nombre, color, velocidad):
        super().__init__(color, velocidad)
        self._eslora = eslora
        self._nombre = nombre

    def __str__(self) -> str:
        return f"Barco llamado {self.get_nombre()} con eslora de {self.get_eslora()}, color {self.get_color()}, velocidad {self.get_velocidad()}"

    def __eq__(self, obj):
        # checking both objects of same class
        if isinstance(obj, Barco):
            if self.get_velocidad() == obj.get_velocidad():
                return f"{self} es mas veloz"
            else:
                return f"{obj} es mas veloz"

    @classmethod
    def crear_barco(cls):
        return Barco(60, "Zeus", "gris", 80)

    def get_eslora(self):
        return self._eslora

    def set_eslora(self, eslora):
        self._eslora = eslora

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

