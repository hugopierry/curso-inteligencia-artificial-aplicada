### 4. Merge e agrupamentos

# - [ ] Combinação de DataFrames.
# - [ ] Agrupamentos com Pandas.

# Conceito

# merge junta dois DataFrames usando uma coluna em comum (a chave). É o JOIN do SQL.
# é bastante similar ao PROCV no excel

from numpy import 
import pandas as pd

produtos = pd.DataFrame({
    "id_produto": [1,2,3,4],
    "nome": ["Parafuso","Porca","Arruela","Prego"]
})
print("="*30)
print("Tabela 1:\n")
print(produtos)

estoque = pd.DataFrame(({
    "id_produto": [1,2,3,5],
    "quantidade":[100,50,30,20]
}))
print("="*30)
print("Tabela 2:\n")
print(estoque)

print("="*30)

print("inner: só o que existe nos dois (padrão)\n")
print(pd.merge(produtos, estoque, on='id_produto', how="inner"))

print("="*30)
print("left: tudo de produtos + o que casar do estoque")
print(pd.merge(produtos, estoque, on = 'id_produto', how = "left"))

print("="*30)
print("right: tudo do estoque + o que casar de produtos\n")
print(pd.merge(produtos, estoque , on = 'id_produto', how = 'right'))

print("="*30)
print("outer: tudo dos dois\n")
print(pd.merge(produtos, estoque , on = 'id_produto', how = 'outer'))

print("="*30)
print("outer + indicator: mostra de onde veio cada linha")
print(pd.merge(produtos, estoque , on = 'id_produto', how = 'outer',indicator=True))
