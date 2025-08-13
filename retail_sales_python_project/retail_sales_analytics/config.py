from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"

# Files
DATA_FILE = DATA_DIR / "retail_sales_data.csv"
FORECAST_CSV = OUTPUTS_DIR / "forecast_next_3_months.csv"

# Plot filenames
PLOT_MONTHLY = OUTPUTS_DIR / "monthly_revenue.png"
PLOT_CATEGORY = OUTPUTS_DIR / "revenue_by_category.png"
PLOT_REGION = OUTPUTS_DIR / "region_share.png"
PLOT_DISCOUNT = OUTPUTS_DIR / "discount_vs_revenue.png"
PLOT_FORECAST = OUTPUTS_DIR / "forecast_plot.png"

KPI_JSON = OUTPUTS_DIR / "kpis.json"
