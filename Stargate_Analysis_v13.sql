/* * Stargate Cluster v13.1 | Senior Architect: LauroBeckDBA 
 * Project: Bloomberg Intelligence - Institutional Liquidity Mapping
 * Event: April 8th Hormuz Truce Inflection
 */

USE BloombergGlobal;
GO

WITH EarningsMap AS (
    SELECT 
        Symbol, 
        Price, 
        CAST(Volume AS BIGINT) AS Vol_Big, 
        CAST(Price * CAST(Volume AS BIGINT) AS DECIMAL(25,2)) AS Notional_USD,
        CASE 
            WHEN Symbol = 'JPM' THEN '2026-04-14'
            WHEN Symbol = 'BNY' THEN '2026-04-16'
            ELSE NULL 
        END AS Q1_Earnings_Date
    FROM MarketData.Ticks
    WHERE TradeTime >= CAST(GETDATE() AS DATE)
)
SELECT 
    Symbol, 
    Q1_Earnings_Date, 
    DATEDIFF(day, CAST(GETDATE() AS DATE), Q1_Earnings_Date) AS Days_Remaining,
    SUM(Vol_Big) AS Daily_Volume,
    SUM(Notional_USD) AS Total_Notional_Sales,
    CAST(AVG(Price) AS DECIMAL(18,2)) AS VWAP_Estimate
FROM EarningsMap
GROUP BY Symbol, Q1_Earnings_Date
ORDER BY Total_Notional_Sales DESC;
GO
