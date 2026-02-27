import pandas as pd
import matplotlib.pyplot as plt

# Ler o arquivo da pasta data
df = pd.read_csv("data/data_clean.csv")

# Converter coluna Data para datetime
df["Data"] = pd.to_datetime(df["Data"])

# Criar coluna de mês
df["Mes"] = df["Data"].dt.month

# Total de vendas por produto
total_por_produto = df.groupby("Produto")["Total_Venda"].sum().sort_values(ascending=False)

print("Total de vendas por produto:")
print(total_por_produto)

# Produto com maior faturamento
produto_top = total_por_produto.idxmax()
print("\nProduto com maior faturamento:", produto_top)

# Vendas mensais
vendas_mensais = df.groupby("Mes")["Total_Venda"].sum()

# Plot gráfico
plt.figure()
vendas_mensais.plot()
plt.title("Tendência de Vendas Mensais - 2023")
plt.xlabel("Mês")
plt.ylabel("Total de Vendas")
plt.show()