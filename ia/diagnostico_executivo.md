# Diagnóstico Executivo com IA — WMS Logistics Analytics

## Objetivo

Utilizar Inteligência Artificial para transformar os indicadores analíticos do projeto em uma interpretação executiva, destacando problemas, possíveis causas e pontos de atenção operacional.

## Entrada dos dados

A análise utiliza os indicadores produzidos pelo projeto:

- Total de pedidos
- Pedidos atrasados
- SLA
- Tempo médio de processamento
- Desempenho por mês
- Desempenho por turno
- Desempenho por área
- Ocorrências associadas aos atrasos

## Prompt de diagnóstico

> Atue como um analista sênior de operações logísticas e Analytics.
>
> A partir dos indicadores fornecidos, produza um diagnóstico executivo objetivo.
>
> Estruture a análise em:
>
> 1. Situação geral da operação
> 2. Principais desvios de desempenho
> 3. Períodos, turnos ou áreas que merecem atenção
> 4. Principais ocorrências associadas aos atrasos
> 5. Hipóteses operacionais que devem ser investigadas
> 6. Recomendações para análise ou ação
>
> Não invente informações que não estejam presentes nos dados.
> Diferencie fatos observados de hipóteses.
> Priorize os problemas pelo impacto operacional observado.

## Exemplo de entrada

Total de pedidos: 3000  
Pedidos atrasados: 148  
SLA: 95,07%  
Tempo médio de processamento: 12,02 minutos

A análise deve considerar também os resultados das consultas mensais, por turno/área e por ocorrência.

## Resultado esperado

A IA deve transformar os indicadores técnicos em uma visão executiva compreensível para gestores, mantendo rastreabilidade entre os dados e as conclusões.

## Observação

A IA é utilizada como camada de interpretação e apoio à tomada de decisão. Os indicadores são calculados previamente por Excel/Power Query, Power BI/DAX, Python, SQL e Databricks.