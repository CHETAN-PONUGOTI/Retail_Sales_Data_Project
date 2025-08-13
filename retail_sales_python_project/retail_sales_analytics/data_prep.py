import pandas as pd

def load_data(path):
    df = pd.read_csv(path, parse_dates=["OrderDate"])
    return df

def clean_and_engineer(df):
    df = df.drop_duplicates(subset=["OrderID"]).copy()
    df["ProductCategory"] = df["ProductCategory"].astype("category")
    df["ProductName"] = df["ProductName"].astype("category")
    df["Region"] = df["Region"].astype("category")
    df["Year"] = df["OrderDate"].dt.year
    df["Month"] = df["OrderDate"].dt.month
    df["YearMonth"] = df["OrderDate"].values.astype("datetime64[M]")
    # Sanity checks
    assert (df["UnitsSold"] >= 1).all()
    assert (df["UnitPrice"] > 0).all()
    assert (df["Discount"].between(0,1)).all()
    # Recompute revenue for consistency
    df["RevenueCheck"] = (df["UnitsSold"] * df["UnitPrice"] * (1 - df["Discount"])).round(2)
    return df
