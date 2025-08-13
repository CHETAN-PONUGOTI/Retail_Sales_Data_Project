# Retail Sales Analytics (Pure Python Project)

A production-style data analytics project using only Python files (no notebooks). Includes data cleaning, EDA, plots, and a simple sales forecast.

## Structure
```
retail_sales_analytics/      # Python package
  __init__.py
  config.py
  data_prep.py
  eda.py
  modeling.py
  plotting.py
data/
  retail_sales_data.csv
outputs/                     # Generated plots + forecast csv
sql/
  sql_queries.sql
powerbi/
  powerbi_measures_dax.txt
  powerbi_theme.json
  powerbi_report_setup.md
tests/
  test_basic.py
scripts/
  run.sh
requirements.txt
README.md
```

## Quickstart

```bash
# 1) create venv (optional)
python -m venv .venv && . .venv/bin/activate  # (Windows: .venv\Scripts\activate)

# 2) install deps
pip install -r requirements.txt

# 3) run
python -m retail_sales_analytics.cli --data data/retail_sales_data.csv --horizon 3
```

## Outputs
- `outputs/monthly_revenue.png`
- `outputs/revenue_by_category.png`
- `outputs/region_share.png`
- `outputs/discount_vs_revenue.png`
- `outputs/forecast_plot.png`
- `outputs/forecast_next_3_months.csv`
- `outputs/kpis.json`

## SQL + Power BI
- Use `sql/sql_queries.sql` to run aggregations in SQLite or Postgres.
- Power BI assets included for a quick dashboard.
