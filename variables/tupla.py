tupla = tuple(['hola', 2121312])

# Creando tuplas sin parentesis

tuplaDos = "hola", "la"

# nesting listas dentro de tuplas
tpl=([1,2,3],['David','Pedro',True])
print(tpl)
tpl[0].append('Tuy')
print(tpl)
tpl[1].remove('David')
print(tpl)

#### LOGS ####
([1, 2, 3], ['David', 'Pedro', True])
([1, 2, 3, 'Tuy'], ['David', 'Pedro', True])
([1, 2, 3, 'Tuy'], ['Pedro', True])

print(tupla, tuplaDos)
