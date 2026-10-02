import requests
import pandas as pd

URL = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios?view=nivelado"

# 1. Buscar os dados na API
resposta = requests.get(URL, timeout=30)
resposta.raise_for_status()
dados = resposta.json()

print("=== O que a API devolveu ===")
print(type(dados), len(dados))
print(dados[0])

# 2. Transformar em tabela
df = pd.DataFrame(dados)

# 3. Conhecer a tabela: tamanho, colunas e tipos
print("=== Tamanho da tabela ===")
print(df.shape)
print("=== Colunas ===")
print(df.columns)
print("=== Tipos das colunas ===")
print(df.dtypes)

# 4. Ficar só com as colunas úteis, com nomes melhores
df_subset = df[["municipio-id", "municipio-nome", "UF-sigla", "regiao-nome"]]

df_subset = df_subset.rename(columns={
    "municipio-id": "codigo_ibge",
    "municipio-nome": "municipio",
    "UF-sigla": "UF",
    "regiao-nome": "regiao"
})
print("=== Subconjunto de colunas ===")
print(df_subset)
# 5. Quantos municípios cada estado tem?
df_agrupado = df_subset.groupby("UF")["municipio"].size()
df_sorted = df_subset.sort_values(by='codigo_ibge', ascending=False)
print("=== Quantidade de municípios por estado ===")
print(df_agrupado)
print("=== Municípios ordenados por código IBGE ===")
print(df_sorted)

# 6. Existem municípios com o mesmo nome?
# TODO

# 7. Salvar o resultado em CSV
# TODO