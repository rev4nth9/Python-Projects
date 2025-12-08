# test_pandas.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a simple dataset
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [25000, 27000, 30000, 28000, 32000, 35000],
    "Expenses": [15000, 16000, 17000, 18000, 19000, 21000]
}

df = pd.DataFrame(data)

# Add a new column 'Profit'
df["Profit"] = df["Sales"] - df["Expenses"]

print("=== Company Financial Data ===")
print(df)
print("\nAverage Profit:", round(df["Profit"].mean(), 2))

# Plot sales vs expenses
plt.figure(figsize=(8, 4))
plt.plot(df["Month"], df["Sales"], marker='o', label="Sales")
plt.plot(df["Month"], df["Expenses"], marker='o', label="Expenses")
plt.plot(df["Month"], df["Profit"], marker='o', label="Profit")
plt.title("Monthly Company Performance")
plt.xlabel("Month")
plt.ylabel("Amount (₹)")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()
