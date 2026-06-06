import pandas as pd

# Lectura del archivo de ventas
df = pd.read_csv("../ventas.csv")

# Cálculo de ventas totales
ventas_totales = (df["cantidad"] * df["precio"]).sum()

# Producto más vendido
producto_mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()

print("Ventas totales:", ventas_totales)
print("Producto más vendido:", producto_mas_vendido)
