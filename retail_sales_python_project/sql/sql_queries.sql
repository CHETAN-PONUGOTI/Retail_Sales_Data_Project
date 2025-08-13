
-- Create table
CREATE TABLE sales (
    OrderID INTEGER PRIMARY KEY,
    OrderDate DATE NOT NULL,
    ProductCategory TEXT,
    ProductName TEXT,
    Region TEXT,
    UnitsSold INTEGER,
    UnitPrice REAL,
    Discount REAL,
    TotalRevenue REAL
);

-- Basic indexes
CREATE INDEX idx_sales_orderdate ON sales(OrderDate);
CREATE INDEX idx_sales_region ON sales(Region);
CREATE INDEX idx_sales_category ON sales(ProductCategory);

-- Load CSV (SQLite CLI example)
-- .mode csv
-- .import retail_sales_data.csv sales

-- KPIs
SELECT SUM(TotalRevenue) AS TotalRevenue FROM sales;

-- Revenue by region
SELECT Region, SUM(TotalRevenue) AS Revenue
FROM sales
GROUP BY Region
ORDER BY Revenue DESC;

-- Revenue by category
SELECT ProductCategory, SUM(TotalRevenue) AS Revenue
FROM sales
GROUP BY ProductCategory
ORDER BY Revenue DESC;

-- Monthly revenue
SELECT strftime('%Y-%m', OrderDate) AS YearMonth, SUM(TotalRevenue) AS Revenue
FROM sales
GROUP BY YearMonth
ORDER BY YearMonth;

-- Average order value (approx: per OrderID)
SELECT AVG(RevenuePerOrder) AS AOV FROM (
  SELECT OrderID, SUM(TotalRevenue) AS RevenuePerOrder
  FROM sales
  GROUP BY OrderID
);

-- Top 10 products by revenue
SELECT ProductName, SUM(TotalRevenue) AS Revenue
FROM sales
GROUP BY ProductName
ORDER BY Revenue DESC
LIMIT 10;
