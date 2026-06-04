import pandas as pd
df = pd.read_csv("day 9/world_development_data.csv")
print(df.head())
print(df.describe())
print(df.shape) #attributes like shape don't need the parentheses, methods do)
print(df.info())

#countries where > 20% lack clean water
water_crisis = df[df["clean_water_pct"] < 80]
print(water_crisis[["country", "clean_water_pct"]])

#life expectancy < 60
life_expectancy = df[df["life_expectancy"] < 60]
print(life_expectancy[["country", "life_expectancy"]])
print(len(life_expectancy))

#highest life expectancy
highest = df.loc[df["life_expectancy"].idxmax()]
print(highest[["country", "life_expectancy"]])

#unique regions
df["region"] = df["region"].str.title().str.strip()
regions = df["region"].unique()
print(regions)

#null values
print(df.isnull().sum())

ssa = df[df["region"] == "Sub-Saharan Africa"]
print(ssa[["country", "region"]])

df["clean_water_pct"] = df["clean_water_pct"].fillna(0)
print(df[["clean_water_pct"]])
assert df["clean_water_pct"].notna().all(), "Missing clean water data!"

