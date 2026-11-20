# 02. Engenharia e Preparação de Dados

## Conteúdo programático

- Coleta e estruturação de dados.
- SQL: SELECT, WHERE, JOIN e GROUP BY.
- Pandas: limpeza e transformação de dados.
- Merge e agrupamentos.
- Estatística: média, mediana e desvio padrão.
- Correlação e distribuição.
- Visualização de dados com Matplotlib.

---

## Acompanhamento dos estudos

### 1. Coleta e estruturação de dados

- [x] Estudar conceitos e aplicações.
- [x] Identificar fontes e formatos de dados.

### 2. SQL

- [x] SELECT.
- [x] WHERE.
- [x] JOIN.
- [x] GROUP BY.
- [x] HAVING.
- [x] Funções de agregação.

**Registro de estudo:** revisão realizada em 13/11/2026, utilizando SQLite.

**Prática complementar:** relacionamentos entre tabelas de clientes e vendas, utilizando INNER JOIN, LEFT JOIN, RIGHT JOIN e FULL JOIN.

### 3. Pandas

- [x] Limpeza de dados.
- [x] Tratamento de valores nulos e duplicados.
- [x] Transformação e padronização de dados.

### 4. Merge e agrupamentos

- [x] Combinação de DataFrames.
- [x] Aplicação dos métodos INNER, LEFT, RIGHT e OUTER.
- [x] Utilização do parâmetro indicator=True.
- [x] Agrupamentos com Pandas (groupby).

**Registro de estudo:** prática realizada em 19/11/2026, utilizando DataFrames de produtos e estoque.

**Prática complementar:** combinação de tabelas utilizando a coluna id_produto como chave de relacionamento, analisando os registros correspondentes e não correspondentes.

### 5. Estatística

- [ ] Média.
- [ ] Mediana.
- [ ] Desvio padrão.

### 6. Correlação e distribuição

- [ ] Análise de correlação.
- [ ] Distribuição dos dados.

### 7. Visualização com Matplotlib

- [ ] Construção de gráficos.
- [ ] Visualização e interpretação dos dados.

---

# Prática SQL — Relacionamento entre tabelas

**Base de estudo:** Clientes e Vendas (SQLite).

**Tabelas utilizadas:**
- `clientes`: id_cliente, nome e cidade.
- `vendas`: id_venda, id_cliente, produto e valor_compra.

**Objetivo:** compreender como relacionar tabelas utilizando chaves em comum e aplicar filtros nas consultas SQL.

## 1. INNER JOIN

O INNER JOIN combina registros de duas tabelas, retornando somente aqueles que possuem correspondência nas duas.

```sql
/*
INNER JOIN:
Retorna somente os registros que possuem correspondência
entre as tabelas clientes e vendas.

Clientes sem vendas não aparecem no resultado.
*/

SELECT
    clientes.nome,
    vendas.produto,
    vendas.valor_compra
FROM clientes
INNER JOIN vendas
    ON clientes.id_cliente = vendas.id_cliente;

-- Resultado esperado: 10 linhas.
-- Diego e Gabriela não aparecem, pois não possuem vendas.
-- Carla aparece 3 vezes, pois realizou 3 compras.
```

## 2. INNER JOIN + WHERE

O WHERE permite filtrar os registros retornados pelo JOIN, conforme uma condição específica.

**2.1. Compras acima de R$ 200,00**

```sql
SELECT
    clientes.nome,
    vendas.produto,
    vendas.valor_compra
FROM clientes
INNER JOIN vendas
    ON clientes.id_cliente = vendas.id_cliente
WHERE vendas.valor_compra > 200;

-- Resultado esperado: 6 linhas.
```

**2.2. Compras abaixo de R$ 200,00**

```sql
SELECT
    clientes.nome,
    vendas.produto,
    vendas.valor_compra
FROM clientes
INNER JOIN vendas
    ON clientes.id_cliente = vendas.id_cliente
WHERE vendas.valor_compra < 200;

-- Resultado esperado: 4 linhas.
```

**2.3. Compras acima de R$ 500,00**

```sql
SELECT
    clientes.nome,
    vendas.produto,
    vendas.valor_compra
FROM clientes
INNER JOIN vendas
    ON clientes.id_cliente = vendas.id_cliente
WHERE vendas.valor_compra > 500;

-- Resultado esperado: 2 linhas.
-- Ambas correspondem a compras de Monitor.
```

**Observação:** valores exatamente iguais a R$ 200,00 não entram nas condições `>` ou `<`. Para incluir o valor limite, utilize `>=` ou `<=`.

## 3. LEFT JOIN

O LEFT JOIN mantém todos os registros da tabela posicionada no FROM, mesmo quando não existe correspondência na segunda tabela.

Quando não existe correspondência, as colunas da tabela da direita retornam NULL.

```sql
SELECT
    clientes.nome,
    vendas.produto,
    vendas.valor_compra
FROM clientes
LEFT JOIN vendas
    ON clientes.id_cliente = vendas.id_cliente;

-- Resultado esperado: 12 linhas.
-- Inclui os 10 registros de vendas e os 2 clientes sem compras.
```

**3.1. Identificando clientes que não realizaram compras**

```sql
SELECT
    clientes.nome
FROM clientes
LEFT JOIN vendas
    ON clientes.id_cliente = vendas.id_cliente
WHERE vendas.id_venda IS NULL;

-- Resultado esperado: 2 linhas.
-- Diego Alves e Gabriela Nunes.
```

**Observação:** para identificar valores nulos, utilizamos `IS NULL`, e não `= NULL`.

## 4. RIGHT JOIN

O RIGHT JOIN mantém todos os registros da tabela posicionada à direita do JOIN, mesmo quando não existe correspondência na tabela da esquerda.

```sql
SELECT
    clientes.nome,
    vendas.produto,
    vendas.valor_compra
FROM clientes
RIGHT JOIN vendas
    ON clientes.id_cliente = vendas.id_cliente;

-- Resultado esperado: 10 linhas.
-- Todas as vendas possuem um cliente correspondente.
```

**Alternativa utilizando LEFT JOIN**

O mesmo resultado pode ser obtido invertendo a ordem das tabelas:

```sql
SELECT
    clientes.nome,
    vendas.produto,
    vendas.valor_compra
FROM vendas
LEFT JOIN clientes
    ON clientes.id_cliente = vendas.id_cliente;
```

## 5. FULL JOIN

O FULL JOIN retorna todos os registros das duas tabelas, incluindo aqueles que não possuem correspondência.

Quando não existe relacionamento, as colunas da tabela sem correspondência recebem NULL.

```sql
SELECT
    clientes.nome,
    vendas.produto,
    vendas.valor_compra
FROM clientes
FULL JOIN vendas
    ON clientes.id_cliente = vendas.id_cliente;

-- Resultado esperado: 12 linhas.
-- Inclui todas as vendas e os clientes sem compras.
```

**Observação:** o SQLite oferece suporte a FULL JOIN a partir da versão 3.39.0. A mesma versão mínima se aplica ao RIGHT JOIN.

---

## 6. Resumo dos JOINs

| Tipo | Comportamento |
|---|---|
| INNER JOIN | Somente registros correspondentes. |
| LEFT JOIN | Todos os registros da tabela esquerda. |
| RIGHT JOIN | Todos os registros da tabela direita. |
| FULL JOIN | Todos os registros das duas tabelas. |

---

# Prática Pandas — Combinação de DataFrames

**Base de estudo:** DataFrames de Produtos e Estoque (Python e Pandas).

**Data:** 19/11/2026.

**Objetivo:** compreender como combinar DataFrames utilizando uma chave em comum e identificar registros correspondentes e não correspondentes.

## 1. Estruturação dos DataFrames

Foram criados dois DataFrames:

- `produtos`: contém o identificador e o nome dos produtos.
- `estoque`: contém o identificador dos produtos e suas respectivas quantidades.

A coluna `id_produto` foi utilizada como chave de relacionamento.

## 2. INNER — Registros correspondentes

Retorna somente os registros que possuem correspondência nos dois DataFrames.

```python
pd.merge(produtos, estoque, on='id_produto', how='inner')
```

**Resultado:** produtos com correspondência nas duas tabelas.

## 3. LEFT — Mantém o DataFrame da esquerda

Retorna todos os registros de `produtos` e os dados correspondentes de `estoque`.

```python
pd.merge(produtos, estoque, on='id_produto', how='left')
```

**Resultado:** todos os produtos, inclusive aqueles sem quantidade cadastrada no estoque.

## 4. RIGHT — Mantém o DataFrame da direita

Retorna todos os registros de `estoque` e os dados correspondentes de `produtos`.

```python
pd.merge(produtos, estoque, on='id_produto', how='right')
```

**Resultado:** todos os registros de estoque, inclusive aqueles sem produto correspondente no cadastro.

## 5. OUTER — União dos registros

Retorna todos os registros dos dois DataFrames, independentemente de possuírem correspondência.

```python
pd.merge(produtos, estoque, on='id_produto', how='outer')
```

**Resultado:** todos os produtos e registros de estoque, incluindo os não correspondentes.

## 6. OUTER + INDICATOR — Identificação da origem

O parâmetro `indicator=True` adiciona uma coluna chamada `_merge`, que identifica a origem de cada registro.

```python
pd.merge(
    produtos,
    estoque,
    on='id_produto',
    how='outer',
    indicator=True
)
```

A coluna `_merge` apresenta três classificações:

| Classificação | Significado |
|---|---|
| both | Registro encontrado nos dois DataFrames. |
| left_only | Registro encontrado somente no DataFrame da esquerda. |
| right_only | Registro encontrado somente no DataFrame da direita. |

**Aprendizado:** o parâmetro `indicator=True` permite identificar divergências entre bases de dados, sendo útil em processos de conferência, integração e validação de informações.

---

## Projeto prático

**Base de dados:** Pizzaria (SQLite e Python).

**Objetivo:** preparar, limpar, transformar e analisar dados utilizando ferramentas de análise de dados.

**Metodologia de aprendizagem:**

1. Aprender os conceitos.
2. Registrar o conteúdo.
3. Aplicar em projetos práticos.
4. Validar os resultados.
5. Documentar a evolução dos estudos.

---

**Status:** SQL revisado. Pandas: limpeza, transformação e combinação de DataFrames concluídas. 

**Próxima etapa:** agrupamentos com Pandas (`groupby`), seguido de estatística descritiva.