import pandas as pd

# Загрузка данных
df = pd.read_csv("data/sales.csv")

print("Initial data preview:")
print(df.head())

print("\nDataset info:")
print(df.info())

# Очистка данных
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["price"] = df["price"].fillna(df["price"].median())
df["quantity"] = df["quantity"].fillna(1)
df["city"] = df["city"].fillna("Unknown")
df = df.drop_duplicates()

df["revenue"] = df["price"] * df["quantity"]

# Основной анализ
total_revenue = df["revenue"].sum()

revenue_by_category = (
    df.groupby("category")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

top_products = (
    df.groupby("product")["quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTotal revenue:", total_revenue)
print("\nRevenue by category:")
print(revenue_by_category)
print("\nTop products by quantity sold:")
print(top_products)
