consumo = float(input('Introduce la cantidad de kWh: '))

if consumo <= 100:
    importe = consumo * 0.05
elif consumo <= 250:
    aux = consumo - 100
    importe = 5 + aux * 0.07
else:
    aux = consumo - 250
    importe = 15.5 + aux * 0.1

print(f'Importe: {importe:.2f} euros')
