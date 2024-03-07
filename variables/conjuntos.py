conjunto = set([ 'dato1', 'dato2'])

print(conjunto)

# Agragando un conjunto dentro de otro conjunto
# Para meter un conjunto dentro de conjunto usando forzenset 

conjunto1 = {'dato', 'dato2'}
# conjunto2 = {'dats', 'ddas', conjunto1} # esto asi arrojaria error

conjunto3 = { 'ddasas', ' dsadasd ', frozenset(conjunto1)}

print(conjunto3)

# Teoria de conjuntos

conjuntoT = {2,3,4,5,6}
conjuntoB = {2,3,4}

#Verificando si es un subconjunto
resultado = conjuntoB.issubset(conjuntoT)
#tambien lopodemos verificar de la siguinet forma 
resultado = conjuntoB <= conjuntoT # Es lo mismo pero par averificar si es un subconjunto usamos el igual

#Verificando si es un superconjunto
resultadoDos = conjuntoT.issuperset(conjuntoB)
resultadoDos = conjuntoT < conjuntoB # Cuandoverificamos si es un super conjunto no usamos el igual 
# para verificar tenemos que preguntar si conjuntoB es menor o si conjuntoT es mayor que conjuntoB seria como decir si conjuntoT es un superConjunto
 
 
# Verificar si algun elemento en comun

resultado_en_comun= conjuntoB.isdisjoint(conjuntoT) # Si devuelve false es porque si hay elementos en comun si devuelve true es porque no 

print(resultado) # por que? porqu el conjunto B tiene todos los elementos del conjutno T
print(resultadoDos) # por que ? porqeu el conjuntoT tiene las mismas cosas que el B py aparte tiene mas elementos