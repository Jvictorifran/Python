condicao = False
passou_no_if = None

if condicao:
  passou_no_if = True
  print('faça Algo')
else:
  print('Nao faça algo')
print(passou_no_if, passou_no_if is None) #nao passou no if
print(passou_no_if, passou_no_if is not None) #passou no if

if passou_no_if is None:
  print("nao passou no if")
else:
    print("passou no if")