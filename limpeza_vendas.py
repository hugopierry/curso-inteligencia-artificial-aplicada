# Etapas de análise e limpeza de dados

# Etapa 1 — Preparar o ambiente e importar a planilha
# Primeiro, importe a biblioteca e carregue o arquivo.



import pandas as pd

df = pd.read_excel(r"C:\\Users\\hugop\\OneDrive\\Desktop\\Curso Inteligência Artificial aplicada\\vendas_sujo.ods", engine="odf")

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

print("# Alterando o tipo dos dados para string(texto)")
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


# alterando o tipo do dado para float
df['valor_compra'] = df['valor_compra'].astype(float)

print(df['valor_compra'].dtype)
print(df['valor_compra'].head(10))

print((df['valor_compra']< 0).sum())
print(df[df['valor_compra'] < 0])

df.loc[df['valor_compra'] < 0, 'valor_compra'] = 0
print(df['valor_compra'].head(10))

print('##############################')
print("Valores nulos:", df['valor_compra'].isnull().sum())
print(df[df['valor_compra'].isnull()])
# localiza um valor que não é número (Not a Number)

df['valor_compra'] = df['valor_compra'].fillna(0)
print(df.head(55))
print("Valores nulos:", df['valor_compra'].isnull().sum())
print("Valores negativos:", (df['valor_compra'] < 0).sum())
print("Tipo de dado:", df['valor_compra'].dtype)

print("análise estatística")
print(df['valor_compra'].describe())
print(df[df['valor_compra']== 95000])
print(df[df['produto']== 'teclado'][['id_cliente', 'valor_compra']])

print("Corrigindo erro de digitação '95000' para o valor médio de um teclado '74.00'")
df.loc[df['valor_compra'] == 95000, 'valor_compra'] = 95.00
print(df[df['valor_compra']== 95.00])

print("Resgistro com valor 95000:", (df['valor_compra'] == 95000).sum())
print("Resgistro com valor 95.00:", (df['valor_compra'] == 95.00).sum())


print(df.head(56))
# Remover registros que possuem valores nulos
print("Revendo registros que possuem valores nulos")
df= df.dropna()

# Verificar novamente
print(df.isnull().sum())

print(df.head(60))

# Padronizar ID do cliente como número inteiro
df['id_cliente'] = pd.to_numeric(df['id_cliente']).astype(int)

df.to_excel(r"C:\Users\hugop\OneDrive\Desktop\Curso Inteligência Artificial aplicada\\vendas_tratada.xlsx", index= False)
print("✔ Arquivo tratado com sucesso!")
input("\n\nPressione ENTER para finalizar...")