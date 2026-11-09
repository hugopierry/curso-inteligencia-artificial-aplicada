## Comentários — conceitos de Machine Learning

- Dados desbalanceados: 
Quantidade alta de um status, e menor quantidade de outro, não ensina nada ao sistema.
Pois o modelo pode favorecer a classe majotitária.

- Rótulo (label):
É a resposta que o sistema prevê, como o motivo de ressalvas. Precisa ser dados precisos. 

- Features:
São tipos de entradas, lembrando os dados informados nos "inputs" pelo usuário.
Dados que o sistema usa para encontrar padrões.

- Hipótese x estatística:
O "acho", ou suposição, só vira estatísticas quando meidido através de dados em GROUP BY + COUNT:

Exemplo: 

SELECT tipo_carga, COUNT(*) AS total_ressalvas
FROM ressalvas
GROUP BY tipo_carga;


## Padronização de strings 

- Ache
- ACHE
- Áche
- ache  (com espaço)

Deve usar:

SELECT DISTINCT
    UPPER(TRIM(nome)) AS nome_padronizado
FROM fornecedor;

## Segunda etapa: remover acentos no SQLite.

SELECT DISTINCT
    UPPER(
        REPLACE(
            REPLACE(
                REPLACE(
                    REPLACE(
                        TRIM(nome),
                        'é', 'e'
                    ),
                    'É', 'E'
                ),
                'á', 'a'
            ),
            'Á', 'A'
        )
    ) AS nome_padronizado
FROM fornecedores;
- TRIM(nome) : remove espaços em branco que estão no início e no final do texto.

- Exemplo:

Original	        Resultado
Ache	             Ache
    Aché	         Aché
ACHE  (espaço)	     ACHE

- REPLACE()
O REPLACE() substitui um determinado caractere ou texto por outro.

- Exemplo: 
REPLACE(texto_original, texto_a_substituir, substituto)

- ③ Segundo REPLACE()

REPLACE(
    REPLACE(TRIM(nome), 'é', 'e'),
    'É', 'E'
)

- AS nome_padronizado

Cria um nome alternativo para a coluna exibida no resultado da consulta.

É chamado de alias.

Não altera o nome original no banco de dados.

- ⑥ SELECT DISTINCT
Elimina os valores duplicados do resultado.

## Resultado:

Original	Padronizado
Ache	        ACHE
Aché	        ACHE
ACHE	        ACHE
ache	        ACHE
ACHE	        ACHE