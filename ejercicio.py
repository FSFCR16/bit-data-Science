def squareUp(n):
    lista_final = []

    for i in range(1, n + 1):
        contador = 0

        while contador < n:
            if contador < n - i:
                lista_final.append(0)
            else:
                lista_final.append(n - contador)

            contador += 1

    return lista_final

# Ejemplo de uso

def get_count(sentence):

  contador = 0
  for i in sentence:
    if(i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
      contador += 1
  
  return contador
  

def find_outlier(integers):
    par = [0, 0]
    impar = [0,0]
    for i in integers:
      if i % 2 == 0:
        par[0] += 1
        par[1] = i
      else:
        impar[0] += 1
        impar[1] = i
    
    if par[0] > impar[0]:
      
      return impar[1]
    
    else:
      
      return par [1]
    

    
    
def find_outlier(int):
    odds = [x for i in int if i%2!=0]
    evens= [x for i in int if i%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]
    

# def find_outlier(integers):
#     parity = [n % 2 for n in integers]
#     return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]


minimo = 2.5 * 60
promedio = 4 * 60
maximo = 7 * 60
crudoA= 3.5 * 60
crudoP= 5 * 60
curso_actual = 1.5 * 60

# a)

def porcentaje(maximo , minimo, promedio):
  resultadosA= {
    "dm" : ((curso_actual - maximo) * 1000 // maximo) / 10   ,
    "dr" : ((curso_actual - minimo) * 1000 // minimo) / 10,
    "dp" : ((curso_actual - promedio) * 1000 // promedio) / 10
  }
  
  resultadosB={
    "crudoP": int((promedio - crudoP) * 1000 // crudoP) / 10,
    "crudoA": int((curso_actual - crudoA) * 1000 // crudoA) / 10
  }
  
  resultadosC = (10000 // curso_actual) * promedio / 1000
  
  print( f' mas lento:  {resultadosA["dm"]}% \n mas rapido: {resultadosA["dr"]}% \n promedio: {resultadosA["dp"]}%')
  print( f' en comparacion con el crudo promedio se redujo un: {resultadosB["crudoP"]}% \n en comparacion con el curso actual se redujo un: {resultadosB["crudoA"]}%')
  print( f' ver 10 horas de este curso equivale a {resultadosC}hrs')


def bitExercise():
  nombre =  str(input("Digite su nombre: "))
  edad =  int(input("Digite su edad: "))
  
  if (nombre[-1] in "aeiou") and (edad > 18):
    print(" Es candidato a compra ")
  
  elif(nombre[-1] not in "aeiou" and (edad <= 18)):
    print( "Es candidato por pariente ")
    
  else:
    print("No apto")
    
bitExercise()
    
  
    
    


