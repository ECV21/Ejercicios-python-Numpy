# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 15:58:21 2023

@author: eduar
"""

# Resumen de numpy

import numpy as np

#creación de un arraglo de DOS dimensiones
valoraciones = np.array([[8,7,8,5], [2,6,8,1], [8,8,9,5]]) #matrz de 3x4
valoraciones
valoraciones[1] #ver solo la fila de index 1
valoraciones[1:3] #ver filas con index 1 y 2

# Acceder a los elementos del arreglo:
valoraciones[0][1] # Primer elemnto de 1ra dimensión(FILAS); y segundo elemento de segunda dimension (COLUMNAS)
valoraciones[0,1] # otra fomra de acceder

valoraciones[2][2] # 3ra fila(PRIMERA DIMENSION) y 3ra columna (SEGUNDA DIMENSION) = 9
valoraciones[2,2] # Otra forma de aceder

#modificar fila completa de un array
valoraciones[0]=123
valoraciones
valoraciones.shape # 3 filas 4 columnas



# AREGLO con TRES Dimeniosnes
valoraciones2 = np.array([[[8,7,8,5], [2,5,5,2]], [[2,6,8,4], [8,9,7.7,6]], [[8,8,9,3.9], [10,9,10,8]]])
valoraciones2
# 3 clientes (FILAS EXTERIORES); DIMENSION 1
# 2 años por cliente (FILAS INTERIORES de cada cliente): DIUMENSION 2
# 4 PRODUCTOS (COLUMNAS): DIMENSION 3

# Acceder al elemento 7.7 --> PRIMERO filas (exterio-->interior) y SEGUNDO Columnas
valoraciones2[1,1,2] # FILA exterior 2(DIMENSION 1), fila interior 2(DIMENSION 2) y columna 3 (DIMENSION 3)
valoraciones2[2, 0, 3] ## acceder al elemento "3.9"


# ARREGLOS VACÍOS, de TRES dimensiones
np.zeros((3,2,4)) #arreglo de CEROS de 3 dimensiones 


# SUMAR arrays con misma dimension:
valoraciones2 + np.ones((3,2,4))

# PROMEDIO del array:
np.mean(valoraciones2)


# PROMEDIO del array en una dimensión particular:
np.mean(valoraciones2, axis = 0)

# CONVERTIR UNA LISTA EN UN ARRAY de dimensiones específicas:
np.reshape([1,2,3,4,5,6,7,8,9,10,11,12], (3,2,2)) # tres dimensiones, dos filas y dos columnas

# PROMEDIO de una columan de DATAFRAME:
np.median(data_clean["Edad"])


# GENERAR ARRAYs aleatorios:
np.random.rand(2,2) # dos filas y dos columnas

#crear arreglo e indicar tipo de dato INT
arreglo = np.array([1,2,3,4,5,6], dtype="i")
print(arreglo, arreglo.dtype)

arreglo = np.array([1000000000,2,3,4,5,6], dtype="i2")
print(arreglo, arreglo.dtype, arreglo.itemsize, arreglo.size)#tipo ded ato INT16

arreglo = np.array([1000000000,2,3,4,5,6], dtype="i4") #tipo ded ato INT32
print(arreglo, arreglo.dtype, arreglo.itemsize, arreglo.size)

arreglo = np.array([1000000000,2,3,4,5,6], dtype="i8") #tipo de dato INT64
print(arreglo, arreglo.dtype, arreglo.itemsize, arreglo.size)
arreglo.shape #tamaño del arreglo 6


arreglo.reshape((2,3)) #cambiar la dimension del arreglo de 6 a 2x3: 2filas y 3 columnas
arreglo.reshape((3,2)) # cambiar a 3 filas y 2 columnas

#agregar elementos en array
arreglo # 6 Elementos
np.append(arreglo, 100) # agregar elemento 100, ahora son 7 elementos
np.insert(arreglo, 1, 100) #insertar en INDEX 1 el elemento 100
np.delete(arreglo, 1) #eliminar elemento que tienen INDEX 1

#extraer elemento de acuerdo al indexi
arreglo = np.array([1,2,3,4,5,6], dtype="i") #crea un arreglo  que contiene los enteros del 1 al 6. El tipo de datos es int
x = np.where(arreglo == 6) #encontrar todas las ubicaciones en el arreglo donde el valor es 6
x #devuelve un tupla que contiene el INDEX de la ubicación IGUAL a 6

#ordenamiento de array
arreglo.sort() #ordena el arreglo arreglo en orden ascendente

#SLICING: invertir el orden de los elementos del array
arreglo[::-1]  

#Operaciones básicas con arreglos
arreglo + 2
arreglo - 2
arreglo / 2


alturas = np.array([1.74, 1.8, 1.78, 1.68, 1.78, 1.7, 1.74, 1.74, 1.73, 1.79, 
           1.78, 1.72, 1.65, 1.78, 1.7, 1.68, 1.79, 1.68, 1.82, 1.72,
           1.75, 1.66, 1.67, 1.79, 1.75, 1.65, 1.78, 1.73, 1.71, 1.81,
           1.73, 1.71, 1.68, 1.74, 1.75, 1.68, 1.74, 1.81, 1.73, 1.82,
           1.8, 1.67, 1.73, 1.7, 1.73, 1.7, 1.81, 1.81, 1.76, 1.82, 1.68,
           1.74, 1.65, 1.8, 1.78, 1.7, 1.68, 1.78, 1.79, 1.73, 1.64, 1.67,
           1.69, 1.74, 1.76, 1.66, 1.66, 1.73, 1.79, 1.81, 1.78, 1.63,
           1.76, 1.72, 1.71, 1.7, 1.62, 1.8, 1.75, 1.8, 1.78, 1.78, 1.76,
           1.65, 1.65, 1.68, 1.74, 1.75, 1.69, 1.75, 1.7, 1.83, 1.64, 1.7,
           1.69, 1.69, 1.64, 1.69, 1.77, 1.8, 1.78, 1.69, 1.7, 1.7, 1.7,
           1.63, 1.73, 1.84, 1.66, 1.78, 1.8, 1.79, 1.78, 1.74, 1.77,
           1.73, 1.77, 1.76, 1.75, 1.8, 1.75,  1.8, 1.79, 1.71, 1.73,
           1.59, 1.76, 1.75, 1.71, 1.76, 1.8, 1.68, 1.74, 1.77, 1.73,
           1.68, 1.63, 1.67])
alturas
alturas.shape #dimension: (138,)

pesos = np.array([81.4, 88.7, 87.3, 62.7, 81.6, 80.9, 74.6, 84.7, 76.7, 88.3,
         84.6, 74, 57.7, 84.1, 79.7, 63.8, 88.4, 71.2, 87.1, 67, 80.7,
         74.7, 60.5, 85.9, 72.4, 59.7, 87.3, 85.7, 64.1, 91.9, 82.8, 75.7,
         60.2, 73.1, 74.7, 65.9, 80.9, 91.3, 76, 86.8, 80.7, 74.2, 83.1,
         77.8, 84.5, 58.8, 89.5, 87, 84, 89.9, 56.5, 80.2, 61.8, 86.3,
         82.6, 69.4, 65.8, 79.3, 88.1, 78.5, 69.1, 62.5, 74, 74.4, 87.6,
         59.6, 61.4, 83.2, 89.2, 89.2, 103.7, 67.9, 85.4, 69.5, 75.7, 
         83.9, 59.5, 87.9, 82.6, 88.1, 86.2, 88.9, 84.4, 58.4, 61.5, 69.2,
         84.2, 78, 81.1, 81.5, 74.7, 90.4, 59.2, 79.3, 65.1, 93, 60.5,
         76.4, 98.8, 89.1, 88.9, 61.1, 76.6, 86, 75.5, 66.9, 79.4, 87.9,
         72.3, 93.8, 89, 90.7, 86.7, 77.6, 85.1, 91.8, 103.2, 91.1, 67,
         86.9, 78.7, 87.1, 85.5, 69.8, 75, 53.9, 99, 93.7, 88, 79.4, 87.6,
         60.4, 82.7, 90.6, 79.8, 61.2, 62.5, 59.7]) 

#operación de división de dos arrays
imc = pesos/(alturas*alturas)
imc
print(imc.mean()) #promedio del array

#obtener el promedio de arrays por medio de un FOR
imc = []
for i in range(alturas.size): 
    imc.append(pesos[i]/(alturas[i]*alturas[i]))  
print(sum(imc) /len(imc))


# filtrado de elementos en numpy
import numpy as np


#crear un arreglo
arreglo = np.array([11, 12, 13, 14, 15])
print(np.where(arreglo>= 13)) #encontrar elINDEX de arreglo donde elemento es >=13

#crear un filtro/lista de index a devolver, solo TRUE es devuelto
filtro = [True, False, False, True, True]
print(arreglo[filtro])



#mismo ejemplo anterio pero con elemntos smenores a 13
arreglo = np.array([11, 12, 13, 14, 15])
print(np.where(arreglo <= 13))
filtro = [False, True, False, True, False]
print (arreglo[filtro])

#mismo ejemplo anterio pero con elemntos smenores a 13
arreglo = np.array([[11, 18, 13, 14, 15], [20,21,9,23,0]])
arreglo #arreglo de 2x5
print(np.where(arreglo >= 13))

#crear un ARRAY con una lista de strings
pais= np.array(["Albania", "Alemania", "Andorra", "Angola",
                "Antigua y Barbuda", "Arabia Saudita", "Argelia",
                "Argentina", "Armenia", "Australia", "Austria",
                "Bahrein", "Bangladesh", "Belarús", "Belice", "Benín",
                "Bermudas", "Bolivia", "Bosnia y Hercegovina", "Botsuana",
                "Brasil", "Brunéi", "Burundi", "Bélgica", "Cabo Verde",
                "Cambodia", "Canadá", "Catar", "Chad", "Chequia", "Chile",
                "Colombia", "Congo (Rep. Democr.)", "Corea del Norte",
                "Corea del Sur", "Costa de Marfil", "Costa Rica", "Croacia",
                "Cuba", "Dinamarca", "Dominica", "Ecuador", "Egipto",
                "El Salvador", "Emiratos Árabes", "Eritrea", "Eslovaquia",
                "Eslovenia", "España", "Estonia", "Etiopía", "Fiji",
                "Filipinas", "Finlandia", "Francia", "Gabón", "Gambia",
                "Granada", "Grecia", "Groenlandia", "Guatemala",
                "Guinea Ecuatorial", "Honduras", "Hong Kong", "Hungría",
                "India", "Indonesia", "Iraq", "Irlanda", "Islandia",
                "Islas Cook", "Islas Salomón", "Israel", "Japón",
                "Kirguistán", "Kiribati", "Laos", "Letonia", "Libia",
                "Lituania", "Luxemburgo", "Líbano", "Macedonia",
                "Madagascar", "Malaui", "Maldivas", "Malta", "Marruecos",
                "Micronesia", "Moldavia", "Mongolia", "Montenegro",
                "Mozambique", "México", "Namibia", "Nauru", "Nepal",
                "Nicaragua", "Niue", "Noruega", "Nueva Zelandia", "Níger",
                "Omán", "Palaos", "Panamá", "Papúa Nueva Guinea", "Paraguay",
                "Países Bajos", "Perú", "Polinesia Francesa", "Polonia",
                "Puerto Rico", "Reino Unido", "República Dominicana",
                "Rumania", "Samoa", "Samoa Americana", "Santa Lucía",
                "Senegal", "Serbia", "Seychelles", "Suecia", "Suiza",
                "Tailandia", "Taiwán", "Timor Oriental", "Tokelau", "Tonga",
                "Tuvalu", "Túnez", "Ucrania", "Uganda", "Uruguay", "USA",
                "Venezuela", "Vietnam", "Yemen", "Zambia"])
pais
  
#crear un ARRAY con una lista de INTs              
altura = np.array([1.74, 1.8, 1.78, 1.68, 1.78, 1.7, 1.74, 1.74, 1.73, 1.79, 
           1.78, 1.72, 1.65, 1.78, 1.7, 1.68, 1.79, 1.68, 1.82, 1.72,
           1.75, 1.66, 1.67, 1.79, 1.75, 1.65, 1.78, 1.73, 1.71, 1.81,
           1.73, 1.71, 1.68, 1.74, 1.75, 1.68, 1.74, 1.81, 1.73, 1.82,
           1.8, 1.67, 1.73, 1.7, 1.73, 1.7, 1.81, 1.81, 1.76, 1.82, 1.68,
           1.74, 1.65, 1.8, 1.78, 1.7, 1.68, 1.78, 1.79, 1.73, 1.64, 1.67,
           1.69, 1.74, 1.76, 1.66, 1.66, 1.73, 1.79, 1.81, 1.78, 1.63,
           1.76, 1.72, 1.71, 1.7, 1.62, 1.8, 1.75, 1.8, 1.78, 1.78, 1.76,
           1.65, 1.65, 1.68, 1.74, 1.75, 1.69, 1.75, 1.7, 1.83, 1.64, 1.7,
           1.69, 1.69, 1.64, 1.69, 1.77, 1.8, 1.78, 1.69, 1.7, 1.7, 1.7,
           1.63, 1.73, 1.84, 1.66, 1.78, 1.8, 1.79, 1.78, 1.74, 1.77,
           1.73, 1.77, 1.76, 1.75, 1.8, 1.75,  1.8, 1.79, 1.71, 1.73,
           1.59, 1.76, 1.75, 1.71, 1.76, 1.8, 1.68, 1.74, 1.77, 1.73,
           1.68, 1.63, 1.67])
altura


peso = np.array([81.4, 88.7, 87.3, 62.7, 81.6, 80.9, 74.6, 84.7, 76.7, 88.3,
         84.6, 74, 57.7, 84.1, 79.7, 63.8, 88.4, 71.2, 87.1, 67, 80.7,
         74.7, 60.5, 85.9, 72.4, 59.7, 87.3, 85.7, 64.1, 91.9, 82.8, 75.7,
         60.2, 73.1, 74.7, 65.9, 80.9, 91.3, 76, 86.8, 80.7, 74.2, 83.1,
         77.8, 84.5, 58.8, 89.5, 87, 84, 89.9, 56.5, 80.2, 61.8, 86.3,
         82.6, 69.4, 65.8, 79.3, 88.1, 78.5, 69.1, 62.5, 74, 74.4, 87.6,
         59.6, 61.4, 83.2, 89.2, 89.2, 103.7, 67.9, 85.4, 69.5, 75.7, 
         83.9, 59.5, 87.9, 82.6, 88.1, 86.2, 88.9, 84.4, 58.4, 61.5, 69.2,
         84.2, 78, 81.1, 81.5, 74.7, 90.4, 59.2, 79.3, 65.1, 93, 60.5,
         76.4, 98.8, 89.1, 88.9, 61.1, 76.6, 86, 75.5, 66.9, 79.4, 87.9,
         72.3, 93.8, 89, 90.7, 86.7, 77.6, 85.1, 91.8, 103.2, 91.1, 67,
         86.9, 78.7, 87.1, 85.5, 69.8, 75, 53.9, 99, 93.7, 88, 79.4, 87.6,
         60.4, 82.7, 90.6, 79.8, 61.2, 62.5, 59.7])

#Filtros de arrays
print(pais[peso>90])# países con peso mayor a 90
print(pais[peso>90].size) #núm de paises con el peso mayor a 90

print(pais[altura>1.80]) #países con altura mayoe a 1.80
print(pais[altura>1.80].size) #númeor de países con esa altura

print(pais[(peso>90) & (altura>1.80)]) #países con peso mayor a 90 y altura mayor a 1.80
print(pais[(peso>90) & (altura>1.80)].size)

print(pais[(peso>90) | (altura>1.80)])
print(pais[(peso>90) | (altura>1.80)].size)


# Eje de arrays
altura_y_pesos = np.array([[ 1.74, 91.40 ],
                           [ 1.80, 88.70 ],
                           [ 1.78, 87.30 ],
                           [ 1.68, 62.70 ],
                           [ 1.78, 81.60 ]])
altura_y_pesos # 5x2; 5 filas y 2 columnas

#filtrado total
print("Minimo", altura_y_pesos.min()) #Elemento m mín del array
print("Maximo", altura_y_pesos.max()) #Elemento máx del array
print("Pos Min", altura_y_pesos.argmin()) #posición/INDEX del elemento mínimo
print("Pos Max", altura_y_pesos.argmax()) #posición/INDEX del elemento max
print("Suma", altura_y_pesos.sum()) #suma de elementos de array
print("Promedio", altura_y_pesos.mean()) #promedio del array

#filtrar por columnas
print("Minimo", altura_y_pesos.min(axis=1)) #filtrar columna MÍNIMA del array
print("Maximo", altura_y_pesos.max(axis=1)) #filtrar columna MÁXIMA del array
print("Pos Min", altura_y_pesos.argmin(axis=1)) #posición de la columna MINIMA
print("Pos Max", altura_y_pesos.argmax(axis=1)) #posición de la columna MAX
print("Suma", altura_y_pesos.sum(axis=1)) #suma por  FILAS
print("Promedio", altura_y_pesos.mean(axis=1)) #promedio por FILAS



arreglo1 = np.array([1, 2, -3, 4, 5])
arreglo2 = np.array([11, 12, 13, 14, 15])

print("SUMA", np.add(arreglo1, arreglo2)) #suma de Array (suma elemento por elemento)
print("RESTA", np.subtract(arreglo1, arreglo2)) #resta de array, elemento por elemento
print("DIVSION", np.divide(arreglo1, arreglo2)) #división de elemento por elemento
print("MULTIPLICACION", np.multiply(arreglo1, arreglo2)) #multiplicación de elemento por elmemento
print("POTENCIA", np.power(arreglo1, 2)) #exponenye
print("ABSOLUTO", np.absolute(arreglo1)) #valor absoluto

altura = np.array([1.74, 1.8, 1.78, 1.68, 1.78, 1.7, 1.74, 1.74, 1.73, 1.79, 
           1.78, 1.72, 1.65, 1.78, 1.7, 1.68, 1.79, 1.68, 1.82, 1.72,
           1.75, 1.66, 1.67, 1.79, 1.75, 1.65, 1.78, 1.73, 1.71, 1.81,
           1.73, 1.71, 1.68, 1.74, 1.75, 1.68, 1.74, 1.81, 1.73, 1.82,
           1.8, 1.67, 1.73, 1.7, 1.73, 1.7, 1.81, 1.81, 1.76, 1.82, 1.68,
           1.74, 1.65, 1.8, 1.78, 1.7, 1.68, 1.78, 1.79, 1.73, 1.64, 1.67,
           1.69, 1.74, 1.76, 1.66, 1.66, 1.73, 1.79, 1.81, 1.78, 1.63,
           1.76, 1.72, 1.71, 1.7, 1.62, 1.8, 1.75, 1.8, 1.78, 1.78, 1.76,
           1.65, 1.65, 1.68, 1.74, 1.75, 1.69, 1.75, 1.7, 1.83, 1.64, 1.7,
           1.69, 1.69, 1.64, 1.69, 1.77, 1.8, 1.78, 1.69, 1.7, 1.7, 1.7,
           1.63, 1.73, 1.84, 1.66, 1.78, 1.8, 1.79, 1.78, 1.74, 1.77,
           1.73, 1.77, 1.76, 1.75, 1.8, 1.75,  1.8, 1.79, 1.71, 1.73,
           1.59, 1.76, 1.75, 1.71, 1.76, 1.8, 1.68, 1.74, 1.77, 1.73,
           1.68, 1.63, 1.67])

peso = np.array([81.4, 88.7, 87.3, 62.7, 81.6, 80.9, 74.6, 84.7, 76.7, 88.3,
         84.6, 74, 57.7, 84.1, 79.7, 63.8, 88.4, 71.2, 87.1, 67, 80.7,
         74.7, 60.5, 85.9, 72.4, 59.7, 87.3, 85.7, 64.1, 91.9, 82.8, 75.7,
         60.2, 73.1, 74.7, 65.9, 80.9, 91.3, 76, 86.8, 80.7, 74.2, 83.1,
         77.8, 84.5, 58.8, 89.5, 87, 84, 89.9, 56.5, 80.2, 61.8, 86.3,
         82.6, 69.4, 65.8, 79.3, 88.1, 78.5, 69.1, 62.5, 74, 74.4, 87.6,
         59.6, 61.4, 83.2, 89.2, 89.2, 103.7, 67.9, 85.4, 69.5, 75.7, 
         83.9, 59.5, 87.9, 82.6, 88.1, 86.2, 88.9, 84.4, 58.4, 61.5, 69.2,
         84.2, 78, 81.1, 81.5, 74.7, 90.4, 59.2, 79.3, 65.1, 93, 60.5,
         76.4, 98.8, 89.1, 88.9, 61.1, 76.6, 86, 75.5, 66.9, 79.4, 87.9,
         72.3, 93.8, 89, 90.7, 86.7, 77.6, 85.1, 91.8, 103.2, 91.1, 67,
         86.9, 78.7, 87.1, 85.5, 69.8, 75, 53.9, 99, 93.7, 88, 79.4, 87.6,
         60.4, 82.7, 90.6, 79.8, 61.2, 62.5, 59.7])

#crear una función para calcular IMC
def calcular_imc(peso, altura):
    return peso / (altura*altura)

calcular_imc = np.frompyfunc(calcular_imc, 2, 1)
print(calcular_imc(peso, altura))


from time import perf_counter
inicio = perf_counter()

for i in range(10000):
    calcular_imc(peso, altura)
    
final = perf_counter()

print("Numpy %0.2f" % (final-inicio))




altura = [1.74, 1.8, 1.78, 1.68, 1.78, 1.7, 1.74, 1.74, 1.73, 1.79, 
           1.78, 1.72, 1.65, 1.78, 1.7, 1.68, 1.79, 1.68, 1.82, 1.72,
           1.75, 1.66, 1.67, 1.79, 1.75, 1.65, 1.78, 1.73, 1.71, 1.81,
           1.73, 1.71, 1.68, 1.74, 1.75, 1.68, 1.74, 1.81, 1.73, 1.82,
           1.8, 1.67, 1.73, 1.7, 1.73, 1.7, 1.81, 1.81, 1.76, 1.82, 1.68,
           1.74, 1.65, 1.8, 1.78, 1.7, 1.68, 1.78, 1.79, 1.73, 1.64, 1.67,
           1.69, 1.74, 1.76, 1.66, 1.66, 1.73, 1.79, 1.81, 1.78, 1.63,
           1.76, 1.72, 1.71, 1.7, 1.62, 1.8, 1.75, 1.8, 1.78, 1.78, 1.76,
           1.65, 1.65, 1.68, 1.74, 1.75, 1.69, 1.75, 1.7, 1.83, 1.64, 1.7,
           1.69, 1.69, 1.64, 1.69, 1.77, 1.8, 1.78, 1.69, 1.7, 1.7, 1.7,
           1.63, 1.73, 1.84, 1.66, 1.78, 1.8, 1.79, 1.78, 1.74, 1.77,
           1.73, 1.77, 1.76, 1.75, 1.8, 1.75,  1.8, 1.79, 1.71, 1.73,
           1.59, 1.76, 1.75, 1.71, 1.76, 1.8, 1.68, 1.74, 1.77, 1.73,
           1.68, 1.63, 1.67]

peso = [81.4, 88.7, 87.3, 62.7, 81.6, 80.9, 74.6, 84.7, 76.7, 88.3,
         84.6, 74, 57.7, 84.1, 79.7, 63.8, 88.4, 71.2, 87.1, 67, 80.7,
         74.7, 60.5, 85.9, 72.4, 59.7, 87.3, 85.7, 64.1, 91.9, 82.8, 75.7,
         60.2, 73.1, 74.7, 65.9, 80.9, 91.3, 76, 86.8, 80.7, 74.2, 83.1,
         77.8, 84.5, 58.8, 89.5, 87, 84, 89.9, 56.5, 80.2, 61.8, 86.3,
         82.6, 69.4, 65.8, 79.3, 88.1, 78.5, 69.1, 62.5, 74, 74.4, 87.6,
         59.6, 61.4, 83.2, 89.2, 89.2, 103.7, 67.9, 85.4, 69.5, 75.7, 
         83.9, 59.5, 87.9, 82.6, 88.1, 86.2, 88.9, 84.4, 58.4, 61.5, 69.2,
         84.2, 78, 81.1, 81.5, 74.7, 90.4, 59.2, 79.3, 65.1, 93, 60.5,
         76.4, 98.8, 89.1, 88.9, 61.1, 76.6, 86, 75.5, 66.9, 79.4, 87.9,
         72.3, 93.8, 89, 90.7, 86.7, 77.6, 85.1, 91.8, 103.2, 91.1, 67,
         86.9, 78.7, 87.1, 85.5, 69.8, 75, 53.9, 99, 93.7, 88, 79.4, 87.6,
         60.4, 82.7, 90.6, 79.8, 61.2, 62.5, 59.7]


def calcular_imc(peso, altura):
    return peso / (altura*altura)


from time import perf_counter

inicio = perf_counter()


for i in range(10000):
    imc = []
    for j in range(len(peso)):
        imc.append(calcular_imc(peso[j], altura[j]))
    
final = perf_counter()

print("Listas Tradicionales %0.2f" % (final-inicio))



# unión y separación de arrays
altura = np.array([1.74, 1.8, 1.78, 1.68, 1.78])
peso = np.array([81.4, 88.7, 87.3, 62.7, 81.6])

union = np.stack((altura, peso), axis=0) #unir los 2 arrays anteriores por fila
print(union, type(union))

print()

#dividir los arrays 
separados = np.split(union, 2) #dividir en 2 FILAS,
print(separados, type(separados))









































































































































