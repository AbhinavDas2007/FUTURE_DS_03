import pandas as pd

df = pd.read_csv(r"F:\TASK - 3 (Python)\bank-additional-full.csv", sep=";")

df = df.drop_duplicates()

total_contacts = len(df)
successful = (df["y"] == "yes").sum()
unsuccessful = (df["y"] == "no").sum()
conversion_rate = successful / total_contacts * 100

print("Total Contacts:", total_contacts)
print("Successful Subscriptions:", successful)
print("Unsuccessful Contacts:", unsuccessful)
print("Conversion Rate:", round(conversion_rate, 2), "%")

df.to_csv("bank_marketing_cleaned.csv", index=False)

print("\nCleaned dataset exported successfully!")










