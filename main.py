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
