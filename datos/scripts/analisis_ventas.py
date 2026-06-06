import pandas as pd

print("Analisis de ventas iniciado")

df = pd.read_csv("../ventas.csv")

print(df.head())

ventas_totales = (df["cantidad"] * df["precio"]).sum()

print("Ventas totales:", ventas_totales)
