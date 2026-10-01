# ============================================================
# WMS LOGISTICS ANALYTICS
# Databricks | Python | PySpark | SQL
# ============================================================

import pandas as pd
from pyspark.sql import functions as F

# ------------------------------------------------------------
# 1. CARREGAMENTO DA BASE
# ------------------------------------------------------------

arquivo = "/Volumes/workspace/default/wms_data/LogiAnalytics_Base_WMS_Dados tratados .xlsx"

df = pd.read_excel(arquivo)

print("Base carregada")
print(f"Registros: {len(df):,}")
print(f"Colunas: {len(df.columns)}")


# ------------------------------------------------------------
# 2. CONVERSÃO PARA SPARK
# ------------------------------------------------------------

df_spark = spark.createDataFrame(df)

print(f"Registros Spark: {df_spark.count():,}")

df_spark.write.mode("overwrite").saveAsTable("wms_pedidos")

print("Tabela wms_pedidos criada.")


# ------------------------------------------------------------
# 3. KPIs EXECUTIVOS
# ------------------------------------------------------------

total_pedidos = df["Pedido"].nunique()

pedidos_atrasados = (
    df["Status_Calculado"] == "Atrasado"
).sum()

sla = (
    (total_pedidos - pedidos_atrasados)
    / total_pedidos
    * 100
)

tempo_medio = df["Tempo_Processamento_Min"].mean()

print("\n--- KPIs EXECUTIVOS ---")
print(f"Total de pedidos: {total_pedidos:,}")
print(f"Pedidos atrasados: {pedidos_atrasados:,}")
print(f"SLA: {sla:.2f}%")
print(f"Tempo médio: {tempo_medio:.2f} min")


# ------------------------------------------------------------
# 4. ANÁLISE MENSAL
# ------------------------------------------------------------

analise_mensal = (
    df.groupby("Nome do Mês")
      .agg(
          Total_Pedidos=("Pedido", "nunique"),
          Pedidos_Atrasados=(
              "Status_Calculado",
              lambda x: (x == "Atrasado").sum()
          ),
          Tempo_Medio_Min=(
              "Tempo_Processamento_Min",
              "mean"
          )
      )
      .reset_index()
)

analise_mensal["SLA_Percentual"] = (
    (
        analise_mensal["Total_Pedidos"]
        - analise_mensal["Pedidos_Atrasados"]
    )
    / analise_mensal["Total_Pedidos"]
    * 100
).round(2)

analise_mensal["Tempo_Medio_Min"] = (
    analise_mensal["Tempo_Medio_Min"].round(2)
)

print("\n--- ANÁLISE MENSAL ---")
display(analise_mensal)


# ------------------------------------------------------------
# 5. ANÁLISE POR TURNO E ÁREA
# ------------------------------------------------------------

analise_turno_area = (
    df.groupby(["Turno", "Area"])
      .agg(
          Total_Pedidos=("Pedido", "nunique"),
          Pedidos_Atrasados=(
              "Status_Calculado",
              lambda x: (x == "Atrasado").sum()
          ),
          Tempo_Medio_Min=(
              "Tempo_Processamento_Min",
              "mean"
          )
      )
      .reset_index()
)

analise_turno_area["SLA_Percentual"] = (
    (
        analise_turno_area["Total_Pedidos"]
        - analise_turno_area["Pedidos_Atrasados"]
    )
    / analise_turno_area["Total_Pedidos"]
    * 100
).round(2)

analise_turno_area["Tempo_Medio_Min"] = (
    analise_turno_area["Tempo_Medio_Min"].round(2)
)

analise_turno_area = analise_turno_area.sort_values(
    "Pedidos_Atrasados",
    ascending=False
)

print("\n--- TURNO X ÁREA ---")
display(analise_turno_area)


# ------------------------------------------------------------
# 6. ANÁLISE DAS OCORRÊNCIAS
# ------------------------------------------------------------

atrasos = df[
    df["Status_Calculado"] == "Atrasado"
].copy()

analise_ocorrencia = (
    atrasos.groupby("Ocorrencia")
    .agg(
        Pedidos_Atrasados=("Pedido", "nunique"),
        Tempo_Medio_Min=(
            "Tempo_Processamento_Min",
            "mean"
        )
    )
    .reset_index()
)

analise_ocorrencia["Participacao_%"] = (
    analise_ocorrencia["Pedidos_Atrasados"]
    / analise_ocorrencia["Pedidos_Atrasados"].sum()
    * 100
).round(2)

analise_ocorrencia["Tempo_Medio_Min"] = (
    analise_ocorrencia["Tempo_Medio_Min"].round(2)
)

analise_ocorrencia = analise_ocorrencia.sort_values(
    "Pedidos_Atrasados",
    ascending=False
)

print("\n--- OCORRÊNCIAS DOS ATRASOS ---")
display(analise_ocorrencia)


# ------------------------------------------------------------
# 7. RESUMO EXECUTIVO
# ------------------------------------------------------------

resumo = pd.DataFrame({
    "Indicador": [
        "Total de Pedidos",
        "Pedidos Atrasados",
        "SLA (%)",
        "Tempo Médio de Processamento (min)"
    ],
    "Valor": [
        total_pedidos,
        pedidos_atrasados,
        round(sla, 2),
        round(tempo_medio, 2)
    ]
})

print("\n--- RESUMO EXECUTIVO ---")
display(resumo)


# ------------------------------------------------------------
# 8. SALVAR RESUMO NO DATABRICKS
# ------------------------------------------------------------

spark_resumo = spark.createDataFrame(resumo)

spark_resumo.write.mode(
    "overwrite"
).saveAsTable(
    "wms_resumo_executivo"
)

print("\nTabela wms_resumo_executivo criada com sucesso.")