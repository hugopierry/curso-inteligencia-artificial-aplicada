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

- [X] Estudar conceitos e aplicações.
- [X] Identificar fontes e formatos de dados.

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

- [X] Limpeza de dados.
- [X] Tratamento de valores nulos e duplicados.
- [X] Transformação e padronização de dados.

### 4. Merge e agrupamentos

- [ ] Combinação de DataFrames.
- [ ] Agrupamentos com Pandas.

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

**Status:** SQL revisado. Próxima etapa: aprofundar a aplicação de SQL em consultas analíticas e avançar para Pandas.