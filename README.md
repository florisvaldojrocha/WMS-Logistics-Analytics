# WMS Logistics Analytics

Projeto de **Analytics aplicado à operação logística**, utilizando dados operacionais para transformar informações de uma operação de distribuição em **indicadores, análises e diagnósticos para apoio à decisão**.

O projeto combina conceitos de **Logística, WMS, Dados, BI, Automação e Inteligência Artificial**, simulando uma aplicação prática que pode ser utilizada como apoio à gestão operacional.

## Objetivo

Transformar dados operacionais em informações gerenciais capazes de identificar:

* desempenho do SLA;
* volume de pedidos;
* pedidos atrasados;
* tempo médio de processamento;
* concentração de atrasos por período;
* áreas e turnos críticos;
* ocorrências associadas aos atrasos;
* possíveis gargalos operacionais.

## Problema de negócio

Em uma operação logística, acompanhar somente o volume de pedidos não é suficiente para identificar problemas de desempenho.

O projeto busca responder perguntas como:

> **Onde estão ocorrendo os atrasos?**

> **Quando os atrasos acontecem?**

> **Quais áreas e turnos apresentam maior impacto?**

> **Quais ocorrências estão associadas aos pedidos atrasados?**

A partir dessas respostas, os dados são transformados em informações que podem apoiar a análise e a tomada de decisão operacional.

## Solução desenvolvida

O projeto utiliza diferentes tecnologias para trabalhar as informações em etapas complementares:

1. **Tratamento dos dados** utilizando Excel e Power Query.
2. **Automação de atualização** utilizando VBA.
3. **Modelagem e análise** utilizando Power BI e DAX.
4. **Análise exploratória** utilizando Python e Pandas.
5. **Processamento de dados** utilizando Databricks, Python/PySpark e SQL.
6. **Diagnóstico operacional** utilizando Inteligência Artificial.
7. **Versionamento e documentação** utilizando Git e GitHub.
8. **Publicação do projeto** utilizando GitHub Pages.

## Tecnologias utilizadas

* Excel
* Power Query
* VBA
* Power BI
* DAX
* Python
* Pandas
* PySpark
* SQL
* Databricks
* Inteligência Artificial
* Git
* GitHub
* GitHub Pages

## Fluxo do projeto

```text
                 DADOS OPERACIONAIS
                         │
                         ▼
              ┌─────────────────────┐
              │ Excel / Power Query │
              │ Tratamento dos dados│
              └──────────┬──────────┘
                         │
             ┌───────────┴───────────┐
             ▼                       ▼
      ┌──────────────┐       ┌──────────────┐
      │ Power BI/DAX │       │ Python/Pandas│
      │ Indicadores  │       │ Análise      │
      └──────┬───────┘       └──────┬───────┘
             │                      │
             └──────────┬───────────┘
                        ▼
              ┌─────────────────────┐
              │ Databricks / PySpark│
              │ Processamento       │
              └──────────┬──────────┘
                         ▼
                    ┌─────────┐
                    │  SQL    │
                    │ Análises│
                    └────┬────┘
                         ▼
              ┌─────────────────────┐
              │ Diagnóstico         │
              │ operacional         │
              └──────────┬──────────┘
                         ▼
              ┌─────────────────────┐
              │ IA / Diagnóstico    │
              │ executivo           │
              └──────────┬──────────┘
                         ▼
              ┌─────────────────────┐
              │ Git / GitHub        │
              │ GitHub Pages        │
              └─────────────────────┘
```

## Indicadores analisados

Entre os principais indicadores e análises do projeto estão:

* SLA operacional;
* volume de pedidos;
* quantidade de pedidos atrasados;
* percentual de atraso;
* tempo médio de processamento;
* distribuição dos pedidos por turno;
* concentração de atrasos;
* ocorrências operacionais;
* análise por área;
* identificação de pontos críticos.

## Dashboard

O projeto possui um dashboard desenvolvido em **Power BI**, permitindo visualizar os principais indicadores operacionais e realizar análises por diferentes dimensões da operação.

A proposta é transformar os dados operacionais em uma visão gerencial que facilite a identificação de desvios e pontos de atenção.

## Automação

O arquivo Excel possui automação utilizando **VBA** para apoiar o processo de atualização dos dados e indicadores.

A automação permite reduzir atividades manuais e tornar o processo de atualização mais padronizado.

## Análise com Python

A etapa de Python utiliza **Pandas** para análise e exploração dos dados, permitindo complementar as análises realizadas no Power BI.

## Databricks

A etapa de Databricks utiliza **Python/PySpark e SQL** para demonstrar uma abordagem de processamento e análise de dados em ambiente de dados.

## Inteligência Artificial

A Inteligência Artificial é utilizada como apoio à interpretação dos resultados e elaboração de diagnósticos operacionais.

Os prompts utilizados no desenvolvimento do projeto estão documentados no diretório:

```text
/ia/prompts.md
```

A documentação permite reproduzir as etapas de utilização da IA no projeto.

## Estrutura do projeto

```text
WMS-Logistics-Analytics/
│
├── Excel/
│   └── vba/
│
├── databricks/
│
├── ia/
│
├── python/
│
├── sql/
│
├── site/
│
├── index.html
├── script.js
├── style.css
├── README.md
└── .gitignore
```

## Aplicação profissional

O projeto foi desenvolvido com foco em uma situação próxima à realidade de uma operação logística, utilizando dados para apoiar:

* acompanhamento de desempenho;
* identificação de gargalos;
* análise de atrasos;
* acompanhamento de indicadores;
* diagnóstico operacional;
* suporte à tomada de decisão.

A proposta é demonstrar como conhecimentos de **Logística + WMS + Dados + Tecnologia** podem ser combinados em uma solução prática de Analytics.

## Perfil técnico demonstrado

O projeto demonstra a aplicação integrada de conhecimentos em:

**Logística**
→ processos operacionais, indicadores, SLA, atrasos e análise de gargalos.

**WMS**
→ visão orientada a processos e dados de uma operação logística.

**Dados**
→ tratamento, transformação, análise e interpretação de dados operacionais.

**BI**
→ criação de indicadores, análises e dashboard.

**Programação**
→ Python, Pandas, PySpark, SQL e VBA.

**Tecnologia**
→ Git, GitHub, Databricks e publicação web.

**IA**
→ utilização de prompts para apoio à análise e diagnóstico.

## Status do projeto

**Projeto em desenvolvimento contínuo.**

Novas análises, melhorias no dashboard, automações e documentação poderão ser incorporadas ao longo da evolução do portfólio.
