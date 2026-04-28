import pandas as pd

print("🚀 Pipeline started")

# Step 1: Read data
df = pd.read_csv("data/sales.csv")

# 👇 ADD THESE 2 LINES HERE
print("Columns:", df.columns)
print(df.head())

# (keep this also if you added earlier)
df.columns = df.columns.str.strip()

# Stop here temporarily (for debugging)