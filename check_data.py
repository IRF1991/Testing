import os

ruta = "data_backup/peliculas.csv"

if os.path.exists(ruta):
    print("Archivo localizado correctamente.")
else:
    print("No se encontró el archivo.")