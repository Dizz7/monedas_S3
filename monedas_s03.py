#Ejercicio 2 - Conversor de monedas

#Valores al 21 de agosto 2024 en pesos chilenos
d_australiano = 617.38
p_argentino = 0.97
yen = 6.31

#Bienvenida y selección de divisas
print('Bienvenido al conversor de divisas hacia Peso Chileno.')
print('Seleccione la divisa desde la que desea convertir: ')
print('1. Dolar Australiano')
print('2. Peso Argentino')
print('3. Yen Japones')
divisa = int(input('Ingresa un número acá: '))


#Conversor según selección
if divisa == 1:
  print('Vas a convertir Dólares Australianos a Pesos Chilenos')
  cantidad = float(input('Ingresa la cantidad de Dólares Australianos acá: '))
  p_chileno = d_australiano * cantidad
  print('El valor de 1 Dólar Australiano es 617.38 pesos chilenos - fecha: 21-08-24')
  print('La cantidad de pesos chilenos es: ', round(p_chileno))

elif divisa == 2:
  print('Vas a convertir Pesos Argentinos a Pesos Chilenos')
  cantidad = float(input('Ingresa la cantidad de Pesos Argentinos acá: '))
  p_chileno = p_argentino * cantidad
  print('El valor de 1 Peso Argentino es 0.97 pesos chilenos - fecha: 21-08-24')
  print('La cantidad de pesos chilenos es: ', round(p_chileno))
else:
  print('Vas a convertir Yenes a Pesos Chilenos')
  cantidad = float(input('Ingresa la cantidad de Yenes acá: '))
  p_chileno = yen * cantidad
  print('El valor de 1 Yen es 6.31 pesos chilenos - fecha: 21-08-24')
  print('La cantidad de pesos chilenos es: ', round(p_chileno))

print('Los resultados en Pesos Chilenos han sido redondeados.')
