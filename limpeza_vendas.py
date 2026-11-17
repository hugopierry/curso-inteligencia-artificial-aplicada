# Etapas de análise e limpeza de dados

# Etapa 1 — Preparar o ambiente e importar a planilha
# Primeiro, importe a biblioteca e carregue o arquivo.



import pandas as pd

df = pd.read_excel("vendas_sujo.ods", engine="odf")

# Etapa 2 — Conhecer os dados importados
# Antes de limpar qualquer coisa, precisamos investigar o conteúdo.

print("# Visualizar as primeiras 5 linhas")
print(df.head())

print("\n# Visualizar as primeiras 10 linhas")
print(df.head(10))

print("\n# Visualizar as últimas 5 linhas")
print(df.tail())

print("\n# Ver quantidade de linhas e colunas")
print(df.shape)

print("\n# Ver nomes das colunas")
print(df.columns)

print("\n# # Ver tipos de dados e valores não nulos")
print(df.info())

print("\n# Ver estatísticas descritivas")
print(df.describe())

#Investigar problemas nos dados
# Agora começa o trabalho de investigação.

print("\n# Contar valores vazios por coluna")
print(df.isnull().sum())

print("\n# Ver percentual de dados ausentes")
print(df.isnull().mean() * 100)

# Verificar duplicidades
print("\n# Identificar registros duplicados")
print(df.duplicated().sum())

print("\n # Visualizar registros duplicados")
print(df[df.duplicated()])

# Verificar valores únicos

print("\n# Identificar valores diferentes em uma coluna")
print(df["id_cliente"].unique())
print(df["produto"].unique())
print(df["valor_compra"].unique())

print("\n# Contar ocorrências de cada valor")
print(df["id_cliente"].value_counts())
print(df["produto"].value_counts())
print(df["valor_compra"].value_counts())

print("\nRemovendo espaços")

print("# Remover espaços no início e no final das células")
df['id_cliente'] = df['id_cliente'].astype('string').str.strip()
df['produto'] = df['produto'].astype('string').str.strip()
df['valor_compra'] = df['valor_compra'].astype('string').str.strip()

print("# Verificar espaços nas colunas")
print(df['id_cliente'].str.contains(r'^\s|\s$', na=False).sum())
print(df['produto'].str.contains(r'^\s|\s$', na= False).sum())
print(df['valor_compra'].str.contains(r'^\s|\s$', na= False).sum())

print("\nRemovendo valor negativo")

df['valor_compra'] = df['valor_compra'].str.replace("R$", '', regex=False).str.strip()
df['valor_compra'] = df['valor_compra'].str.replace(",", '.', regex=False).str.strip()


df['valor_compra'] = df['valor_compra'].astype(float)

print(df['valor_compra'].dtype)
print(df['valor_compra'].head(10))

print((df['valor_compra']< 0).sum())
print(df[df['valor_compra'] < 0])

df.loc[df['valor_compra'] < 0, 'valor_compra'] = 0
print(df['valor_compra'].head(10))

print("Valores negativos restantes:", (df['valor_compra']< 0).sum())
