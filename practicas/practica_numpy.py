# arrays: creacion e indexado
import numpy as np

calificaciones = np.array([88, 92, 76, 95, 81, 68])

print(calificaciones[0])
print(calificaciones[-1])
print(calificaciones[2:5])
print(len(calificaciones))


# operaciones vectorizadas

comisiones = np.array([150.40, 200.75, 180.20, 220.50])
comisiones_con_bono = comisiones * 1.10
print(comisiones_con_bono.round(2))

# funciones estadisticas

consumo_gb = np.array([2.5, 3.0, 1.8, 4.2, 3.5, 8.4, 5.1, 6.9])

print("Promedio:", round(np.mean(consumo_gb), 2))
print("Maximo:", np.max(consumo_gb))
print("Minimo:", np.min(consumo_gb))
print("Desviacion estandar:", round(np.std(consumo_gb), 2))

## al interpretar los resultados, veo que mi consumo promedio fue de 4.42 gb, viendo que un dia estuve muy cerca, otro dia estuve por debajo, y otro dia estuve muy por encima, lo que me indica que mi consumo es muy variable. Si la desviacion estandar fuera mucho mas baja, el consumo seria mas estandarzado.

# arrays de dos dimensiones

horas_estudio = np.array([
    [5, 8, 6, 7],
    [10, 9, 11, 8],
    [3, 4, 2, 5],
])

print(horas_estudio.shape)
print("Promedio por estudiante:", np.mean(horas_estudio, axis=1))
print("Promedio por semana:", np.mean(horas_estudio, axis=0))


# desafio final: ventas semanales de 3 sucursales

ventas = np.array([
[1200, 1350, 980, 1420, 1100],
[850, 920, 1050, 890, 960],
[1600, 1750, 1580, 1690, 1720],
])

print("Total de ventas por sucursal:", np.sum(ventas, axis = 1))
print("Comision del 5 por ciento sobre las ventas por sucursal:", np.round(np.sum(ventas, axis = 1) * 0.05, 2))
print("Total de ventas por por dia:", np.sum(ventas, axis = 0))

variacion_por_sucursal = np.round(np.std(ventas, axis = 1), 2)

minima_variacion = np.min(variacion_por_sucursal)

for i in range(len(variacion_por_sucursal)):
    print(f"Variacion en ventas de la Sucursal no. {i+1}: {variacion_por_sucursal[i]}")
    if variacion_por_sucursal[i] == minima_variacion:
        sucursal_menor_variacion = f"Sucursal no. {i+1}"

print("Sucursal con las ventas diarias mas consistentes:", sucursal_menor_variacion)