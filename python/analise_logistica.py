import pandas as pd

# Arquivo Excel tratado pelo Power Query
arquivo = "../Excel/vba/LogiAnalytics_Base_WMS_Dados tratados .xlsx"

# Leitura da base
df = pd.read_excel(arquivo)

# Indicadores principais
total_pedidos = df["Pedido"].nunique()
pedidos_atrasados = (df["Status_Calculado"] == "Atrasado").sum()

sla = ((total_pedidos - pedidos_atrasados) / total_pedidos) * 100

tempo_medio = df["Tempo_Processamento_Min"].mean()

print("=== WMS LOGISTICS ANALYTICS ===")
print(f"Total de pedidos: {total_pedidos}")
print(f"Pedidos atrasados: {pedidos_atrasados}")
print(f"SLA: {sla:.2f}%")
print(f"Tempo médio de processamento: {tempo_medio:.2f} minutos")

# Análise mensal
analise_mensal = (
    df.groupby("Nome do Mês")
    .agg(
        Pedidos=("Pedido", "nunique"),
        Tempo_Medio=("Tempo_Processamento_Min", "mean")
    )
    .reset_index()
)

print("\n=== ANÁLISE MENSAL ===")
print(analise_mensal)

# Análise por turno e área
analise_turno_area = (
    df.groupby(["Turno", "Area"])
    .agg(
        Pedidos=("Pedido", "nunique"),
        Tempo_Medio=("Tempo_Processamento_Min", "mean")
    )
    .reset_index()
)

print("\n=== TURNO x ÁREA ===")
print(analise_turno_area)

# Principais ocorrências
analise_ocorrencias = (
    df.groupby("Ocorrencia")
    .agg(
        Pedidos=("Pedido", "nunique"),
        Tempo_Medio=("Tempo_Processamento_Min", "mean")
    )
    .sort_values("Pedidos", ascending=False)
    .reset_index()
)

print("\n=== OCORRÊNCIAS ===")
print(analise_ocorrencias)