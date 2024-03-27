import re

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
    
# bitExer
    
def bank():
  accounts = [ 
              ["Jhon Doe", 1000.0, "123456789"],
              ["Jane Doe", 500.0, "987654321"],
              ["Jin Smith", 2000.0, "111111111"]  
                
  ]
  opciones = print("¿Que desea realizar? \n \
      escoga 1 para: ver todas las cuentas de los clientes \n \
      escoga 2 para: ver detalles de tu cuenta \n \
      escoga 3 para: retirar dinero de tu cuenta \n \
      escoga 4 para: depositar en tu cuenta \n \
      escoga 5 para: salir del sistema \n \
    ")
  
  while True:
    
    opcion = str(input(" Digite la opcion que desea: "))
      
    if(opcion == "1"):
      for i in accounts:
        print(f" Nombre: {i[0]} \n Saldo: {i[1]} \n N. Cuenta: {i[2]}")
        print("---------------------------")
        
    elif(opcion == "2"):
      numero_cuenta = str(input("Digite su numero de cuenta: "))
      for i in accounts: 
        if numero_cuenta == i[2]:
          print(f"Nombre: {i[0]} \n Saldo: {i[1]} \n N. Cuenta: {i[2]}")
          break
        elif accounts.index(i) == len(accounts) - 1:
          print("Numero de cuenta no existe")
          
    elif(opcion == "3"):
      numero_cuenta = str(input("Digite su numero de cuenta: "))
      for i in accounts: 
        if numero_cuenta == i[2]:
          valor_retirar = int(input("Ingresa el valor a retirar: "))

          if((i[1] - valor_retirar) < 0):
            print("No tienes fondos suficientes")
            break
            
          else:
            i[1] -= valor_retirar
            print(f"Cantidad retirada: {valor_retirar} \n Saldo: {i[1]}")
            break
            
        elif accounts.index(i) == len(accounts)-1:
          print("Numero de cuenta no existe")
          
    elif(opcion == "4"):
        numero_cuenta = str(input("Digite su numero de cuenta: "))
        for i in accounts: 
          if numero_cuenta == i[2]:
            valor_depositar = int(input("Ingresa el valor a depositar: "))
            i[1] += valor_depositar
            print(f" Cantidad Depositada: {valor_depositar} \n Saldo: {i[1]}")
            break
            
          elif accounts.index(i) == len(accounts) - 1:
            print("Numero de cuenta no existe")
            
    elif(opcion == "5"):
      print("Gracias por usar la aplicacion, hasta luego.")
      break
    
    else: 
      print("Escoge una opcion correcta")
      
# bank()

def create_phone_number(n):
  return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

def order(sentence):
  if(sentence == ""):
    return ""
  sentence_to_array = sentence.split(" ")
  patron = re.compile(r'[0-9]')
  
  for i in range(0,2,1):
    for y, x in enumerate(sentence_to_array):
      numero = int(patron.search(x).group()) - 1 # El group devuelve el texto coincidente
      
      if(x == numero):
        continue
      else:
        word = sentence_to_array[numero]
        sentence_to_array[numero] = x
        sentence_to_array[y] = word
      
  print(" ".join(sentence_to_array))
order("4of Fo1r pe6ople g3ood th5e the2")


def cakes(recipe, available):
  if(len(recipe) > len(available)):
    return 0
  else:
    lista = []
    for i in recipe:
      resultado = 0
      if(i not in available or recipe[i] > available[i]):
        return 0
      else:
        resultado = available[i] // recipe[i]
        lista.append(resultado)

    print(min(lista)) 
        
cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000})

def cakes(recipe, available):
	return min(available.get(k, 0)/recipe[k] for k in recipe)