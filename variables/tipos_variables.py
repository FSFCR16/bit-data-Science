# Variables de tipo booleano 
# Las variables booleanas son variables que se basan en verdadero o falso,
# este tipo de variables son inmutables, ya que el valor de la varibale no puede ser cambiado
 
### EJEMPLO ###

boo_true = True

boo_false = False

# Tenemos dos variables cada una declarada con un valor ya sea verdadero o falso y eso la hace una variable booleana

# Variables de tipo int
# Estas varoables son numeros que son solo enteros, quiere decir que no acepta decimales
# este tipo de variable tampoco es inmutable

### EJEMPLO ###

num_int = 23

# Variables de tipo float
# Estas variables son las que son numeros decimales 
# este tipo de varible tambien es inmutable

### EJEMPLO ### 

num_float = 2.3

# Variables de tipo lista
# Este tipo de lista es un conjunto que puede estar conformado por varios tipos de de variable
# como numeros, booleanos, string, listas, tuplas etc... 
# Estas variables son mutables quiere decir que su valor puede cambiar debido a que le puedes añadir mas varibles a una lista

### EJEMPLO ###

lista = [2, True, "santiago", [2,4,5], (2,4,5,6) ]

# Variables de tipo tuplas 
# Son conjuntos iguales que las listas que tienen diferentes tipos de datos la diferencia es que
# las tuplas no se pueden moficar son valor es constante 

### EJEMPLO ###

tupla = ("santiago", 12, 4, False, [2,3,4])
 
# Tambien puedes ver la diferencia usando el metodo dir() que te permite mirar cuales 
# metodos y propiedades tiene el objeto pasado por paramtro

# print(dir(lista)) 

#### LOG ####

# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', 
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', 
# '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', 
# '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', 
# '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# print(dir(tupla))

#### LOG ####

['__add__', '__class__', '__class_getitem__', '__contains__',
  '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__getitem__', '__getnewargs__', '__getstate__', '__gt__', 
'__hash__', '__init__', '__init_subclass__', '__iter__', '__le__',
 '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__',
   '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

# Como se puede ver las tuplas y las lisats tienen metodos diferentes debido a que una tiene metodos de manipulacion y la otr
# tiene solo metodos para hallar elementos

# Variables de tipo string
# Este tipo de variable son variables de tipo texto eso quiere decir que solo unicamente texto, este tipo de variables tambien son inmutables

### EJEMPLO ###

string = "hola mundo"

# Variables de tipo set 
# Este tipo de es un conjunto mutable porque se puede modificar sus valores tambien se le pueden añadir
# diferentes tipos de datos pero la diferencia es que a la hora de llamar los sets sus valores
# llegan de forma desordenada esto quiere decir que cada vez que lo llames sus valores llegan en una posicion diferente

### EJEMPLO ###

sets = {"David",2 , 4, "Juan", False }

# Variable de tipo fronzenset
# Lo que hace es pasar un conjunto de tipo mutable a un inmutable

### EJEMPLO ###

# frozenset(lista)
# Esto da error, por que ? debido a que esta variable lista tiene elementos mutables en su interior y no puedes inmutar un elemento con elementos mutables en su interior

frozenset([1,4,5,6]) # Este seria correcto

# Ahora la listas son inmutables

# Variable de tipo dict o diccionario
# Los diccionarios son objetos 1 a 1 u objetos de tipo clave-valor

### EJEMPLO ###

Santiago = {
    "name" : "Santiagi",
    "edad" : 12,
    "Trabaja" : True
}

print(Santiago["name"])

#### LOG ####
#Santiagi
 
print(1 == True) # Esta pregunta es verdadera debido a que en python el 1 equivale a true
print(0 == False) # Esta pregunta es verdadera debido a que en python el 0 equivale a false