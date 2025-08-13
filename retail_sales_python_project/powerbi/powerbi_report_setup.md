
# Power BI Setup Guide

1) Open Power BI Desktop
2) Get Data -> Text/CSV -> select `retail_sales_data.csv`
3) In Model view:
   - Ensure `OrderDate` is Date type.
   - Create a Date table:
     Date = CALENDAR(MIN(sales[OrderDate]), MAX(sales[OrderDate]))
     Add columns: Year, Month, YearMonth = FORMAT([Date], "YYYY-MM")
   - Create relationship Date[Date] -> sales[OrderDate]
4) Add Measures (copy from powerbi_measures_dax.txt)
5) Import theme: View -> Browse for themes -> select `powerbi_theme.json`
6) Build pages:
   - Overview: Cards (Total Revenue, Orders, AOV), Line chart (Monthly Revenue), Pie (Region share)
   - Category Deep Dive: Bar chart (Revenue by Category), Table (Top Products), Slicer (Date, Region, Category)
   - Forecast Page: Use Notebook's exported `forecast_next_3_months.csv` as an additional table or plot actual vs forecast.
