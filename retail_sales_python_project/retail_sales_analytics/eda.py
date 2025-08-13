import matplotlib.pyplot as plt

def run_eda(df):
    print("\nGenerating EDA Reports...")

    # Revenue by Region
    rev_by_region = df.groupby("Region")["TotalRevenue"].sum().sort_values(ascending=False)
    rev_by_region.plot(kind="bar", title="Revenue by Region")
    plt.ylabel("Total Revenue")
    plt.tight_layout()
    plt.show()  # <-- Shows chart in window

    # Revenue by Category
    rev_by_cat = df.groupby("ProductCategory")["TotalRevenue"].sum().sort_values(ascending=False)
    rev_by_cat.plot(kind="bar", title="Revenue by Product Category", color="orange")
    plt.ylabel("Total Revenue")
    plt.tight_layout()
    plt.show()