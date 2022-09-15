import math
weight = input('Ingrese su peso(kg): ')
height = input('Ingrese su estatura(cm): ')
heightMeter = int(height)/100

imc = int(weight)/math.pow(heightMeter,2)

print('Su IMC es de: {:.2f}' .format(imc))


