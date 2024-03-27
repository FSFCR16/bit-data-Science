
#creando un contador que va a ir sumandose
contador = 0
# mientras que la condicion se cumpla, el bucle se va seguir ejecutando
# (vuelta, tras vuelta se verifica la condicion)
while contador < 16:
    contador+= 1
    print(contador)
    
### BRAEK ###
  # El break nor sivre para interrumpir un bloque de codigo, lo que quiere decir que cuando
  # estemos en un bucle el break va a terminar el bucle
### CONTINUES ###
  # Por este lado el continue lo que hace es que no rompe el bucle pero si salta a la siguiente iteracion no termiando la iteracion actual
for i in range(1, 6):
  if i == 3:
      continue
  print(i)

### PASS ###
  # Por este lado el pass desactiva un bloque de codigo haciendo que no se ejecute, el pass desactiva el bloque de codigo complet
  # Haciendo una funcion parecida al continue
  # Tambien es algo un poco sintactico, se usa cuando no en algun momento especifico o por alguna razon no quieres ejecutar ningun codigo 
x = -1
if x < 0:
    pass  # No hace nada si x es negativo
else:
    print("x es positivo")