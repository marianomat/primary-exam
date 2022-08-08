# ****************************
# Consigna:
# Se debe implementar un código en Python que lea el contenido de varios archivos los
# cuales contienen la siguiente información de entrada (son n archivos cuyo contenido
# son números que vienen ordenados):
# Archivo 1: [1,3,5,7,9,....] Archivo 2: [2,4,6,8,...] Archivo 3: [0,10,20,30,...]
# Y genere un único archivo de salida que contenga una lista ordenada de los valores de
# entrada:
# Ejemplo : Archivo resultado: [0,1,2,3,4,5,6,7,8,9,10…]



# Al tener listas ordenadas, sólo necesito recorrerlas una vez simultáneam

# Variables necesarias

arr = []  # Lista que contiene las listas de los archivos
arr_last_index = []  # Lista que contiene el indice del ultimo numero colocado en el array_final
total_length = 0  # Cantidad de loops que debe realizar el for, es la sumatoria de elementos de todas las listas
final_list = []  # lista final que se retorna


import ast
import os

# codigo fuente: https://stackoverflow.com/questions/18262293/how-to-open-every-file-in-a-folder
for filename in os.listdir("archivos"):
    with open(os.path.join("archivos", filename), 'r') as f:  # open in readonly mode

        # codigo fuente: https://stackoverflow.com/questions/36209980/reading-a-list-stored-in-a-text-file
        # documentacion ast,literal_eval https://docs.python.org/3/library/ast.html#ast.literal_eval
        # Soluciona el problema de que tomaba la list como un String, ahora lo reconoce como list
        arr.append((ast.literal_eval(f.read())))
        f.close()

# Inicializamos los elementos en el indice 0
for i in range(len(arr)):
    arr_last_index.append(0)
    total_length += len(arr[i])

for i in range(total_length):
    min_num_list = []
    for j in range(len(arr)):
        if len(arr[j]) != arr_last_index[j]:
            min_num_list.append(arr[j][arr_last_index[j]])
    min_num = min(min_num_list)
    for j in range(len(arr)):
        if len(arr[j]) > arr_last_index[j] and min_num == arr[j][arr_last_index[j]]:
            if arr_last_index[j] < len(arr[j]):
                arr_last_index[j] += 1
                break
    final_list.append(min_num)

# Escribir archivo con lista final
f = open("../output.txt", "a")
f.write(str(final_list))
f.close()





