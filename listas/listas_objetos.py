# Metodos par ala manipulacion de listas

lista = [1,2,3,4,5,6]

# Otra forma de crear una lista es con el objeto list, que recibe como argumentos los elementos que va a tener la lista

### EJEMPLO ###

new_list = list((2, 3, True, "Juan" ))

print(new_list)

#### LOG ####
# [2, 3, True, 'Juan']

# Metodo append

# Este metodo sirve para agregar elemntos a lista, estos elementos seran agragados al final de la lista

lista.append(3)
print(lista)

# Eso se pueede hacer tambien de la siguente manera

lista[len(lista):] = [4]
print(lista) # Poruqe esos dos puntos son slicing lo que permite decir como desde la ultima posicion de la lista hasta lo ultimo el siguiente elemento sera [4]


# Metodo extend

#une una lista con otra

lista_dos = [5,6,7,8,9]
lista.extend(lista_dos)
print(lista)

#o tambien puedo extender una lista de la siguiente manera
lista_tres= [11,22,345,65, "hola"]
lista = [*lista, *lista_tres ]
print(lista)

#ambas formas hacen lo mismo


#Metodo insert 

#recibe dos parametros el primero sera la posicion desde la cual se insertara un elemento, el segundo elemento 

lista.insert(0, "hola")
print(lista)

# El metodo remove, borra un elemento borra el primer elemento con el cual concuerde o tenga coincidencia

lista.remove("hola")
lista.remove(3)
print(lista)


# El metodo pop()

#Elimina el item en la posicion dada y lo retorna, si no se le especifica ningun parametro elemina el ultimo

lista.pop(2)
lista.pop()
print(lista)

# Metedo count al igual que los string( dice cuantas veces esta un elemnto en la lista

print(lista.count(4))

#Metodo clear 

# Elimina todos los elemntos de la lista 

lista.clear()
print(lista)

# Metodo sort Ordena los elementos de la lista 

lista = [2,3,56,3,23,4]

lista.sort() # recibe dos argumentos el primero es como criterio por el caul se va a ordenar y reverse si queremos que la devuleva de atras hacia adelante
print(lista)

#Metodo copy 
#Devulve una copia superficial de la lista


del lista[2]
del lista[0] # Tambine sirve para elemtos de una lista
print(lista)

lista.pop()

print(lista)

# Listas anidadas, quiere decir que hay listas dentro de listas 

### EJEMPLO ###

lista_anidada = [["juan", False], [2, 5], [64, 32]]

# Si se desea acceder al un elemento de una lista anidada una forma seria

print(lista_anidada[0][1])

#### LOG ####

# False

# Tambien aparte de hacer slicing con los indices podemos hacer que vaya de 2 en 2 o de 3 en 3

### EJEMPLO ###

# slicing

lista_slice = [2,4,5,6,7,8]

print(lista_slice[:3]) # aca le estamos diciendo que vaya desde el inicio hasta la posicion 3, no toma la posicion 3.

#### LOG ####

#[2,3,5]

# Ahora que vaya de 2 en dos

print(lista_slice[0:5:2])

#### LOG #### 

# [2, 5, 7]

# Otra forma para dar el sentido inverso sin usar el reverse es la siguiente

print(lista_slice[::-1]) # Esto no estoy seguro, estoy supuniendo pero supongo que se debe a que 
# si tu dices que vas a ir de -1 en -1 se va ir sumando -1 sera -2 depues -3 y asi cambiando el orden de la lista


# Tambien podemos multiplicar la lista y sumar que en realidad en la caso de la multiplicacion seria poner en una lista los elementos de la lista base
# la cantidad de n entonces si n es 3 la lista base estara en lista unica 3 veces y en el caso de la suma funciona como concatenacion normal

### EJEMPLO ###
 
print(lista_slice*3)

#### LOG ####

# [2, 4, 5, 6, 7, 8, 2, 4, 5, 6, 7, 8, 2, 4, 5, 6, 7, 8]

# Con la suma

print(lista_slice + lista_dos)

#### LOG ####

# [2, 4, 5, 6, 7, 8, 5, 6, 7, 8, 9]

# Tambien podemos simular el funcionamiento del metodo "split" seria un split que no se le pasa nada como argumento 
# con el objeto list, pasandole como argumento un str y el covierte cada caracter deñ str en 
# un elemento de la lista

print(list("hola soy santiago fajardo"))

#### LOG ####

# ['h', 'o', 'l', 'a', ' ', 's', 'o', 'y', ' ', 's', 'a', 'n', 't', 'i', 'a', 'g', 'o', ' ', 'f', 'a', 'j', 'a', 'r', 'd', 'o']

# Una forma de desestructurar una lista seria esta

num, *numotros = lista_slice

print(num) #### LOG #### 2
print(numotros) #### LOG #### 4 5 6 7 8

print(dir(list()))