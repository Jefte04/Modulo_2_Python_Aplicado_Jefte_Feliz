import numpy as np
import pandas as pd
df = pd.read_csv("hollywood.csv")

# Etapa 1: Cargar y diagnosticar
df = pd.read_csv("hollywood.csv")

"""
## REquisitos: Cargar el archivo descargado. Quédate solo con estas 8 columnas: Movie, LeadStudio, Genre, RottenTomatoes, AudienceScore,
WorldGross, Budget, Year. Diagnostica: la forma del dataset (filas y columnas), y cuántos valores nulos tiene cada columna.
"""

df = df[["Movie", "LeadStudio", "Genre", "RottenTomatoes", "AudienceScore", "WorldGross", "Budget", "Year"]]

print(df.shape)
print(df.isnull().sum())

# Etapa 2: Limpiar

"""
## REquisitos: Para Genre y LeadStudio (columnas de texto): rellena los valores nulos con una categoría de reemplazo razonable, en vez de eliminar esas
filas.
Para RottenTomatoes y AudienceScore (columnas numéricas): rellena los nulos con una medida que ya usaron en el Tema 4, que no se
distorsione tanto con valores extremos.
Para WorldGross y Budget: son pocas filas afectadas. Elimínalas en vez de rellenarlas, ya que vas a necesitar estos 2 números exactos más
adelante.
"""
# Rellenar nulos en columnas de texto
df["Genre"] = df["Genre"].fillna("Desconocido")
df["LeadStudio"] = df["LeadStudio"].fillna("Desconocido")

# Rellenar nulos en columnas numéricas con la mediana
df["RottenTomatoes"] = df["RottenTomatoes"].fillna(df["RottenTomatoes"].median())
df["AudienceScore"] = df["AudienceScore"].fillna(df["AudienceScore"].median())

# Eliminar filas con nulos en WorldGross y Budget
df = df.dropna(subset=["WorldGross", "Budget"])

print(df.shape)
print(df.isnull().sum().sum())

# Etapa 3: Crear columnas nuevas

"""
## REquisitos: Crea una columna Ganancia, que sea el resultado de restarle el presupuesto (Budget) a la recaudación mundial (WorldGross).
Crea una columna Exitosa, que sea True si la calificación de la crítica (RottenTomatoes) es de 60 o más, y False en cualquier otro caso.
"""
df["Ganancia"] = df["WorldGross"] - df["Budget"]
df["Exitosa"] = df["RottenTomatoes"] >= 60

print(df["Exitosa"].value_counts())

# Etapa 4: Tipos de datos y ordenar

"""
## REquisitos: Confirma con .dtypes que Exitosa quedó guardada como un tipo booleano, no como texto ni número.
Ordena el dataset por Ganancia, de mayor a menor, e imprime el nombre y la ganancia de las 3 películas más rentables.
"""

print(df.dtypes)
df = df.sort_values("Ganancia", ascending=False)
print(df[["Movie", "Ganancia"]].head(3))

# Etapa 5: Agrupar y analizar

"""
## REquisitos: Agrupa el dataset por Genre, y calcula el promedio de RottenTomatoes de cada género, redondeado a 1 decimal.
Agrupa el dataset por LeadStudio, y calcula el promedio de Ganancia de cada estudio, redondeado a 1 decimal.
"""

# Calcular el promedio de RottenTomatoes por género y redondear a 1 decimal
df_genre = df.groupby("Genre")["RottenTomatoes"].mean().round(1)
print(df_genre.sort_values(ascending=False))

# Validacion de datos pelicula con crtica mas alta
print(df_genre.sort_values(ascending=False))
print(df["Genre"].value_counts())

# Calcular el promedio de Ganancia por estudio y redondear a 1 decimal
df_studio = df.groupby("LeadStudio")["Ganancia"].mean().round(1)
print(df_studio.sort_values(ascending=False))

# Etapa 6: Guardar el resultado

"""
## REquisitos: Guarda el dataset ya limpio y con las columnas nuevas en un archivo llamado hollywood_limpio.csv, sin la columna extra de índice que
Pandas agregaría por defecto.
"""
df.to_csv("hollywood_limpio.csv", index=False)
print("Archivo guardado como hollywood_limpio.csv")

# Validar que el archivo se guardó correctamente
df_limpio = pd.read_csv("hollywood_limpio.csv")
print(df_limpio.shape)
print(df_limpio.isna().sum().sum())
