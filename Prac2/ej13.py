uso = int(input('¿Cuántas veces prevés utilizar el gimnasio? '))

precioTarjeta = 50
precioBono = 20
precioEntrada = 3
usosBono = 10

bonosNecesarios = uso // usosBono
entradasAdicionales = uso % usosBono

print(f'Con tarjeta: {precioTarjeta} euros.')

if entradasAdicionales != 0 and uso < 10:
    costoBono = (bonosNecesarios + 1) * precioBono
    costoEntradasBono = entradasAdicionales * precioEntrada
    print(f'Con bonos ({bonosNecesarios + 1}): {costoBono} euros.')
elif entradasAdicionales != 0 and uso > 10:
    costoBono = (bonosNecesarios + 1) * precioBono
    costoEntradasBono = (entradasAdicionales * precioEntrada) + (bonosNecesarios * precioBono)
    print(f'Con bonos ({bonosNecesarios + 1}): {costoBono} euros.')
else:
    costoBono = bonosNecesarios * precioBono
    costoEntradasBono = costoBono

print(f'Con bonos ({bonosNecesarios}) y entradas ({entradasAdicionales}): {costoEntradasBono} euros.')

if precioTarjeta <= costoBono and precioTarjeta <= costoEntradasBono:
    recomendacion = 'tarjeta'
elif costoEntradasBono < precioTarjeta and costoEntradasBono <= costoBono:
    recomendacion = 'bonos y entradas'
else:
    recomendacion = 'bonos'

print(f'Recomendación: {recomendacion}.')
