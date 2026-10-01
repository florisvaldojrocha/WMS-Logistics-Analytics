# Prompts de IA — WMS Logistics Analytics

## Objetivo

Este documento registra os prompts utilizados durante o desenvolvimento do projeto **WMS Logistics Analytics**.

A IA (Google Gemini) foi utilizada como apoio em todas as etapas do projeto: geração de massa de testes sintética via Python no Google Colab, arquitetura do pipeline, diagnóstico de causas-raiz de atrasos, documentação técnica do repositório no GitHub e construção do portfólio web executivo para publicação no GitHub Pages.

---

> 1. Geração da base bruta WMS para teste de automação (Google Colab)

### Prompt

> Atue como um Engenheiro de Dados WMS sênior. Crie uma planilha de dados brutos no formato XLSX para testes de estresse e validação do pipeline de automação (Power Query + Power BI).
>
> ---
>
> 1. ESPECIFICAÇÃO DE ARQUIVO E ESTRUTURA
>    1.1. Nome exato do arquivo: "LogiAnalytics_Base_WMS_Bruta(1).xlsx"
>    1.2. Nome exato da aba interna: "WMS_OUTBOUND_BRUTO"
>
> ---
>
> 2. ESTRUTURA RIGOROSA DAS COLUNAS (MAPEAMENTO A À O)
>    2.1. Coluna A (Data): Formato DD/MM/AAAA. Intervalo de datas cobrindo os meses de Junho, Julho e Agosto de 2026.
>    2.2. Coluna B (Pedido): Formato 'PED100001' a 'PED103000' (6 dígitos numéricos).
>    2.3. Coluna C (SKU): Formato 'SKU001' a 'SKU012'.
>    2.4. Coluna D (Produto): Descrição do produto associado ao SKU.
>    2.5. Coluna E (Quantidade): Valor inteiro entre 1 e 15 unidades.
>    2.6. Coluna F (Operador): Código de 'OP001' a 'OP045'.
>        2.6.1. Turno 1: OP001 até OP015
>        2.6.2. Turno 2: OP016 até OP030
>        2.6.3. Turno 3: OP031 até OP045
>    2.7. Coluna G (Turno): '1º Turno', '2º Turno' ou '3º Turno'.
>    2.8. Coluna H (Area): 'Picking A', 'Picking B' ou 'Picking C'.
>    2.9. Coluna I (Hora_Inicio): Formato de hora HH:MM:SS.
>    2.10. Coluna J (Hora_Fim): Formato de hora HH:MM:SS (obrigatório ser posterior à Hora_Inicio no mesmo dia).
>    2.11. Coluna K (Status): Status do WMS ('Concluído' ou 'Atrasado').
>    2.12. Coluna L (SLA_Min): Valor numérico fixo de tempo meta (20 minutos).
>    2.13. Coluna M (Ocorrencia): Motivo operacional ('Sem ocorrência', 'Avaria', 'Divergência', 'Reprocesso', 'Endereço bloqueado', 'Falta de estoque').
>    2.14. Coluna N (Doca): Identificador da doca de 'D01' a 'D08'.
>    2.15. Coluna O (CD): Fixo 'CD Jundiaí'.
>
> ---
>
> 3. REGRAS DE NEGÓCIO E SIMULAÇÃO DE ERROS (STRESS TEST)
>    3.1. Volumetria Total: Gerar exatas 3.023 linhas (3.000 válidas + 20 duplicadas + 3 nulas).
>    3.2. Metas e Indicadores Executivos:
>        3.2.1. Total de Pedidos Válidos: 3.000 pedidos.
>        3.2.2. Total de Pedidos Atrasados: Exatamente 148 pedidos.
>        3.2.3. SLA Global: Exatamente 95,07%.
>        3.2.4. Tempo Médio de Processamento Global: Exatamente 12,02 minutos.
>    3.3. Concentração do Gargalo Operational:
>        3.3.1. Concentração Temporal: 100% dos 148 atrasos no mês de JUNHO/2026.
>        3.3.2. Concentração de Turno: 100% dos 148 atrasos no '3º Turno'.
>        3.3.3. Causa Raiz / Ofensores: Concentrados em 6 operadores (OP031 a OP036).
>        3.3.4. Performance dos Demais Períodos: Julho e Agosto com 100% de entregas no prazo (SLA perfeito).
>
> ---
>
> 4. INSTRUÇÕES DO PIPELINE DE AUTOMAÇÃO
>    4.1. Passo 1 - Geração via Google Colab (Python):
>        4.1.1. Executar o script Python no ambiente em nuvem.
>        4.1.2. Baixar o arquivo bruto gerado `LogiAnalytics_Base_WMS_Bruta(1).xlsx`.
>    4.2. Passo 2 - Organização de Pastas:
>        4.2.1. Mover o arquivo para o diretório raiz de vba.
>        4.2.2. Renomear o arquivo para `LogiAnalytics_Base_WMS_Bruta.xlsx`.
>    4.3. Passo 3 - Processamento no Excel:
>        4.3.1. Abrir `WMS_Logistics_Analytics.xlsm`.
>        4.3.2. Ir para a aba `00_Painel_de_Controle`.
>        4.3.3. Clicar no botão `ATUALIZAR INDICADORES`.
>        4.3.4. Salvar (`Ctrl + S`) e fechar o arquivo.
>    4.4. Passo 4 - Atualização Executiva no Power BI:
>        4.4.1. Abrir o relatório `WMS_Logistics_Analytics.pbix`.
>        4.4.2. Na aba 'Página Inicial', clicar em `Atualizar`.

> 5. Código Python completo para execução no Google Colab

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Fixar semente para garantir repetibilidade exata dos indicadores
np.random.seed(42)
random.seed(42)

# 1. Estruturas Auxiliares
skus_produtos = {
    'SKU001': 'Smartphone A', 'SKU002': 'Notebook 15', 'SKU003': 'Monitor 24',
    'SKU004': 'Fone Bluetooth', 'SKU005': 'Teclado Mecânico', 'SKU006': 'Cabo HDMI',
    'SKU007': 'Mouse', 'SKU008': 'Impressora', 'SKU009': 'Tablet',
    'SKU010': 'Roteador', 'SKU011': 'Webcam', 'SKU012': 'Carregador Fast'
}

areas = ['Picking A', 'Picking B', 'Picking C']
docas = [f'D0{i}' for i in range(1, 9)]
ocorrencias_erro = ['Avaria', 'Divergência', 'Reprocesso', 'Endereço bloqueado', 'Falta de estoque']

datas_junho = pd.date_range(start='2026-06-01', end='2026-06-30').strftime('%d/%m/%Y').tolist()
datas_julho = pd.date_range(start='2026-07-01', end='2026-07-31').strftime('%d/%m/%Y').tolist()
datas_agosto = pd.date_range(start='2026-08-01', end='2026-08-31').strftime('%d/%m/%Y').tolist()

registros = []

# 2. Gerar os 148 Pedidos Atrasados (Junho / 3º Turno / OP031 a OP036)
for i in range(1, 149):
    ped_id = f"PED{100000 + i}"
    data = random.choice(datas_junho)
    sku, produto = random.choice(list(skus_produtos.items()))
    qtd = random.randint(1, 15)
    operador = f"OP0{random.randint(31, 36)}"
    turno = '3º Turno'
    area = random.choice(areas)
    
    h_inicio_dt = datetime.strptime(f"{random.randint(20, 22):02d}:{random.randint(0, 30):02d}:{random.randint(0, 59):02d}", "%H:%M:%S")
    duracao_min = random.randint(25, 36)
    h_fim_dt = h_inicio_dt + timedelta(minutes=duracao_min)
    
    status = 'Atrasado'
    sla_min = 20
    ocorrencia = random.choice(ocorrencias_erro)
    doca = random.choice(docas)
    cd = 'CD Jundiaí'
    
    registros.append([data, ped_id, sku, produto, qtd, operador, turno, area, 
                      h_inicio_dt.strftime("%H:%M:%S"), h_fim_dt.strftime("%H:%M:%S"), 
                      status, sla_min, ocorrencia, doca, cd])

# 3. Gerar os 2.852 Pedidos Normais / Concluídos
for i in range(149, 3001):
    ped_id = f"PED{100000 + i}"
    mes_escolha = random.choices(['junho', 'julho', 'agosto'], weights=[0.25, 0.38, 0.37])[0]
    
    if mes_escolha == 'junho':
        data = random.choice(datas_junho)
    elif mes_escolha == 'julho':
        data = random.choice(datas_julho)
    else:
        data = random.choice(datas_agosto)
        
    sku, produto = random.choice(list(skus_produtos.items()))
    qtd = random.randint(1, 15)
    
    turno = random.choice(['1º Turno', '2º Turno', '3º Turno'])
    if turno == '1º Turno':
        operador = f"OP0{random.randint(1, 15):02d}"
    elif turno == '2º Turno':
        operador = f"OP0{random.randint(16, 30):02d}"
    else:
        if mes_escolha == 'junho':
            operador = f"OP0{random.randint(37, 45):02d}"
        else:
            operador = f"OP0{random.randint(31, 45):02d}"
            
    area = random.choice(areas)
    
    h_inicio_dt = datetime.strptime(f"{random.randint(6, 20):02d}:{random.randint(0, 30):02d}:{random.randint(0, 59):02d}", "%H:%M:%S")
    duracao_min = random.randint(5, 17)
    h_fim_dt = h_inicio_dt + timedelta(minutes=duracao_min)
    
    status = 'Concluído'
    sla_min = 20
    ocorrencia = 'Sem ocorrência'
    doca = random.choice(docas)
    cd = 'CD Jundiaí'
    
    registros.append([data, ped_id, sku, produto, qtd, operador, turno, area, 
                      h_inicio_dt.strftime("%H:%M:%S"), h_fim_dt.strftime("%H:%M:%S"), 
                      status, sla_min, ocorrencia, doca, cd])

# Embaralhar registros válidos
random.shuffle(registros)

# 4. Estresse de Dados (20 Duplicadas + 3 Linhas Nulas)
duplicadas = random.sample(registros, 20)
registros.extend(duplicadas)

linha_vazia = [None] * 15
registros.insert(500, linha_vazia)
registros.insert(1500, linha_vazia)
registros.insert(2500, linha_vazia)

# 5. Exportação para XLSX
colunas = ['Data', 'Pedido', 'SKU', 'Produto', 'Quantidade', 'Operador', 
           'Turno', 'Area', 'Hora_Inicio', 'Hora_Fim', 'Status', 
           'SLA_Min', 'Ocorrencia', 'Doca', 'CD']

df = pd.DataFrame(registros, columns=colunas)

nome_arquivo = "LogiAnalytics_Base_WMS_Bruta(1).xlsx"
nome_aba = "WMS_OUTBOUND_BRUTO"

with pd.ExcelWriter(nome_arquivo, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name=nome_aba, index=False)

print(f"Base '{nome_arquivo}' gerada com sucesso! Contagem total de linhas: {len(df)}")

> 6. DEFINIÇÃO DA ARQUITETURA E ESCOPO TÉCNICO

### 6.1. Contexto e Objetivo
Mapear as camadas da solução e definir o papel de cada tecnologia no fluxo end-to-end de dados.

### 6.2. Prompt Estruturado
> **Atue como Consultor Especialista em Engenharia de Dados e Logística.**
> 
> Ajude a estruturar a arquitetura técnica de um projeto de analytics aplicado ao ecossistema WMS de um Centro de Distribuição.
> 
> **1. TECNOLOGIAS E PONTOS DE INTEGRAÇÃO:**
> - 1.1. Python (Google Colab): Geração sintética e estresse de carga da base operacional.
> - 1.2. Excel / Power Query (Linguagem M): Camada de tratamento, limpeza e remoção de duplicadas/nulos.
> - 1.3. VBA (Macros): Automação da consolidação de arquivos e atualização com dois cliques.
> - 1.4. Power BI (Linguagem DAX): Modelagem e criação dos dashboards executivos e operacionais.
> - 1.5. SQL & Databricks (PySpark): Consultas estruturadas e simulação de dados em escala de Big Data na nuvem.
> 
> **2. ENTREGÁVEIS ESPERADOS:**
> - 2.1. Definir o papel de cada ferramenta na jornada do dado.
> - 2.2. Garantir que a arquitetura resolva a falta de visibilidade sobre Lead Time, produtividade por turno e estouro de SLA.

---

> 7. ANÁLISE DE INDICADORES E CAUSA-RAIZ DE ATRASOS

### 7.1. Contexto e Objetivo
Diagnosticar as incoerências operacionais identificadas nos dashboards e isolar os causadores das quebras de SLA.

### 7.2. Prompt Estruturado
> **Atue como Especialista em Gestão de Operações Logísticas e WMS.**
> 
> Analise os resultados consolidados do pipeline de dados para extrair diagnósticos táticos e executivos.
> 
> **1. MÉTRICAS BASE:**
> - 1.1. Volumetria: 3.000 pedidos processados.
> - 1.2. SLA Global: 95,07% (148 pedidos atrasados).
> - 1.3. Lead Time Médio: 11,95 minutos.
> 
> **2. DIRETRIZES DE DIAGNÓSTICO:**
> - 2.1. Isolamento de Ofensores: Analisar a distribuição dos atrasos por Mês, Turno, Área (Picking) e Operador.
> - 2.2. Separação Frequência vs. Impacto: Diferenciar ocorrências com alto volume de repetição daquelas com maior tempo médio de atraso.
> - 2.3. Plano de Ação: Estruturar direcionamentos claros para a supervisão alinhar feedback imediato com os operadores e turnos identificados.

---

> 8. CONSTRUÇÃO DA DOCUMENTAÇÃO TÉCNICA (README.MD)

### 8.1. Contexto e Objetivo
Padronizar a documentação do repositório no GitHub para apresentar o projeto de forma profissional a recrutadores e gestores.

### 8.2. Prompt Estruturado
> **Atue como Technical Writer e Engenheiro de Analytics Sênior.**
> 
> Crie uma documentação completa em Markdown (`README.md`) para o repositório público do GitHub do projeto **WMS Logistics Analytics**.
> 
> **1. ESTRUTURA EXIGIDA:**
> - 1.1. Cabeçalho Executivo: Título, badges técnicas e introdução clara.
> - 1.2. Problema de Negócio: Contextualização do desafio real simulado no Centro de Distribuição.
> - 1.3. Arquitetura de Dados: Fluxo de integração (Colab -> Excel/PQ/VBA -> Power BI -> SQL/Databricks -> IA).
> - 1.4. Estrutura do Repositório: Árvore padronizada de pastas e arquivos.
> - 1.5. Guia de Execução: Instruções passo a passo para o usuário clonar, rodar as macros e atualizar os painéis.

---

> 9. DESENVOLVIMENTO DO PORTFÓLIO WEB (INDEX.HTML & STYLE.CSS)

### 9.1. Contexto e Objetivo
Criar a página web responsiva e executiva para publicação no GitHub Pages.

### 9.2. Prompt Estruturado
> **Atue como Desenvolvedor Front-End Sênior e Especialista em Branding Profissional.**
> 
> Desenvolva o código HTML5 e CSS3 da landing page do portfólio executivo do projeto **WMS Logistics Analytics**.
> 
> **1. REQUISITOS DE DESIGN E CONTEÚDO:**
> - 1.1. Perfil do Autor: Conectar mais de 20 anos de experiência prática em logística, WMS e sustentação de sistemas à formação em Análise e Desenvolvimento de Sistemas.
> - 1.2. Módulos Analíticos: Apresentação das 2 visões gerenciais (Torre de Controle/Mensal) e 2 visões operacionais (Análise Operacional/Pente Fino) com imagens demonstrativas.
> - 1.3. Fluxo Operacional: Explicar o processo simples de atualização em dois cliques (salvar arquivo na pasta, rodar macro no Excel e recarregar o Power BI).
> - 1.4. Design & Usabilidade: Contraste de alta legibilidade (Dark/Light mode por seção), tipografia limpa, botões responsivos com links para as pastas do GitHub e ausência de termos repetitivos.

---

## Observação

Os prompts acima representam a sequência cronológica completa do desenvolvimento do projeto WMS Logistics Analytics, integrando a geração da massa sintética de testes, a modelagem analítica, a auditoria de causa-raiz e a construção das evidências públicas do portfólio.

