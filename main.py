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

arr1 = [1, 3, 5, 7]
arr2 = [10, 20, 30, 40]
arr3 = [2, 4, 6, 8]

total_length = len(arr1) + len(arr2) + len(arr3)

arr1_last_index = 0
arr2_last_index = 0
arr3_last_index = 0

final_list = []

print(total_length)
# todos con 4 elementos
for i in range(total_length):

    if ((arr1_last_index < 4 and arr2_last_index < 4) and (arr1[arr1_last_index] < arr2[arr2_last_index])) and ( arr3_last_index < 4 and (arr1[arr1_last_index] < arr3[arr3_last_index])):
        final_list.append(arr1[arr1_last_index])
        arr1_last_index += 1
    elif ((arr2_last_index < 4 and arr1_last_index < 4) and (arr2[arr2_last_index] < arr1[arr1_last_index])) and (arr3_last_index < 4 and (arr2[arr2_last_index] < arr3[arr3_last_index])):
        final_list.append(arr2[arr2_last_index])
        arr2_last_index += 1
    elif ((arr3_last_index < 4 and arr1_last_index < 4) and (arr3[arr3_last_index] < arr1[arr1_last_index])) and  (arr2_last_index < 4 and (arr3[arr3_last_index] < arr2[arr2_last_index])):
        final_list.append(arr3[arr3_last_index])
        arr3_last_index += 1


print(final_list)
