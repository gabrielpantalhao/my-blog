import numpy as np
import pandas as pd
import plotly.express as px

# 1 — Ler os arquivos com dados reais
valores_x = np.loadtxt("X.txt")
valores_y = np.loadtxt("y.txt")

# 2 — Cálculo da regressão
media_x = np.mean(valores_x)
media_y = np.mean(valores_y)

b = np.sum((valores_x - media_x) * (valores_y - media_y)) / np.sum((valores_x - media_x)**2)
a = media_y - b * media_x

# 3 — Preparar dados para o gráfico
df = pd.DataFrame({"x": valores_x, "y": valores_y})
df["reta"] = a + b * df["x"]

# 4 — Plotar
fig = px.scatter(df, x="x", y="y", title="Regressão Linear com Dados da Amostra")
fig.add_traces(px.line(df, x="x", y="reta").data)
fig.show()

# 5 — Mostrar coeficientes
print("\nCoeficientes encontrados:")
print("a (intercepto) =", a)
print("b (inclinação) =", b)
