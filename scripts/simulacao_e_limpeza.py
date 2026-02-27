import pandas as pd
import numpy as np
from faker import Faker
import random
import os
from datetime import date

# Garantir que a pasta data exista
if not os.path.exists("data"):
    os.makedirs("data")

fake = Faker()

# Datas fixas usando datetime (resolve o erro do Faker)
start_date = date(2023, 1, 1)
end_date = date(2023, 12, 31)

# Produtos com categoria e preço base
produtos = {
    "Notebook": ("Eletrônicos", 3500),
    "Monitor": ("Eletrônicos", 1200),
    "Mouse": ("Acessórios", 80),
    "Teclado": ("Acessórios", 150),
    "Cadeira": ("Móveis", 900),
    "Mesa": ("Móveis", 1300)
}

dados = []

# Simulação de 1000 vendas em 2023
for _ in range(1000):
    produto = random.choice(list(produtos.keys()))
    categoria, preco_base = produtos[produto]

    quantidade = random.randint(1, 5)
    preco = round(random.uniform(preco_base * 0.8, preco_base * 1.2), 2)

    dados.append({
        "Data": fake.date_between(start_date=start_date, end_date=end_date),
        "Produto": produto,
        "Categoria": categoria,
        "Quantidade": quantidade,
        "Preco": preco
    })

# Criar DataFrame
df = pd.DataFrame(dados)

# Criar coluna de total
df["Total_Venda"] = df["Quantidade"] * df["Preco"]

# Limpeza simples
df_clean = df.dropna()

# Salvar arquivos na pasta data
df.to_csv("data/data_simulated.csv", index=False)
df_clean.to_csv("data/data_clean.csv", index=False)

print("Simulação e limpeza concluídas com sucesso.")