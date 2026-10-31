import pandas as pd

df = pd.read_csv(r"F:\TASK - 3 (Python)\bank-additional-full.csv",sep=";")

total_contacts = len(df)
successful = (df["y"] == "yes").sum()
unsuccessful = (df["y"] == "no").sum()
conversion_rate = successful / total_contacts * 100

print("\nMarketing Campaign KPIs")
print("Total Contacts:", total_contacts)
print("Successful Subscriptions:", successful)
print("Unsuccessful Contacts:", unsuccessful)
print("Conversion Rate:", round(conversion_rate, 2), "%")











