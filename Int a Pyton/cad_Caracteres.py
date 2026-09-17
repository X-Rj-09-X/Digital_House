txt = """Ricardo Florez Pajaro""" #el uso de comillas triples se pueden hacer saltos de linea.

print(txt)

print(txt[5]) #dentro de un print al colocar corchetes es seleccionar por indice una frase osea podemos recorrer dentro de lo escrito.

print(len(txt)) # con la funcion len podemos contar cuantos caracteres tiene una variable

int = len(txt) #podemos crar una variable con el len 

print(int)

print("Florez" in txt) #podemos preguntar si una palabra o un caracterer esta dentro del texto usando el in (esta) tambien podemos añadirle el not al in para darle una negacion a lo que pedimos

texto = "seguimos trabajando con string"

print(texto[8:19]) #con este comando podemos seleccionar desde donde queremos que empiece a imprimir hasta el unto que queramos [0:8] esto representa que inicia con el primer caracter hasta el ultimo

tx = "RICARDO FLOREZ PAJARO"
minuscula = tx.lower() #se utiliza el .lower para cambiar el texto a minuscula
print(minuscula)

mayuscula = txt.upper() #se utiliza el .upper para cambiar el textpo a mayuscula
print(mayuscula)

escrito = "      me deje un espacio"
print(escrito.strip()) # este comando .strip utilizado para quitar espacios al inicio y al final de un texto

a = "hola"
b = "mundo"
c = a +" "+ b #en este caso al ser dos variables tipo texto el signo + funciona para unir las palabras pero apareceran pegadas para solucionar se pondra el espacio en el mismo texto o se coloca + " " +
print(c)

frase = "el curso demora {1} horas y {0} clases" # se utiliza las llaves cuando queremoa añadir numeros de otra variable al texto, ya que una variable str + int no se pueden unir como tal a menos que concatenemos a str la variable int
horas = 10
clases = 20
print(frase.format(clases, horas)) #con este comando .format podemos añadir el valor int dentro de las llaves que se colocaron en el texto imprimiendo el valor dentro del texto sin error, dentro de las llaves se colocan el numero de orden para que imprima el orden que queramos

# para usar comillas dentro de comillas colocamos \ le da permiso para usarlo "ricardo \"florez"\ pajaro"
# si usamos barras dentro de un texto \ para que no exista el salto y de error usamos \\
# \n salto de linea, \t es un tabulado, \b es borrado hacia atras

print(frase.capitalize()) # con este metodo se coloca la primera letra en mayuscula

print(frase.title()) # con este metodo se coloca cada letra de cada palabra en mayuscula

# .center() para centrar texto dentro de los parentesis se coloca el numero de espacios que deseamos que se centr
#.count() para contar cuantas veces se repite algo, dentro del parentesis va el caracter que queramos ver cuantas veces se repite

#| Método                  | Explicación                                                      |
#| ----------------------- | ---------------------------------------------------------------- |
#| `.lower()`              | Convierte todo el texto a minúsculas.                            |
#| `.upper()`              | Convierte todo el texto a mayúsculas.                            |
#| `.capitalize()`         | Primera letra en mayúscula, resto en minúsculas.                 |
#| `.title()`              | Convierte la primera letra de cada palabra en mayúscula.         |
#| `.swapcase()`           | Invierte mayúsculas por minúsculas y viceversa.                  |
#| `.casefold()`           | Similar a `lower()`, más agresivo para comparaciones.            |
#| `.strip()`              | Elimina espacios al inicio y al final.                           |
#| `.lstrip()`             | Elimina espacios solo al inicio.                                 |
#| `.rstrip()`             | Elimina espacios solo al final.                                  |
#| `.center(n)`            | Centra el texto en un espacio de `n` caracteres.                 |
#| `.ljust(n)`             | Alinea el texto a la izquierda.                                  |
#| `.rjust(n)`             | Alinea el texto a la derecha.                                    |
#| `.zfill(n)`             | Completa con ceros a la izquierda hasta llegar a `n` caracteres. |
#| `.find(texto)`          | Busca un texto y devuelve su posición.                           |
#| `.rfind(texto)`         | Busca desde el final y devuelve la posición.                     |
#| `.index(texto)`         | Igual que `find()`, pero genera error si no encuentra.           |
#| `.rindex(texto)`        | Igual que `rfind()`, pero genera error si no encuentra.          |
#| `.count(texto)`         | Cuenta cuántas veces aparece un texto.                           |
#| `.replace(viejo,nuevo)` | Reemplaza una parte del texto por otra.                          |
#| `.split()`              | Divide una cadena en una lista.                                  |
#| `.rsplit()`             | Divide desde la derecha.                                         |
#| `.splitlines()`         | Divide por saltos de línea.                                      |
#| `.join(lista)`          | Une elementos de una lista en una cadena.                        |
#| `.startswith(texto)`    | Verifica si comienza con cierto texto.                           |
#| `.endswith(texto)`      | Verifica si termina con cierto texto.                            |
#| `.isalpha()`            | Verifica si solo contiene letras.                                |
#| `.isdigit()`            | Verifica si solo contiene números.                               |
#| `.isalnum()`            | Verifica si contiene solo letras y números.                      |
#| `.islower()`            | Verifica si todo está en minúsculas.                             |
#| `.isupper()`            | Verifica si todo está en mayúsculas.                             |
#| `.istitle()`            | Verifica si cada palabra inicia con mayúscula.                   |
#| `.isspace()`            | Verifica si solo contiene espacios.                              |
#| `.encode()`             | Convierte la cadena a bytes.                                     |
#| `.expandtabs()`         | Convierte tabulaciones (`\t`) en espacios.                       |
#| `.partition(sep)`       | Divide la cadena en 3 partes usando un separador.                |
#| `.rpartition(sep)`      | Igual que `partition()`, pero desde la derecha.                  |
#| `.removeprefix(texto)`  | Elimina un prefijo específico.                                   |
#| `.removesuffix(texto)`  | Elimina un sufijo específico.                                    |
#| `.translate()`          | Reemplaza caracteres según una tabla de traducción.              |
#| `.format()`             | Inserta valores dentro de una cadena.                            |
