import pandas as pd
import seaborn as sns

from sklearn.model_selection import train_test_split
# módulo do scikit-learn com as ferramentas para dividir e validar dados
# train_test_split = é a função que embaralha e separa treino e teste

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


df = sns.load_dataset("titanic")

print("Linhas e colunas: ",df.shape)
print(df.head())
print(df.info())
print(df.isna().sum())

# 1. escolher as colunas (features + alvo)
df = df[["survived","pclass","sex","age","sibsp","parch","fare"]]

# 2. preencher os nulos de age com a mediana
df["age"] = df["age"].fillna(df["age"].median())

# 3. transformar texto em número
df["sex"] = df["sex"].map({"male": 0, "female": 1})

print(df.isna().sum())
print(df.head())


# X = o que o modelo vê (features)
X = df[["pclass","sex","age","sibsp","parch","fare"]]

# y = o que ele tem que prever (alvo)
Y = df['survived']

# divide: 80% treino, 20% teste
X_treino, X_teste, Y_treino, Y_teste = train_test_split(
    X, Y, test_size =0.2, random_state=42
)

print("Treino:", X_treino.shape)
print("Teste:", X_teste.shape)

# Criar o modelo
modelo = DecisionTreeClassifier(random_state=42)

# Treinar o modelo
modelo.fit(X_treino, Y_treino)

print("Modelo treinado com sucesso!")

# Fazer previsões
previsoes = modelo.predict(X_teste)

# Comparar previsões com resultados reais
acuracia = accuracy_score(Y_teste, previsoes)

print(f"Acurária do modelo: {acuracia:.2%}")