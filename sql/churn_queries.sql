-- Customer Churn Analytics SQL Queries
-- Table name assumed: telco_churn


-- 1. Total customers
SELECT 
    COUNT(*) AS total_customers
FROM telco_churn;


-- 2. Overall churn count
SELECT 
    Churn,
    COUNT(*) AS customer_count
FROM telco_churn
GROUP BY Churn;


-- 3. Overall churn rate
SELECT 
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 
        2
    ) AS churn_rate_percentage
FROM telco_churn;


-- 4. Churn rate by gender
SELECT 
    gender,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate
FROM telco_churn
GROUP BY gender
ORDER BY churn_rate DESC;


-- 5. Churn rate by senior citizen
SELECT 
    SeniorCitizen,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate
FROM telco_churn
GROUP BY SeniorCitizen
ORDER BY churn_rate DESC;


-- 6. Churn rate by contract type
SELECT 
    Contract,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate
FROM telco_churn
GROUP BY Contract
ORDER BY churn_rate DESC;


-- 7. Churn rate by internet service
SELECT 
    InternetService,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate
FROM telco_churn
GROUP BY InternetService
ORDER BY churn_rate DESC;


-- 8. Churn rate by payment method
SELECT 
    PaymentMethod,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate
FROM telco_churn
GROUP BY PaymentMethod
ORDER BY churn_rate DESC;


-- 9. Churn rate by tenure group
SELECT 
    TenureGroup,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate
FROM telco_churn
GROUP BY TenureGroup
ORDER BY churn_rate DESC;


-- 10. Churn rate by monthly charge group
SELECT 
    MonthlyChargeGroup,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate
FROM telco_churn
GROUP BY MonthlyChargeGroup
ORDER BY churn_rate DESC;


-- 11. Average charges by churn status
SELECT 
    Churn,
    ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charges,
    ROUND(AVG(TotalCharges), 2) AS avg_total_charges
FROM telco_churn
GROUP BY Churn;


-- 12. Average tenure by churn status
SELECT 
    Churn,
    ROUND(AVG(tenure), 2) AS avg_tenure
FROM telco_churn
GROUP BY Churn;


-- 13. Monthly revenue lost due to churn
SELECT 
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN MonthlyCharges ELSE 0 END), 2) AS monthly_revenue_lost,
    ROUND(SUM(MonthlyCharges), 2) AS total_monthly_revenue,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN MonthlyCharges ELSE 0 END) * 100.0 / SUM(MonthlyCharges), 2) AS revenue_loss_percentage
FROM telco_churn;


-- 14. Revenue by contract type
SELECT 
    Contract,
    ROUND(SUM(MonthlyCharges), 2) AS total_monthly_revenue,
    ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_revenue
FROM telco_churn
GROUP BY Contract
ORDER BY total_monthly_revenue DESC;


-- 15. Revenue lost by contract type
SELECT 
    Contract,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN MonthlyCharges ELSE 0 END), 2) AS revenue_lost,
    ROUND(SUM(MonthlyCharges), 2) AS total_revenue,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN MonthlyCharges ELSE 0 END) * 100.0 / SUM(MonthlyCharges), 2) AS revenue_loss_percentage
FROM telco_churn
GROUP BY Contract
ORDER BY revenue_lost DESC;


-- 16. High-risk customers
SELECT 
    customerID,
    Contract,
    tenure,
    MonthlyCharges,
    TotalCharges,
    InternetService,
    PaymentMethod,
    Churn
FROM telco_churn
WHERE Contract = 'Month-to-month'
  AND MonthlyCharges > 70
  AND tenure < 12
ORDER BY MonthlyCharges DESC;


-- 17. Top 20 highest revenue customers
SELECT 
    customerID,
    tenure,
    MonthlyCharges,
    TotalCharges,
    Contract,
    InternetService,
    Churn
FROM telco_churn
ORDER BY TotalCharges DESC
LIMIT 20;


-- 18. Customers with low tenure and high monthly charges
SELECT 
    customerID,
    tenure,
    MonthlyCharges,
    Contract,
    InternetService,
    PaymentMethod,
    Churn
FROM telco_churn
WHERE tenure <= 12
  AND MonthlyCharges >= 80
ORDER BY MonthlyCharges DESC;


-- 19. Churn by paperless billing
SELECT 
    PaperlessBilling,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate
FROM telco_churn
GROUP BY PaperlessBilling
ORDER BY churn_rate DESC;


-- 20. Churn by tech support
SELECT 
    TechSupport,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate
FROM telco_churn
GROUP BY TechSupport
ORDER BY churn_rate DESC;


-- 21. Churn by online security
SELECT 
    OnlineSecurity,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate
FROM telco_churn
GROUP BY OnlineSecurity
ORDER BY churn_rate DESC;


-- 22. Churn by multiple lines
SELECT 
    MultipleLines,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate
FROM telco_churn
GROUP BY MultipleLines
ORDER BY churn_rate DESC;


-- 23. Customer distribution by revenue segment
SELECT 
    RevenueSegment,
    COUNT(*) AS total_customers,
    ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charges,
    ROUND(AVG(TotalCharges), 2) AS avg_total_charges
FROM telco_churn
GROUP BY RevenueSegment
ORDER BY total_customers DESC;


-- 24. Churn by dependents
SELECT 
    Dependents,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate
FROM telco_churn
GROUP BY Dependents
ORDER BY churn_rate DESC;


-- 25. Churn by partner status
SELECT 
    Partner,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate
FROM telco_churn
GROUP BY Partner
ORDER BY churn_rate DESC;


-- 26. Average customer lifetime value by churn
SELECT 
    Churn,
    ROUND(AVG(TotalCharges), 2) AS avg_customer_lifetime_value,
    ROUND(SUM(TotalCharges), 2) AS total_customer_lifetime_value
FROM telco_churn
GROUP BY Churn;


-- 27. Churn risk segment summary
SELECT 
    ContractRisk,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate,
    ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charges
FROM telco_churn
GROUP BY ContractRisk
ORDER BY churn_rate DESC;


-- 28. Internet service and contract combined churn analysis
SELECT 
    InternetService,
    Contract,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate
FROM telco_churn
GROUP BY InternetService, Contract
ORDER BY churn_rate DESC;


-- 29. Payment method and contract combined churn analysis
SELECT 
    PaymentMethod,
    Contract,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate
FROM telco_churn
GROUP BY PaymentMethod, Contract
ORDER BY churn_rate DESC;


-- 30. Final retention target list
SELECT 
    customerID,
    Contract,
    tenure,
    MonthlyCharges,
    TotalCharges,
    InternetService,
    PaymentMethod,
    TechSupport,
    OnlineSecurity,
    Churn
FROM telco_churn
WHERE Churn = 'No'
  AND Contract = 'Month-to-month'
  AND MonthlyCharges >= 70
  AND tenure <= 18
ORDER BY MonthlyCharges DESC;