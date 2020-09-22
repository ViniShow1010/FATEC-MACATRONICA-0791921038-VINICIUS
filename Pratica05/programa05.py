#fazer o calculo de bascara
a = float(input('coeficiente A: '))
b = float(input('coeficiente B: '))
c = float(input('coeficiente C: '))

#calcule o valor de delta (potencia no python - x elevado a y == x**y)
delta = (b**2) - (4*a*c)

#Determine o numero de raiz em função do valor do delta
if delta < 0:
  print('não possui raizes reais')
elif delta > 0:
  x1 = (-b + delta**0.5) / (2*a)
  x2 = (-b - delta**0.5) / (2*a)
  print('Raizes: ', x1, x2)
else:
  x2 = (-b - delta**0.5) / (2*a)
  print('Raiz: ', x2)
