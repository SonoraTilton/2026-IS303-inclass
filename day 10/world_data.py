import pandas as pd
df = pd.read_csv("day 9/world_development_data.csv")
df["region"] = df["region"].str.title().str.strip()
df["gdp_per_capita"] = pd.to_numeric(
    df["gdp_per_capita"].astype(str).str.replace(",", ""), errors="coerce"
)
"""
print(df.groupby("region")["life_expectancy"].mean())

print(df.groupby("region")["literacy_rate"].mean())
print(df.groupby("region")["literacy_rate"].mean().idxmin())

print(df.groupby("region")["population_thousands"].sum().sort_values(ascending=False))

print(df.groupby("region")["country"].count())

print(df.groupby("region")["life_expectancy"].max())
print(df.loc[df["life_expectancy"].idxmax()])


gtr_70 = df[df["life_expectancy"] > 70]
ls_60 = df[df["life_expectancy"] < 60]
print(gtr_70["gdp_per_capita"].mean())
print(ls_60["gdp_per_capita"].mean())

df["total_gdp"] = (df["gdp_per_capita"] *  df["population_thousands"])
print(df.groupby("region")["total_gdp"].sum().max())
print(df.groupby("region")["total_gdp"].sum().idxmax())

"""
import matplotlib.pyplot as plt

plt.scatter(df["gdp_per_capita"], df["infant_mortality"], color="pink")
plt.title("Infant Mortality vs GDP per Capita")
plt.xlabel("GDP per Capita")
plt.ylabel("Infant Mortality")
plt.tight_layout()
plt.savefig("chart.png")
plt.show()