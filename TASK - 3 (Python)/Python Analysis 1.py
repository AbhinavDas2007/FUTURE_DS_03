import pandas as pd
df = pd.read_csv(r"F:\TASK - 3 (Python)\bank-additional-full.csv",sep=";")

print("Dataset Shape:", df.shape)
print("\nFirst 5 Rows:")
print(df.head())
print("\nColumn Names:")
print(df.columns.tolist())
print("\nMissing Values:")
print(df.isnull().sum())
print("\nDuplicate Rows:", df.duplicated().sum())




