# ============================================================
#  DAY 98 — Portfolio Project
#  PROJECT: Space Race Data Analysis
# ============================================================
#
#  SKILLS USED: pandas, matplotlib, plotly, groupby, time series
#
#  QUESTIONS TO ANSWER:
#    1. How many launches per year? (line chart)
#    2. Which country launched the most rockets? (bar chart)
#    3. What % of launches were successful over time?
#    4. Mission failure rates by country
#    5. Cold War era vs post-Cold War launches
#
#  Dataset: "mission_launches.csv" from Maven Analytics / Kaggle
#  (search "space missions" on Kaggle — it's free)
#  For now, use the sample data below.
#
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Sample data (download the real 4,324-row dataset from Kaggle)
data = {
    "Company":  ["NASA", "NASA", "Roscosmos", "SpaceX", "SpaceX", "NASA", "JAXA", "ESA"],
    "Location": ["USA", "USA", "Russia", "USA", "USA", "USA", "Japan", "France"],
    "Date":     ["1969-07-16", "1972-12-07", "1975-05-24", "2015-12-21",
                 "2020-05-30", "2023-05-05", "2023-07-01", "2023-10-13"],
    "Mission":  ["Apollo 11", "Apollo 17", "Soyuz 18", "OG2 Mission", "Crew Dragon", "Artemis", "H-IIB", "Vega"],
    "Status":   ["Success", "Success", "Success", "Success", "Success", "Success", "Failure", "Success"],
    "Cost_$M":  [355, 450, None, 60, 200, 4100, 90, 80],
}
df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])
df["Year"] = df["Date"].dt.year


# --------------------------------------------------
#  TODO 1: Launches per year (line chart)
# --------------------------------------------------
launches_per_year = df.groupby("Year").size()
# plt.plot(launches_per_year.index, launches_per_year.values)
# plt.title("Space Launches Per Year")


# --------------------------------------------------
#  TODO 2: Launches by country (bar chart)
# --------------------------------------------------
by_country = df["Location"].value_counts()
# plt.bar(by_country.index, by_country.values)


# --------------------------------------------------
#  TODO 3: Success rate over time
# --------------------------------------------------
df["Success"] = (df["Status"] == "Success").astype(int)
# success_by_year = df.groupby("Year")["Success"].mean() * 100
# plot as line chart


# --------------------------------------------------
#  TODO 4: Choropleth map — launches by country
# --------------------------------------------------
# fig = px.choropleth(
#     df.groupby("Location").size().reset_index(name="count"),
#     locations="Location", locationmode="country names",
#     color="count", title="Space Launches by Country"
# )
# fig.show()

print(df.describe())
print("\nLaunches by country:\n", by_country)
