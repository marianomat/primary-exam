# ****************************
# Consigna:
# Se debe implementar un código en Python que lea el contenido de varios archivos los
# cuales contienen la siguiente información de entrada (son n archivos cuyo contenido
# son números que vienen ordenados):
# Archivo 1: [1,3,5,7,9,....] Archivo 2: [2,4,6,8,...] Archivo 3: [0,10,20,30,...]
# Y genere un único archivo de salida que contenga una lista ordenada de los valores de
# entrada:
# Ejemplo : Archivo resultado: [0,1,2,3,4,5,6,7,8,9,10…]

# Explicacion algoritmo:

# Al tener listas ordenadas, sólo necesito recorrerlas una vez simultáneam

# Variables necesarias

arr = []  # Lista que contiene las listas de los archivos
arr_last_index = []  # Lista que contiene el indice del ultimo numero colocado en el array_final
total_length = 0  # Cantidad de loops que debe realizar el for, es la sumatoria de elementos de todas las listas
final_list = []  # lista final que se retorna


import ast
import os

# codigo fuente: https://stackoverflow.com/questions/18262293/how-to-open-every-file-in-a-folder
for filename in os.listdir("./archivos"):
    with open(os.path.join("./archivos", filename), 'r') as f:  # open in readonly mode

        # codigo fuente: https://stackoverflow.com/questions/36209980/reading-a-list-stored-in-a-text-file
        # documentacion ast,literal_eval https://docs.python.org/3/library/ast.html#ast.literal_eval
        # Soluciona el problema de que tomaba la list como un String, ahora lo reconoce como list
        arr.append((ast.literal_eval(f.read())))
        f.close()

# Inicializamos los elementos en el indice 0
for i in range(len(arr)):
    arr_last_index.append(0)
    total_length += len(arr[i])

for i in range(total_length - 1):
    min_num_list = []
    for j in range(len(arr)):
        if len(arr[j]) != arr_last_index[j]:
            min_num_list.append(arr[j][arr_last_index[j]])
    min_num = min(min_num_list)
    for j in range(len(arr)):
        if len(arr[j]) > arr_last_index[j] and min_num == arr[j][arr_last_index[j]]:
            if arr_last_index[j] < len(arr[j]): arr_last_index[j] += 1
    final_list.append(min_num)

# Escribir archivo con lista final
f = open("output.txt", "a")
f.write(str(final_list))
f.close()



## Preguntas extra

# 1) ¿Qué es y para qué sirve una clase abstracta? ¿Qué es herencia múltiple?
# Una clase abstracta es una clase que no se instancia por sí sola, sino que es instanciada mediante sus clases hijas.
# Sirve para:
#   1: Obligar la implementación de métodos abstractos en las clases hijas
#   2: Usar como estructura base para objetos que compartan propiedades. Ejemplo: clase abstracta Persona, donde es padre de Empleado y Cliente.
# Ambas comparten atributos como DNI, nombre pero por cuestiones de diseño se decide que nunca se instancia un objeto Persona directamente.
# Herencia multiple consiste en que una clase pueda extender de multiples clases, esto en algunos lenguajes como Java no se permite pero en Python si.
# implementacion en Python:
# class DerivedClassName(Base1, Base2, Base3):
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>
# https://docs.python.org/3/tutorial/classes.html#multiple-inheritance

# Los metodos publicos son funcionalidades que posee una clase los cuales pueden ser invocadas desde afuera del scope de la clase, por ejemplo en otra clase.
# Un metodo privado es aquel que solo peude ser llamado en la clase en la que se define
# En python no existen distinciones entre private y public, entonces para indicar que algo private se utiliza un "_" adelante del metodo o atributo.
# Para que el desarrollador sepa que se debe utilizar dentro de la clase.



