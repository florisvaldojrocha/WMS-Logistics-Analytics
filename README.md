# WMS Logistics Analytics

Projeto de **Analytics aplicado à operação logística**, utilizando dados operacionais para transformar informações de uma operação de distribuição em **indicadores, análises e diagnósticos para apoio à decisão**.

O projeto combina conhecimentos de **Logística, WMS, Dados, BI, Automação e Inteligência Artificial**, demonstrando uma aplicação prática e integrada de tecnologias voltadas à análise operacional.

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

A partir dessas respostas, os dados são transformados em informações estruturadas para apoiar a análise e a tomada de decisão operacional.

## Solução desenvolvida

O projeto utiliza diferentes tecnologias em etapas complementares:

1. **Tratamento dos dados** utilizando Excel e Power Query.
2. **Automação da atualização** utilizando VBA.
3. **Modelagem e análise** utilizando Power BI e DAX.
4. **Análise exploratória** utilizando Python e Pandas.
5. **Consultas analíticas** utilizando SQL.
6. **Processamento de dados** utilizando Databricks, Python e PySpark.
7. **Uso de Inteligência Artificial** como apoio à análise e documentação.
8. **Versionamento e documentação** utilizando Git e GitHub.
9. **Publicação do projeto** utilizando GitHub Pages.

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
             │                       │
             └──────────┬────────────┘
                        ▼
              ┌─────────────────────┐
              │ SQL / Databricks    │
              │ Análise e           │
              │ processamento       │
              └──────────┬──────────┘
                         ▼
              ┌─────────────────────┐
              │ IA                  │
              │ Apoio à análise e   │
              │ documentação        │
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

## Resultados da base analisada

A base utilizada no projeto contém **3.000 pedidos** após o tratamento dos dados.

Entre os principais indicadores apresentados no projeto estão:

* **3.000** pedidos analisados;
* **148** pedidos atrasados;
* **95,07%** de SLA global;
* **12,02 minutos** de tempo médio de processamento.

Esses indicadores são utilizados como referência para as análises apresentadas no Excel e no Power BI.

## Dashboard

O projeto possui um dashboard desenvolvido em **Power BI**, permitindo visualizar os principais indicadores operacionais e realizar análises por diferentes dimensões da operação.

A proposta é transformar os dados operacionais em uma visão gerencial que facilite a identificação de desvios e pontos de atenção.

## Automação

O arquivo Excel possui automação utilizando **VBA** para apoiar o processo de atualização dos dados e indicadores.

A automação permite reduzir atividades manuais e tornar o processo de atualização mais padronizado.

## Análise com Python

A etapa de Python utiliza **Pandas** para análise e exploração dos dados, permitindo complementar as análises realizadas no Power BI.

Os arquivos relacionados à análise em Python estão disponíveis no diretório:

```text
/python
```

## SQL

O projeto também utiliza **SQL** para demonstrar consultas analíticas aplicadas aos dados operacionais.

Os arquivos SQL estão disponíveis no diretório:

```text
/sql
```

## Databricks

A etapa de Databricks utiliza **Python/PySpark e SQL** para demonstrar uma abordagem de processamento e análise de dados em ambiente de dados.

Os arquivos relacionados ao processamento estão disponíveis no diretório:

```text
/databricks
```

## Inteligência Artificial

A Inteligência Artificial foi utilizada como ferramenta de apoio durante o desenvolvimento do projeto, incluindo análise, documentação, estruturação e exploração dos dados.

Os prompts utilizados no projeto estão documentados no arquivo:

```text
/ia/prompts.md
```

A documentação permite consultar e reproduzir as principais instruções utilizadas durante o desenvolvimento.

## Estrutura do projeto

```text
WMS-Logistics-Analytics/
│
├── Excel/
│   └── vba/
│       ├── LogiAnalytics_Base_WMS_Dados tratados .xlsx
│       └── WMS_Logistics_Analytics.xlsm
│
├── databricks/
│   └── WMS_Logistics_Analytics.py
│
├── ia/
│   └── prompts.md
│
├── python/
│   └── analise_logistica.py
│
├── sql/
│   └── consultas_analiticas.sql
│
├── WMS_Logistics_Analytics.pbix
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

### Logística

Processos operacionais, indicadores, SLA, atrasos e análise de gargalos.

### WMS

Visão orientada a processos e dados de uma operação logística.

### Dados

Tratamento, transformação, análise e interpretação de dados operacionais.

### BI

Criação de indicadores, análises e dashboard.

### Programação

Python, Pandas, PySpark, SQL e VBA.

### Tecnologia

Git, GitHub, Databricks e publicação web.

### IA

Utilização de prompts como apoio à análise, documentação e desenvolvimento.

## Portfólio online

O projeto possui uma página própria com acesso aos principais componentes do portfólio:

**GitHub • Excel/VBA • Power BI • Python • SQL • Databricks • IA/Prompts**

## Status do projeto

**Projeto em desenvolvimento contínuo.**

A estrutura principal do projeto está disponível no GitHub, com os arquivos de análise, automação, BI, programação, processamento de dados, documentação e página de portfólio.
