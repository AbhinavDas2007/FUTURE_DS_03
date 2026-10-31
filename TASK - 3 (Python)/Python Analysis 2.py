import pandas as pd

df = pd.read_csv(r"F:\TASK - 3 (Python)\bank-additional-full.csv",sep=";")

df = df.drop_duplicates()


print("Shape after removing duplicates:", df.shape)
print("\nDuplicate Rows After Cleaning:", df.duplicated().sum())
print("\nTarget Distribution:")
print(df["y"].value_counts())
print("\nTarget Percentage:")
print((df["y"].value_counts(normalize=True) * 100).round(2))
















































