import argparse
import json
from .config import DATA_FILE, OUTPUTS_DIR, KPI_JSON
from . import data_prep, eda, modeling
from .modeling import prepare_monthly

def main():
    parser = argparse.ArgumentParser(description="Retail Sales Analytics (pure Python)")
    parser.add_argument("--data", type=str, default=str(DATA_FILE), help="Path to CSV data file")
    parser.add_argument("--horizon", type=int, default=3, help="Forecast horizon in months")
    args, _ = parser.parse_known_args()

    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)

    df = data_prep.load_data(args.data)
    df = data_prep.clean_and_engineer(df)

    # EDA
    eda_results = eda.run_eda(df)
    with open(KPI_JSON, "r", encoding="utf-8") as f:
        kpis = json.load(f)
    print("KPIs:")
    for k,v in kpis.items():
        print(f"  {k}: {v:,.2f}" if isinstance(v, (int,float)) else f"  {k}: {v}")

    # Modeling
    monthly = prepare_monthly(df)
    model_results = modeling.train_and_forecast(monthly, horizon=args.horizon, alpha=1.0)
    if model_results["mae"] is not None:
        print(f"Forecast MAE: {model_results['mae']:,.2f}")
        print(f"Forecast R^2: {model_results['r2']:.3f}")
    print("Forecast saved to:", str(modeling.FORECAST_CSV))

if __name__ == "__main__":
    main()
