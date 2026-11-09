## Comentários: 

- Dados desbalanceados: 
Quantidade alta de um status, e menor quantidade d eoutro, não ensina nada ao sistema.

- Rótulo:
É a resposta que o sistema prevê, como o motivo de ressalvas. Precisa ser dados precisos. 

- Features:
São tipos de entradas, lembrando os dados informados nos "inputs" pelo usuário.

- Hipótese x estatística:
O "acho", ou suposição, só vira estatísticas quando meidido através de dados em GROUP BY + COUNT:

Exemplo: 
'''sql
SELECT tipo_carga, COUNT(*) AS total_ressalvas
FROM ressalvas
GROUP BY tipo_carga;
'''

