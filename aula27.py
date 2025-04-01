#exec A
try: 
  numero = int(input('Digite um numero inteiro: '))
except:
  print('voce nao digitou um numero inteiro')

if numero % 2 == 0:
  print(f'o {numero} é par')
else:
  print(f"o {numero} é impar")