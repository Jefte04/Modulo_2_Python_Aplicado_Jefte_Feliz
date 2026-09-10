RESPUESTAS A PREGUNTAS DE RAZONAMIENTOS:

1. ¿Por qué diagnosticar el dataset completo (forma, nulos) antes de limpiar nada, en vez de empezar a limpiar directamente desde la primera
columna que veas? 
De esa forma me di cuenta de las estructuras, comprobe las 970 filas y 8 columnas, cual tiene mas nulos, la cual es la columna Genre con 279. Asi uno sabe cómo seguir con el proceso de limpieza y demas pasos.

2. ¿Qué pasaría si rellenaras Budget con 0 en vez de eliminar esas filas? ¿Cómo afectaría eso a la columna Ganancia que vas a crear en la
próxima etapa? 
Si rellenamos los valores nulos co 0, daría un valor desconocido y afectaría las ganancias ya que no sabríamos el presupuesto real.
Al sustituir o eliminar las filas con valores nulos en Budget, tendríamos valores reales pra calcular la ganancia real. 
Comprobamos el resultado de 897 filas y 8 columnas.

3. Ganancia se calcula restando (WorldGross - Budget). ¿Qué representaría, en cambio, una columna que dividiera WorldGross entre
Budget? ¿En qué caso preferirías esa versión en vez de la resta? 
se comprobó 519 peliculas con False y 378 con True.
WorldGross / Budget te permite constatar si con relacion al presupuesto hubo ganancias, asi me doy cuenta si la inversion fue rentable; por eso lo prefiero más que WorldGross - Budget.
Pude comprobar el resultado y vi que Avatar tuvo la mayor ganancia con más de 2,500 millones.

4. ¿Qué habría pasado si hubieras intentado ordenar por Ganancia antes de limpiar los nulos de WorldGross y Budget en la Etapa 2? ¿Por qué
el orden en que se hacen las etapas importa aquí?
si intento ordenar por ganancia antes de limpiar los nulos en WorldGross y Budget en la etapa 2, no hubiese tenido un dato confiable;
eso demuestra la importancia de seguir el orden: primero diagnosticar, luego limpiar.

5. De los géneros con más películas en el dataset (Comedia, Acción, Drama), ¿cuál tiene el promedio de calificación de crítica más alto? ¿Te
sorprende, o era lo que esperabas?
primero comprobe el dato del estudio con mas ganancia: Dream works con 378.2 millones, luego Pixar con 359.8 millones.
el genero con la critica mas alta fue el Desconocido; no me lo esperaba, por eso me sorprendio mucho.

6. ¿Por qué guardar el resultado en un archivo nuevo (hollywood_limpio.csv), en vez de sobrescribir el archivo original hollywood.csv que
descargaste?
guardar el archivo tiene sus ventajas: permite una mejor comprobacion del dataset, entender todas las etapas que se siguieron entre otras ventajas.
