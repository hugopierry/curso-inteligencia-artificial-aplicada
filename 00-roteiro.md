# Curso de Inteligência Artificial Aplicada

**Tema:** IA para Desenvolvedor de Dados
**Objetivo:** preparar dados, treinar modelos simples, usar IA via API e mostrar tudo em um projeto no GitHub.
**Duração estimada:** 35 a 50 sessões de 1h a 2h (ritmo livre).
**Início:** segunda-feira, 09/11/2026

**Em cada módulo:** teoria curta → prática → desafio sozinho → revisão.
**Como estudar com o Claude:** mandar "Claude me ensina!" + o tema. Escrever o código sozinho, depois mostrar para revisão. Pontos soltos: buscar no YouTube.

---

## Estrutura da pasta

```
Curso de Inteligência Artificial Aplicada/
├── 00-roteiro.md
├── 01-fundamentos/
├── 02-dados/
├── 03-machine-learning/
├── 04-redes-neurais/
├── 05-llms-e-prompts/
├── 06-ia-com-api/
├── 07-etica-e-seguranca/
├── 08-automacao/
└── projeto-final-mini-wms-inteligente/
```

Arquivos: `.md` para anotações, `.ipynb` para exploração de dados e machine learning, `.py` para scripts e automação.

---

## Módulo 1: Fundamentos (2 a 3 sessões)

- [x] IA x machine learning x deep learning
- [ ] Aprendizado supervisionado e não supervisionado
- [x] Vocabulário: dados, features, modelo, treino, teste
- [ ] Onde a IA é usada

**Prática:** glossário com suas palavras
**Entrega:** resumo de 1 página
**Buscar no YouTube:** playlist do Realizzare Cursos (Curso Gratuito de Inteligência Artificial)

## Módulo 2: Dados para IA (4 a 6 sessões)

- [x] Limpeza com Pandas (nulos, duplicados, tipos)
- [ ] Merge e groupby
- [ ] SQL para extrair dados
- [ ] Estatística básica (média, mediana, desvio, correlação)
- [ ] Gráficos com matplotlib e Power BI

**Prática:** limpar e explorar um dataset real
**Entrega:** notebook de análise exploratória (mini-wms ou dataset do Kaggle)
**Buscar:** "limpeza de dados pandas", "estatística básica para dados"

## Módulo 3: Machine learning (8 a 10 sessões)

- [ ] scikit-learn
- [ ] Regressão linear
- [ ] Classificação (regressão logística, árvores, random forest)
- [ ] Separar treino e teste
- [ ] Métricas (erro médio, acurácia, precisão, recall)
- [ ] Overfitting
- [ ] Validação cruzada

**Prática:** um modelo de previsão e um de classificação
**Entrega:** 2 notebooks documentados no GitHub
**Buscar:** "scikit-learn iniciantes", "overfitting explicado"

## Módulo 4: Redes neurais e deep learning (3 a 4 sessões, nível conceitual)

- [ ] Neurônio e camadas
- [ ] Como a rede aprende
- [ ] Visão geral de redes para imagem e texto
- [ ] Introdução ao Keras ou PyTorch

**Prática:** reconhecer dígitos escritos à mão (exemplo clássico)
**Entrega:** notebook comentado
**Buscar:** "redes neurais para iniciantes"

## Módulo 5: IA generativa e LLMs (3 a 4 sessões)

- [ ] Como funcionam os LLMs (tokens, contexto, temperatura)
- [ ] Limites e alucinação
- [ ] Engenharia de prompt (papel, contexto, exemplos, formato de saída)
- [ ] Ideia de embeddings e RAG

**Prática:** reescrever o mesmo prompt de 3 formas e comparar
**Entrega:** guia de prompts seu

## Módulo 6: IA aplicada com API (6 a 8 sessões)

- [ ] Chamar um LLM com Python
- [ ] Chave de API em variável de ambiente (nunca no GitHub)
- [ ] Mensagens e parâmetros
- [ ] Tratar erros
- [ ] Custo e tokens
- [ ] Pedir resposta em JSON
- [ ] Integrar com Pandas e SQL

**Prática:** script que lê dados e gera um resumo em texto
**Entrega:** 2 scripts no GitHub com README
**Fonte principal:** documentação da API. Conferir os custos antes de usar.

## Módulo 7: Ética, segurança e limites (1 a 2 sessões)

- [ ] Viés
- [ ] Privacidade e LGPD
- [ ] Dados sensíveis
- [ ] Sempre validar a resposta da IA

**Entrega:** checklist de boas práticas para seus projetos

## Módulo 8: Automação (3 a 4 sessões)

- [ ] Scripts agendados
- [ ] Pipeline: banco → script → IA → Power BI
- [ ] Noção de RPA

**Prática:** automatizar uma rotina do seu projeto

---

## Projeto final: Mini-WMS Inteligente (2 a 3 semanas)

Pipeline completo:

1. SQLite (dados do mini-wms)
2. Pandas (limpeza e indicadores)
3. Um modelo simples (ex.: previsão de demanda ou classificação de giro de estoque)
4. Resumo de insights gerado por LLM via API
5. Dashboard no Power BI
6. README explicando o problema, as decisões e os resultados

**Entregáveis:**

- [ ] Repositório organizado
- [ ] Notebook e scripts documentados
- [ ] Dashboard
- [ ] README

---

## Revisões

- **Fim de cada módulo:** explicar sem consultar, responder 10 perguntas e refazer um exercício do zero
- **Toda sexta:** integração do que viu na semana
- **Antes do projeto final:** revisão geral dos módulos 2, 3 e 6

---

## Fontes gratuitas (conferir se continuam gratuitas e atualizadas)

- Realizzare Cursos (YouTube): conceitos para a semana 1
- Kaggle Learn: Pandas, Intro to Machine Learning, Intro to Deep Learning
- Google Machine Learning Crash Course: teoria e exercícios de ML
- Microsoft Learn: trilhas de fundamentos de IA
- freeCodeCamp.org (YouTube): conferir o nível de cada curso antes de começar
- StatQuest e 3Blue1Brown (YouTube): teoria de ML e redes neurais
- Documentação da API do Claude (docs.claude.com): IA aplicada com API
