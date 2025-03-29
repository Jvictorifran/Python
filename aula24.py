# # introducão ao try/except
# try -> tentar executar um codigo
# except -> ocorreu algum erro ao executa

numero_str = input('Vou dobrar o numero que vc digitar: ')

try:
  print('oi')
  numero_float = float(numero_str)
  print('Float:', numero_float)
  print(f"o dobro de {numero_float}, é {numero_float*2}")
except:
  print('Isso não e um numero')