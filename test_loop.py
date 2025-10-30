import pandas as pd
import numpy as np
from pathlib import Path

# Testing loops in Python

# Importo el dataset: avoacado_kaggle.csv
ruta = Path("data/datasets/avocado_kaggle.csv")
df = pd.read_csv(ruta)

# Recorro las columnas del DataFrame e imprimo su nombre y tipo de dato
#print(df.columns.tolist())

print(df, df.dtypes)

price = 3

# Conteo de valores que cumplen la condición (True/False)
filtro_1 = df["AveragePrice"] > price
print(filtro_1.sum())

# Muestra solo los valores de la columna AveragePrice que son mayores a 'price'
valores_average_price = df["AveragePrice"][df["AveragePrice"] > price]
print(valores_average_price)

# Muestra todas las filas completas donde AveragePrice es mayor a 'price'
filas_average_price = df[df["AveragePrice"] > price]
print(filas_average_price)