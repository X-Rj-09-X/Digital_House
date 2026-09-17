#la forma de castear o cambiar el tipo de dato, seria tipo de dato("el dato original")
#con type podremos saber con que tipo de datos estanmos trabajando

# texto (str)
variable1 = "Texto"
variable2 = "123456"
variable3 = "Texto123"

#Numéricas (int, float, complex)
Variable4 = 10
variable5 = 2.5
variable6 = 1j

print(type(variable1))# <class 'str'>
print(type(variable2))# <class 'str'>
print(type(variable3))# <class 'str'>
print(type(Variable4))# <class 'int'>
print(type(variable5))# <class 'float'>
print(type(variable6))# <class 'complex'> 


lista = ["manzana", "pera", "uva"]
x = list(("manzana","pera", "uva"))

print(type(lista))

# numéricos

x = 5

y = float(x)

print(y)
print(type(y))

#se puede castear entre enteros y flotantes pero los complejos no 

