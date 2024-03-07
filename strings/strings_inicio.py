#usamos tres comillas para simular los backticks en js ejemplo:
'''Hola soy 
  soy santiago '''
  
#tipos de datos en python 
#Numbers
[1,2,3,4,5]
#float
[2.2,4.5, 5.5]
#strings
"hola"
#booleanos 
true = True
false = False
#concatenacion
var = "juan"
conca = f"hola {var}"
del conca #operador para borrar datos
# try:
#   print(conca)
# except:
#   print("continue")


#Arroja que conca no esta definido porque con el del lo quehice fue borrar datos
#--------------------------------------------------------------------------------
#si yo pongo el operador in en un pront en un objeto iterable lo que hara el operador es verificar que 
# lo que nosotros le pedimos este en el objeto iterable
#ejemplo 

nombre= "santiago"

print("sant" in nombre) # arroja true debido a que esa expresion esta en el objeto iterable que3 le mande
print("sant" not in nombre) # el not in es lo contrario al in pregunta sinjo esta en vez si no esta por ernde esto es false

#metodos de str

string_value= "santiago fajardo "
print(string_value * 3) # sirve para repiter el string una cantidad de veces especifica

#añadir elementos a un string 

string_value += "saluda"

print(string_value)

#tamaño de la cadena de caracteres

print(len(string_value))# len es una funcion o metodo que nos permite saber el tamño de una adena de caracteres

#encontrar una sub-cadena enn una cadena de caracteres

encontrar = "o"

print(string_value.find(encontrar,)) # nos indica desde donde comienza la coincidencia que encontro, si no encuntra coincidencia arroja -1#

#como segunda opcion del find tenemos el index el cual nos retorna el indice de la misma forma que lo hace el find

print(string_value.index(encontrar), 'index') # este metodo recibe 3 argumentos, str, indice inicila e indice final, o sea desde quieres que empiece y desde donde quieres que termine

# si le en vez de poner index o find a secas ponemos rfind o rindex la buesqueda sera de derecha a izquierda

print(string_value.rfind(encontrar)) # en este caso arroja 15 


#pasar una cadena de carcteres a minusculas

mayusculas = "HOLAOOOO"

print(mayusculas.lower())# este metodo pasa una cadena de caracteres a minusculas
print(mayusculas.upper(), 'linea 71') #pasa los caracteres a mayuscuklas

#remplazar algo en una cadena de texto 

print(mayusculas.replace("O", "t", 2))# recibe 3 parametros el ultimo es opcional, el primero el caracter que deseamos cambiar, el segundo es el nuevo caracter
# el tercero es cuantas de las coincidencias que encuntre debemos cambiar ejemplo encontro 5 pero le especificamos que nomas cambie 3


#cortar una sub-cadena

print(mayusculas[1:3]) #va desde el el primer parametro hasta el segundo, sin tomar el segundo
#esto solo lo devulve mas no lo borrasi quisieramos borrarlo lo que hariamos seia remplazar la variable ejemplo

mayusculas = mayusculas[1:3]
print(mayusculas) #listo ahora se borro y solo quedo eso 



#metodo count python 

# El metodo count en python sirve para contar cuantas veces se repite un conjunto en una cadena de caracteres
count_var = 'eeewwwwcc'

print(count_var.count('eee')) # Por ende si pongo 'eee' el resultado sera 1 pero si ponemos 'e' el resultado sera 3

#startswith o endwith

#estos metodos sirven para saber si comienza o termina con algo

print(count_var.endswith('cc')) # Arroja un booleano
print(count_var.startswith('ee'))

#tambien podriamos usar la siguiente forma

print(count_var[:3] ==  'eee')

#Los métodos isdigit(), isnumeric() e isdecimal() determinan si todos los caracteres de la cadena son dígitos, números o números decimales.
#Si bien estas definiciones resultam a priori similares, no lo son. La primera, isdigit(), considera caracteres que pueden formar números, incluidos aquellos correspondientes a lenguas orientales. isnumeric() 
# es más amplia, pues incluye también caracteres de connotación numérica que no necesariamente son dígitos (por ejemplo, una fracción). La última, isdecimal(), es la más 
# restrictiva al tener en cuenta únicamente números decimales; esto es, formados por dígitos del 0 al 9.


# Determina si todos los caracteres son alfanuméricos.
"abc123".isalnum()
True
# Determina si todos los caracteres son alfabéticos.
"abcdef".isalpha()
True
"abc123".isalpha()
False
# Determina si todas las letras son minúsculas.
"abcdef".islower()
True
# Mayúsculas.
"ABCDEF".isupper()
True
# Determina si la cadena contiene todos caracteres imprimibles.
"Hola \t mundo!".isprintable()
False
# Determina si la cadena contiene solo espacios.
"Hola mundo".isspace()
False
"    ".isspace()
True


#Metodo capitalize, transforma el primer caracter a mayusculas
"hola mundo".capitalize()
'Hola mundo'


#Metodo encode() codifica la cadena con el mapa de caracteres especificado y retorna una instancia del tipo bytes
print("Hola mundo".encode("utf-16",))
#lo decodifica segun la especificacion que le pasemos por argumento 
#UTF-8: Ampliamente utilizado y compatible con la mayoría de los caracteres en el mundo.

# UTF-16: Proporciona soporte para todos los caracteres Unicode.

# UTF-32: Similar a UTF-16, pero utiliza 4 bytes por carácter.

# Latin-1 (ISO-8859-1): Un encoding simple que cubre muchos caracteres europeos.

# ASCII: Solo cubre los caracteres ASCII, es decir, los primeros 128 caracteres Unicode.

# Metodos center(), ljust() rjust()
# alianean los textos pero en realidad lo que hacen es que con el argumento qu le pasamos da el ancho, o el len para no complicarse, o sea si le pasamos 10 el len final de la cadena sera 10, si es center a ambos la lados, left a la izquierda y right a la derecha
# center lo alinea en el centro
# ljust a la izquierda
# rjust a la derecha

print('hola'.center(15, '*'))
print('hola'.rjust(10))
print('hola'.ljust(10))

# Las funciones strip(), lstrip() y rstrip() remueven los espacios en blanco que preceden y/o suceden a la cadena.

s = " Hola mundo! "
s.strip()
'Hola mundo!'
# Remueve los de la derecha.
s.rstrip()
' Hola mundo!'
# Remueve los de la izquierda.
s.lstrip()
'Hola mundo! '

"Hola mundo!\nHello world!".split()
['Hola', 'mundo!', 'Hello', 'world!']

# Equivalente a split("\n").
"Hola mundo!\nHello world!".splitlines()
['Hola mundo!', 'Hello world!']

"Hola mundo hello world".split(" ", 2)
['Hola', 'mundo', 'hello world']

#Metodo partation 
#Este metdo devulve una tupla pero hace la misma funcion del split solo que no devulve un array si no una tupla

#EL METODO DIR MUY IMPORTANTE NOS PERMITE SABER QUE PODEMOS HACER CON ESE TIPO O ESTRUCTURA DE DATO

print(dir("str"))


cadena_nueva = "Hola tefity"

nueva_cadena = cadena_nueva.replace("Hola", "se puede")

print(nueva_cadena)