
# Un diccionario en Python es una colección de elementos, donde cada uno tiene 
# una llave key y un valor value. Los diccionarios se pueden crear con paréntesis 
# {} separando con una coma cada par key: value. En el siguiente ejemplo tenemos 
# tres keys que son el nombre, la edad y el documento.

d1 = {
  "Nombre": "Sara",
  "Edad": 27,
  "Documento": 1003882
}
print(d1)
#{'Nombre': 'Sara', 'Edad': 27, 'Documento': 1003882}

# Otra forma equivalente de crear un diccionario en Python es usando dict() e introduciendo los pares key: value entre paréntesis.

d2 = dict([
      ('Nombre', 'Sara'),
      ('Edad', 27),
      ('Documento', 1003882),
])
print(d2)
#{'Nombre': 'Sara', 'Edad': '27', 'Documento': '1003882'}

# También es posible usar el constructor dict() para crear un diccionario.
d3 = dict(Nombre='Sara',
          Edad=27,
          Documento=1003882)
print(d3)
#{'Nombre': 'Sara', 'Edad': 27, 'Documento': 1003882}


# Para acceder a los elemntos de un diccionario tenemos dos formas
# Como si fuera un indice
# Como la funcion get 

print(d1.get("Nombre"))
print(d1["Nombre"])


#Podemos modificar su valor de la siguiente forma

d1["Nombre"]= "santiago"
print(d1)

# Si la llave no existe se agrega

d1["Deporte"] = "Futbol"

print(d1)

# Los diccionarios se pueden iterar de manera muy similar a las listas u otras estructuras de datos. Para imprimir los key.

# Imprime los key del diccionario
for x in d1:
    print(x)
    
#Nombre
#Edad
#Documento
#Direccion

# Se puede imprimir también solo el value.

for x in d1:
    print(d1[x])
#Laura
#27
#1003882
#Calle 123

# Imprime los key y value del diccionario
for x, y in d1.items():
    print(x, y)
#Nombre Laura
#Edad 27
#Documento 1003882
#Direccion Calle 123


# Metodos de los dicionarios

# El método clear() elimina todo el contenido del diccionario.
d = {'a': 1, 'b': 2}
d.clear()
print(d) #{}

# El metodo get nos permite encontrar el valor para una key, pasandole la key por parametro y segundo parametro opcional por si no se encuentra que haga algo

d = {'a': 1, 'b': 2}
print(d.get('a')) #1
print(d.get('z', 'No encontrado')) #No encontrado

# El método items() devuelve una lista con los keys y values del diccionario. Si se convierte en list se puede indexar como si de una lista normal se tratase, siendo los primeros elementos las key y los segundos los value.


d = {'a': 1, 'b': 2}
it = d.items()
print(it)             #dict_items([('a', 1), ('b', 2)])
print(list(it))       #[('a', 1), ('b', 2)]
print(list(it)[0][0]) #a

nombres = ["Alice", "Bob", "Charlie"]
edades = [25, 30, 22]

nuevo = zip(nombres, edades)

print(nuevo)

# Funcion zip 

# Cuando utilizas la función zip con listas de diferentes longitudes,
# el comportamiento dependerá de la longitud del iterable más corto. 
# zip se detendrá cuando alcance el final del iterable más corto y no 
# incluirá elementos adicionales del iterable más largo.

# Veamos un ejemplo:

nombres = ["Alice", "Bob", "Charlie"]
edades = [25, 30]

nuevo = zip(nombres, edades)

# Convertir el iterable en una lista
lista_nuevo = list(nuevo)

print(lista_nuevo)
# Resultado: [('Alice', 25), ('Bob', 30)]


# Si alguna de las listas es más larga que la otra y deseas incluir los elementos 
# restantes, puedes usar itertools.zip_longest en lugar de zip. itertools.zip_longest 
# rellena los valores que faltan con un valor predeterminado (por defecto None) en el
# iterable más corto. Aquí tienes un ejemplo:

from itertools import zip_longest

nombres = ["Alice", "Bob", "Charlie"]
edades = [25, 30]

nuevo = zip_longest(nombres, edades)

# Convertir el iterable en una lista
lista_nuevo = list(nuevo)

print(lista_nuevo)
# Resultado: [('Alice', 25), ('Bob', 30), ('Charlie', None)]


# keys()
# El método keys() devuelve una lista con todas las keys del diccionario.

d = {'a': 1, 'b': 2}
k = d.keys()
print(k)       #dict_keys(['a', 'b'])
print(list(k)) #['a', 'b']

# values()
# El método values() devuelve una lista con todos los values o valores del diccionario.

d = {'a': 1, 'b': 2}
print(list(d.values())) #[1, 2]

# Metodo pop elimina uina key, se la pasa la key por parametro

# El método pop() busca y elimina la key que se pasa como parámetro y devuelve su valor asociado. Daría un error si se intenta eliminar una key que no existe.

d = {'a': 1, 'b': 2}
d.pop('a')
print(d) #{'b': 2} # Tambien se le puede indicar por parametro que pasa si la key no es encontrada


# popitem()
# El método popitem() elimina de manera aleatoria un elemento del diccionario.

d = {'a': 1, 'b': 2}
d.popitem()
print(d)
#{'a': 1}

# El método update() se llama sobre un diccionario y tiene como entrada otro diccionario. Los value son actualizados y si alguna key del nuevo diccionario no esta, es añadida.
# actua como el metdo extend de las listas

d1 = {'a': 1, 'b': 2}
d2 = {'a': 0, 'd': 400}
d1.update(d2)
print(d1)
#{'a': 0, 'b': 2, 'd': 400}

print(dir({}))

#Diccionarios con tuplas

dicTupla= { 
          ("hola", "carro"): "cualquier de las dos que pongas me invocare, mentiras asi no funciona" 
}

print(dicTupla[("hola", "carro")])

# creando un diccionario con formKeys

dicKeys=  dict.fromkeys("abcdef", 'sin valor') # El primer parametro es iterable qu ese asignara como clave, el segundo parametro sera el valor

print(dicKeys) # como se puede ver el segundo parametro sera el valor que se le asiganra a las claves