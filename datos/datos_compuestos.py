listas= ["davis", "cristian", 2, 2.3, "davis"] #listas modificables
print(listas)

tuple= ("davis", "cristian", 2, 2.3) #las tuplas no son modificables


sets = {"davis","cristian", 2, 2.3} #no permite repetir valores, no tiene un orden fijo

### LOS SETS ###
  # Este tipo de dato hace referencia a los conjuntos es litereal como trabajar con conjuntos

### METODOS SETS ### 

# Tenemos el metodo union el cual nos da la union entre dos conjuntos

# Definir dos conjuntos (sets)
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Usar el método union para combinar los conjuntos
union_set = set1.union(set2)

# Imprimir el conjunto resultante
print("Conjunto resultante después de la unión:", union_set)

# Tambien tenemos el metodo interseccion el cual nos da la interseccion entre dos conjuntos o sea los numeros que compartes

# Definir dos conjuntos (sets)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Usar el método intersection para encontrar la intersección de los conjuntos
intersection_set = set1.intersection(set2)

# Imprimir el conjunto resultante
print("Conjunto resultante después de la intersección:", intersection_set)


set_new= set(listas) # se convierte la lista a un set poar aquitar los datos repetidos
# Al yo hacer e frozenset queda como una tupla solo que se puede hacer operaciones de conjuntos no solo de tuplas


print(set_new)

diccionario = {
  "nombre": "santiago",
  "edad": 2
} #este es un json de js

print(diccionario["nombre"]) #accedemos a los valores de un diccionario por medio de lo scorchetes y valor al que queremos acceder
print(diccionario.keys())