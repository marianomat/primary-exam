from clases_y_herencia.classes.Automovil import Automovil
from clases_y_herencia.classes.Avion import Avion
from clases_y_herencia.classes.Barco import Barco
from clases_y_herencia.classes.Bicicleta import Bicicleta

automovil = Automovil.crear_automovil()
avion = Avion.crear_avion()
barco = Barco.crear_barco()
bicicleta = Bicicleta.crear_bicicleta()

print(automovil)
print(avion)
print(barco)
print(bicicleta)

automovil_lento = Automovil(4, "Fiat", "azul", 100, 500000, "5 años")

print("\n Método __eq__ Automovil")
print(automovil_lento == automovil)