listas= ["davis", "cristian", 2, 2.3, "davis"] #listas modificables

tuple= ("davis", "cristian", 2, 2.3) #las tuplas no son modificables


sets = {"davis","cristian", 2, 2.3} #no permite repetir valores, no tiene un orden fijo

print(listas)

set_new= set(listas) # se convierte la lista a un set poar aquitar los datos repetidos


print(set_new)

diccionario = {
  "nombre": "santiago",
  "edad": 2
} #este es un json de js

print(diccionario["nombre"]) #accedemos a los valores de un diccionario por medio de lo scorchetes y valor al que queremos acceder
print(diccionario.keys())