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
#
# Al tener listas ordenadas, sólo necesito recorrerlas una vez simultáneam


from math import floor
arr = []
arr_last_index = []

arr1 = [1, 3, 5, 7, 22, 35]
arr2 = [10, 20, 30, 40]
arr3 = [2, 4, 6, 8]
arr4 = [100]

arr.append(arr1)
arr.append(arr2)
arr.append(arr3)
arr.append(arr4)

total_length = 0

for i in range(len(arr)):
    arr_last_index.append(0)
    total_length += len(arr[i])

final_list = []

# todos con 4 elementos
for i in range(total_length):
    min_num_list = []
    for j in range(len(arr)):
        if len(arr[j]) != arr_last_index[j]:
            min_num_list.append(arr[j][arr_last_index[j]])
    min_num = min(min_num_list)
    for j in range(len(arr)):
        if len(arr[j]) > arr_last_index[j] and min_num == arr[j][arr_last_index[j]]:
            if arr_last_index[j] < len(arr[j]): arr_last_index[j] += 1
    final_list.append(min_num)


