import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

# Статистический анализ с помощью NumPy
mean_price = np.mean(df["price"])
median_price = np.median(df["price"])
std_price = np.std(df["price"])

print("\nPrice statistics:")
print("Mean price:", mean_price)
print("Median price:", median_price)
print("Standard deviation:", std_price)

# Визуализация
plt.figure()
revenue_by_category.plot(kind="bar", title="Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("plots/revenue_by_category.png")
plt.close()

plt.figure()
top_products.head(5).plot(kind="bar", title="Top 5 Products by Quantity Sold")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.tight_layout()
plt.savefig("plots/top_5_products.png")
plt.close()

print("\nTwo plots saved to plots/")

# Сохранение очищенных данных
df.to_csv("data/cleaned_sales.csv", index=False)
print("\nCleaned data saved to data/cleaned_sales.csv")
