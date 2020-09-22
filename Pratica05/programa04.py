#verificar se 3 numeros são lados de um triangulo
ladoa = int(input('informe lado a: '))
ladob = int(input('informe lado b: '))
ladoc = int(input('informe lado c: '))

#verificar se é um triangulo
if (ladoa > 0) and (ladob > 0) and (ladoc > 0):
  if (ladoa+ladob) > ladoc and (ladoa+ladoc) > ladob and (ladob+ladoc) > ladoa:
    print('Pode formar um triangulo')
