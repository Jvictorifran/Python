#calculando com While

number_1 = int(input('digite um numero: '))
number_2 = int(input('digite outro numero: '))
operador = int(input('oque deseja fazer? 1- soma, 2- subração, 3- multiplicação, 4- divisao'))
result = int(0)

if operador == 1:
  result = number_1+number_2
elif operador == 2:
  result = number_1+number_2
if operador == 3:
  result = number_1*number_2
elif operador == 4:
  result = number_1/number_2
print(result)
continuar = input('Deseja Continaur (S/N)?')
while continuar != 'N': 
  number = int(input('digite um numero: '))
  operador = int(input('oque deseja fazer? 1- soma, 2- subração, 3- multiplicação, 4- divisao'))
  if operador == 1:
    result += number
  elif operador == 2:
    result -= number
  if operador == 3:
    result *= number
  elif operador == 4:
    result /= number
  print(result)
  continuar = input('Deseja Continaur (S/N)?')