multiplicador = int(input("Ingerese el numero que representa la tabal de multplicar que desea: "))
tabal_multiplicar = []
for i in range(1,11):
  numero = i * multiplicador
  tabal_multiplicar[len(tabal_multiplicar):] = [numero]
print(tabal_multiplicar)