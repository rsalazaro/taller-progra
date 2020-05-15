# Constantes
CAPACIDAD_PISCINA = 90/100
RELACION_AGUA_CLORO = 0.5 / 10000
FLUJO_MANGUERA = 30
METRO_CUBICO = 1000

# Entradas

largo = float(input('Ingrese largo de la piscina: '))
ancho = float(input('Ingrese ancho de la piscina: '))
alto = float(input('Ingrese alto de la piscina: '))


# Proceso

cantidad_agua = largo*ancho*alto*METRO_CUBICO*CAPACIDAD_PISCINA
cantidad_cloro = cantidad_agua * RELACION_AGUA_CLORO
minutos = cantidad_agua / FLUJO_MANGUERA
horas = int(minutos // 60)
minutos = int(minutos % 60)

# Salidas

print('Se necesitan', cantidad_agua, 'litros de agua para llenar la piscina')
print('Se necesitan', cantidad_cloro, 'litros de cloro para mantener la piscina')
print('Se necesitan', horas, 'horas y', minutos,'minutos para llenar la piscina')