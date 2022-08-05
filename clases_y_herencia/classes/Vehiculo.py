class Vehiculo:
    def __init__(self, color, velocidad):
        self._color = color
        self._velocidad = velocidad

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_velocidad(self):
        return self._velocidad

    def set_velocidad(self, velocidad):
        self._velocidad = velocidad
