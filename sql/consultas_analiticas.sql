-- WMS Logistics Analytics
-- Consultas analíticas utilizadas no projeto

-- =========================================================
-- 1. Indicadores principais
-- =========================================================

SELECT
    COUNT(*) AS total_registros,
    COUNT(DISTINCT Pedido) AS total_pedidos,
    SUM(CASE WHEN Status_Calculado = 'Atrasado' THEN 1 ELSE 0 END) AS pedidos_atrasados,
    ROUND(
        (
            COUNT(DISTINCT Pedido)
            - SUM(CASE WHEN Status_Calculado = 'Atrasado' THEN 1 ELSE 0 END)
        ) * 100.0 / COUNT(DISTINCT Pedido),
        2
    ) AS sla_percentual,
    ROUND(AVG(Tempo_Processamento_Min), 2) AS tempo_medio_processamento
FROM wms_pedidos;


-- =========================================================
-- 2. Análise mensal
-- =========================================================

SELECT
    `Nome do Mês` AS mes,
    COUNT(DISTINCT Pedido) AS pedidos,
    SUM(CASE WHEN Status_Calculado = 'Atrasado' THEN 1 ELSE 0 END) AS pedidos_atrasados,
    ROUND(
        (
            COUNT(DISTINCT Pedido)
            - SUM(CASE WHEN Status_Calculado = 'Atrasado' THEN 1 ELSE 0 END)
        ) * 100.0 / COUNT(DISTINCT Pedido),
        2
    ) AS sla_percentual,
    ROUND(AVG(Tempo_Processamento_Min), 2) AS tempo_medio
FROM wms_pedidos
GROUP BY `Nome do Mês`
ORDER BY pedidos DESC;


-- =========================================================
-- 3. Análise por turno e área
-- =========================================================

SELECT
    Turno,
    Area,
    COUNT(DISTINCT Pedido) AS pedidos,
    SUM(CASE WHEN Status_Calculado = 'Atrasado' THEN 1 ELSE 0 END) AS pedidos_atrasados,
    ROUND(
        (
            COUNT(DISTINCT Pedido)
            - SUM(CASE WHEN Status_Calculado = 'Atrasado' THEN 1 ELSE 0 END)
        ) * 100.0 / COUNT(DISTINCT Pedido),
        2
    ) AS sla_percentual,
    ROUND(AVG(Tempo_Processamento_Min), 2) AS tempo_medio
FROM wms_pedidos
GROUP BY Turno, Area
ORDER BY pedidos_atrasados DESC;


-- =========================================================
-- 4. Principais ocorrências
-- =========================================================

SELECT
    Ocorrencia,
    COUNT(DISTINCT Pedido) AS pedidos,
    SUM(CASE WHEN Status_Calculado = 'Atrasado' THEN 1 ELSE 0 END) AS pedidos_atrasados,
    ROUND(AVG(Tempo_Processamento_Min), 2) AS tempo_medio
FROM wms_pedidos
GROUP BY Ocorrencia
ORDER BY pedidos_atrasados DESC;


-- =========================================================
-- 5. Atrasos por operador
-- =========================================================

SELECT
    Operador,
    COUNT(DISTINCT Pedido) AS pedidos,
    SUM(CASE WHEN Status_Calculado = 'Atrasado' THEN 1 ELSE 0 END) AS pedidos_atrasados,
    ROUND(
        (
            COUNT(DISTINCT Pedido)
            - SUM(CASE WHEN Status_Calculado = 'Atrasado' THEN 1 ELSE 0 END)
        ) * 100.0 / COUNT(DISTINCT Pedido),
        2
    ) AS sla_percentual
FROM wms_pedidos
GROUP BY Operador
ORDER BY pedidos_atrasados DESC;