-- ===========================================
-- Consulta 1: Total de vendas por produto
-- ===========================================

SELECT 
    Produto,
    Categoria,
    SUM(Quantidade * Preco) AS Total_Vendas
FROM vendas
GROUP BY Produto, Categoria
ORDER BY Total_Vendas DESC;

-- Explicação:
-- A consulta agrupa os registros por produto e categoria,
-- calcula o total de vendas multiplicando quantidade por preço,
-- e ordena os resultados do maior para o menor valor de vendas.


-- ===========================================
-- Consulta 2: Produto com menor venda em junho de 2023
-- ===========================================

SELECT 
    Produto,
    SUM(Quantidade) AS Total_Quantidade
FROM vendas
WHERE strftime('%m', Data) = '06'
  AND strftime('%Y', Data) = '2023'
GROUP BY Produto
ORDER BY Total_Quantidade ASC
LIMIT 1;

-- Explicação:
-- A consulta filtra apenas registros de junho de 2023,
-- soma a quantidade vendida por produto
-- e retorna aquele com menor volume de vendas.