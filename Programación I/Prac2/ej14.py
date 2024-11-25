importeCompra = float(input('Introduce el importe de la compra: '))
zonaEnvio = input('Introduce la zona de envío (A/B/C): ')
socio = input('¿Eres socio (S/N)? ')

if socio == 'S':
    if importeCompra <= 150 and zonaEnvio == 'A':
        gastosEnvio = 19
    elif importeCompra <= 150 and zonaEnvio == 'B':
        gastosEnvio = 49
    elif importeCompra <= 150 and zonaEnvio == 'C':
        gastosEnvio = 88
    elif importeCompra <= 750 and zonaEnvio == 'A':
        gastosEnvio = 49
    elif importeCompra <= 750 and zonaEnvio == 'B':
        gastosEnvio = 79
    elif importeCompra <= 750 and zonaEnvio == 'C':
        gastosEnvio = 118
    elif importeCompra <= 1500 and zonaEnvio == 'A':
        gastosEnvio = 89
    elif importeCompra <= 1500 and zonaEnvio == 'B':
        gastosEnvio = 119
    elif importeCompra <= 1500 and zonaEnvio == 'C':
        gastosEnvio = 158
    elif importeCompra > 1500 and zonaEnvio == 'A':
        gastosEnvio = importeCompra * 0.06
    elif importeCompra > 1500 and zonaEnvio == 'B':
        gastosEnvio = (importeCompra * 0.06) + 30
    elif importeCompra > 1500 and zonaEnvio == 'C':
        gastosEnvio = (importeCompra * 0.06) + 69
else:
    if importeCompra <= 150 and zonaEnvio == 'A':
        gastosEnvio = 25
    elif importeCompra <= 150 and zonaEnvio == 'B':
        gastosEnvio = 55
    elif importeCompra <= 150 and zonaEnvio == 'C':
        gastosEnvio = 94
    elif importeCompra <= 750 and zonaEnvio == 'A':
        gastosEnvio = 60
    elif importeCompra <= 750 and zonaEnvio == 'B':
        gastosEnvio = 90
    elif importeCompra <= 750 and zonaEnvio == 'C':
        gastosEnvio = 129
    elif importeCompra <= 1500 and zonaEnvio == 'A':
        gastosEnvio = 120
    elif importeCompra <= 1500 and zonaEnvio == 'B':
        gastosEnvio = 150
    elif importeCompra <= 1500 and zonaEnvio == 'C':
        gastosEnvio = 189
    elif importeCompra > 1500 and zonaEnvio == 'A':
        gastosEnvio = importeCompra * 0.08
    elif importeCompra > 1500 and zonaEnvio == 'B':
        gastosEnvio = (importeCompra * 0.08) + 30
    elif importeCompra > 1500 and zonaEnvio == 'C':
        gastosEnvio = (importeCompra * 0.08) + 69

print(f'Gastos de envío: {float(gastosEnvio):.2f} euros')