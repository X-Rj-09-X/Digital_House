import random

#-------------------------
#TIPOS DE DATOS
#-------------------------


#--------------------------
# 1. Texto
#-------------------------
# - str(cadena de caracteres)
texto = "Hola Mundo"
#--------------------------


#--------------------------
# 2. Numericos
#-------------------------
# - int (enteros)
num_entero = 9

# - float (decimales)
num_decimal = 3.1416

# - complex (complejos)
num_complejoos = 3 + 6j
#--------------------------


#--------------------------
# 3. Secuencia
#-------------------------
# - listas [ordenables y mutables]
lista = [1,2,3,4]

# - tuplas [coleccion ordenada e inmutable]
tupla = [1,2,3]

# - range (rango) [secuencia inmutable de numeros]
rango = range(0 ,10)
#--------------------------


#--------------------------
# 4. Mapping type (mapeo)
#-------------------------
# - dict (diccionario) [coleccion no ordenada de pares clave/valor]
diccionario = {"nombre": "Ricardo", "edad": 26}
diccionario = {
    "nombre": "Ricardo", 
    "edad": 26  
    } # se recomienda usar de esta manera para ser mas legible.
#--------------------------


#--------------------------
# 5. Set type (conjunto)
#-------------------------
# - set(conjunto) [coleccion no ordenada y mutable de elementos unicos (no permite repetir)]
conjunto = {1,2,3,4}

# - frozenset (conjunto inmutable)[conjuntoo inmutable de las mismas caracteristicas]
conjunto_inmutable = frozenset({1,2,3,4})
#--------------------------


#--------------------------
# 6. Boolean type (booleanos)
#-------------------------
# - boolean (puede ser verdadero o falso)
booleano = True
booleano2 = False
#--------------------------


#--------------------------
# 7. Binary Type (binarios)
#-------------------------
# - bytes (una secuencia inmutable de bytes)
bytes_data = b"datos"

# - bytearray (array de bytes)[una secuencia mutable de bytes]
bytesarray_data = bytearray(b"datos")

# - memoryview (vista de memoria)[permite acceder a la memoria de objetos de bytes sin hacer una copia]
memoria = memoryview(b"datos")
#--------------------------


#--------------------------
# 8. None/null (nulo)
#-------------------------
# - nonetype (nulo)[representa la auseencia de valor o la no definicion]
nulo = None
#--------------------------


x = random.randrange(1,10) #numero aleatorio dentro del rango estipulado en ,los (), el ultimo diogito que es el 10 no aparece en los numeros
y = random.random() #numero aleatorio de tipo float
z = random.randint(1,10) # numero aleatorio de forma entera dentro del rango dado pero esta vez todo el rango esta dentro osea el 10 tambien

print(z)