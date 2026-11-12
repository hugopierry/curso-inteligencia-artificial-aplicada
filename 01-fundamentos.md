# Inteligência Artificial (IA)

Trata do desenvolvimento de sistemas de computador que podem executar tarefas que normalmente requerem inteligência humana, como percepção visual, reconhecimento de fala, tomada de decisão e processamento de linguagem natural.

Campo extenso da tecnologia que engloba vários subcampos, incluindo aprendizado de máquina e aprendizado profundo.

IA é a simulação da inteligência humana feita por máquinas programadas pelos humanos.

---

# Machine Learning (ML)

### Aprendizado de Máquina

- Termo criado nos anos 1950.
- Subcampo da IA que se concentra no desenvolvimento de algoritmos e modelos estatísticos que permitem aos computadores aprender com conjuntos de dados.
- Emprega algoritmos que podem identificar padrões nos dados e fazer previsões com base nesses dados.
- Fornece a base para o aprendizado profundo.
- Implementa a ideia de que as máquinas podem aprender com os dados, em vez de serem sempre explicitamente programadas.

---

# Deep Learning (DL)

### Aprendizado Profundo

- Divisão do ML (e da IA) que se concentra em treinar redes neurais profundas a partir de grandes conjuntos de dados não estruturados.
- **Objetivo:** simular o comportamento do cérebro humano para que as máquinas aprendam e executem tarefas altamente complexas.
- "Profundo" se refere ao uso de múltiplas camadas na rede neural artificial, o que permite ao algoritmo aprender e modelar representações cada vez mais abstratas dos dados.

---

# Aprendizado supervisionado e não supervisionado

## Aprendizado supervisionado

- O modelo é treinado usando dados rotulados (ou seja, cada exemplo de entrada vem acompanhado da resposta correta ou saída esperada).

**Objetivo:** aprender a mapear a entrada para a saída correta, a fim de prever resultados ou classificar novos dados.

**Principais tarefas:**

- **Classificação:** rótulos discretos (ex.: detectar se um e-mail é spam ou não spam, identificar imagens de gatos).
- **Regressão:** valores numéricos contínuos (ex.: prever o preço de uma casa ou o salário de um profissional com base no histórico).

**Exemplo prático:** você alimenta o sistema com milhares de fotos de frutas já identificadas como "maçã" ou "banana" para que ele aprenda a classificar uma foto nova.

---

## Aprendizado não supervisionado

- O modelo trabalha com dados não rotulados (sem respostas ou supervisão prévia). O algoritmo analisa os dados por conta própria para descobrir estruturas, semelhanças, anomalias ou padrões ocultos.

**Objetivo:** explorar os dados e encontrar padrões, agrupamentos ou reduzir a complexidade da informação.

**Principais tarefas:**

- **Agrupamento (Clustering):** juntar itens parecidos (ex.: segmentação de clientes por hábitos de compra).
- **Associação:** descobrir regras de coocorrência (ex.: produtos que costumam ser comprados juntos no supermercado).
- **Redução de dimensionalidade:** simplificar dados complexos, mantendo as informações mais importantes (ex.: PCA).

**Exemplo prático:** uma base de dados de clientes de um e-commerce na qual o algoritmo separa automaticamente os compradores em 4 grupos diferentes, baseando-se apenas no comportamento de navegação, sem que você diga quem é quem.

---

# Modelos, algoritmos e features

## Features (Atributos / Variáveis)

**O que são:** são as características, colunas ou variáveis de entrada extraídas dos dados brutos que representam uma propriedade do problema.

**Exemplo:** em uma base de dados para prever o risco de crédito de um cliente, as features podem ser: idade, renda mensal, histórico de dívidas e tempo de emprego.

**Engenharia de Features:** é o processo de criar, transformar ou selecionar as melhores variáveis para aumentar o poder preditivo do sistema.

## Algoritmos

**O que são:** são as regras matemáticas e sequências lógicas de treinamento que "aprendem" os padrões escondidos dentro dos dados.

**Exemplos comuns:** Regressão Logística, Árvores de Decisão, Random Forest (Floresta Aleatória), XGBoost e K-Nearest Neighbors (KNN).

**Função:** eles recebem os dados de entrada (features e labels) e executam o processo de otimização.

## Modelos

**O que são:** são os produtos finais gerados depois que os algoritmos são treinados com um conjunto de dados. O modelo é a "instância" ou a estrutura gravada que consegue fazer previsões em novos dados que nunca viu antes.

**Exemplo:** o arquivo salvo em código que recebe a idade e a renda de um novo cliente e responde: "Risco de inadimplência: Baixo".