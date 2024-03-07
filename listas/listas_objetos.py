# Metodos par ala manipulacion de listas

lista = [1,2,3,4,5,6]

# Metodo append

# Este metodo sirve para agregar elemntos a lista estos elemntos seran agragados al final de la lista

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
