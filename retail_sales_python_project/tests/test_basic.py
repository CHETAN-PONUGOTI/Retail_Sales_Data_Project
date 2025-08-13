from retail_sales_analytics.data_prep import load_data, clean_and_engineer
from retail_sales_analytics.config import DATA_FILE

def test_load_and_clean():
    df = load_data(DATA_FILE)
    df = clean_and_engineer(df)
    assert not df.empty
    assert "YearMonth" in df.columns
