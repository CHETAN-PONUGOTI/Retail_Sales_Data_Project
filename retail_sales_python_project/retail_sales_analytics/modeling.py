import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, r2_score
from .plotting import save_line
from .config import PLOT_FORECAST, FORECAST_CSV

def prepare_monthly(df):
    monthly = df.groupby("YearMonth")["TotalRevenue"].sum().reset_index().sort_values("YearMonth")
    monthly["t"] = np.arange(len(monthly))
    monthly["month"] = monthly["YearMonth"].dt.month
    monthly["sin12"] = np.sin(2 * np.pi * monthly["t"] / 12)
    monthly["cos12"] = np.cos(2 * np.pi * monthly["t"] / 12)
    return monthly

def train_and_forecast(monthly, horizon=3, alpha=1.0):
    # Features and target
    X = monthly[["t","month","sin12","cos12"]]
    y = monthly["TotalRevenue"].values

    # Simple train/test split (last 4 months for test if possible)
    split = len(monthly) - 4 if len(monthly) > 8 else int(len(monthly) * 0.8)
    X_train, X_test = X.iloc[:split], X.iloc[split:]
    y_train, y_test = y[:split], y[split:]

    model = Ridge(alpha=alpha)
    model.fit(X_train, y_train)

    mae = None
    r2 = None
    if len(y_test) > 0:
        preds = model.predict(X_test)
        mae = mean_absolute_error(y_test, preds)
        r2 = r2_score(y_test, preds)

    # Build future design matrix
    last_t = int(monthly["t"].iloc[-1])
    last_month_ts = pd.Timestamp(monthly["YearMonth"].iloc[-1])

    future_rows = []
    for i in range(1, horizon + 1):
        ym = (last_month_ts + pd.DateOffset(months=i)).to_period('M').to_timestamp()
        t = last_t + i
        m = ym.month
        sin12 = np.sin(2 * np.pi * t / 12)
        cos12 = np.cos(2 * np.pi * t / 12)
        future_rows.append({"YearMonth": ym, "t": t, "month": m, "sin12": sin12, "cos12": cos12})

    future_df = pd.DataFrame(future_rows)
    future_pred = model.predict(future_df[["t","month","sin12","cos12"]])

    # Save forecast CSV
    out = future_df[["YearMonth"]].copy()
    out["ForecastedRevenue"] = future_pred
    out.to_csv(FORECAST_CSV, index=False)

    # Plot combined series: show historical then forecast extension
    combined_x = pd.concat([monthly["YearMonth"], out["YearMonth"]])
    combined_y = pd.concat([monthly["TotalRevenue"], out["ForecastedRevenue"]])
    save_line(combined_x, combined_y, "Monthly Revenue: Actual (historical) + Forecast (next 3 months)", "Month", "Revenue", PLOT_FORECAST)

    return {"mae": mae, "r2": r2, "forecast": out}
