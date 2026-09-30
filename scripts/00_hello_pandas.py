import pandas as pd

#ler o arquivo CSV
df = pd.read_csv('data/exemplo/consumo_exemplo.csv')

print("=== Primeiras linhas ===")
print(df.head())

print("=== Resumo estatístico ===")
print(df.describe())

print("=== Consumo médio por morador ===")
df["consumo_morador"] = df["consumo_m3"] / df["moradores"]
print(df)

print("=== Suspeitos (acima de 8 m3 por morador)===")
df_suspeitos = df[df["consumo_morador"] > 8]
print(df_suspeitos)

resultado = df.groupby("bloco")["consumo_m3"].mean() 
titulo = "=== Media de consumo por apartamento, por bloco ==="
print(titulo)
print(resultado)