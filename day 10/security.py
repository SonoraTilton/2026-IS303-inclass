import pandas as pd
df = pd.read_csv("day 10/security_log.csv")

failures = df[df["status"] == "failed"]
print(len(failures))
print(f"{failures["attempts"].sum()/df["attempts"]*100}%")

print(df.groupby("username")["attempts"].sum().idxmax())
print(df.groupby("username")["attempts"].sum().max())

print(failures.groupby("ip_address")["attempts"].sum().idxmax())
record = failures[failures.groupby("ip_address")["attempts"].sum().idxmax()]
#ask claude on previous line
