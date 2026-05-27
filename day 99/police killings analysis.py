# ============================================================
#  DAY 99: Portfolio Project
#  PROJECT: Data Analysis: Fatal Police Encounters in the US
# ============================================================
#
#  SKILLS USED: pandas, seaborn, plotly, statistical analysis
#
#  This dataset covers a sensitive, real-world topic.
#  Approach the analysis with care and present findings factually.
#
#  Dataset: FatalEncounters.org / The Guardian "The Counted"
#  For practice, use the sample below or download from Kaggle.
#
#  QUESTIONS TO ANSWER:
#    1. How many incidents per year?
#    2. Breakdown by race (adjusted for population share)?
#    3. By state: choropleth map
#    4. By age distribution
#    5. Trend over time: is it increasing or decreasing?
#
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = {
    "Year":  [2015, 2015, 2016, 2016, 2017, 2017, 2018, 2018, 2019, 2020],
    "State": ["CA", "TX", "FL", "NY", "CA", "TX", "FL", "NY", "CA", "TX"],
    "Race":  ["White", "Black", "Hispanic", "White", "Black", "White", "Hispanic", "Black", "White", "Hispanic"],
    "Age":   [34, 28, 45, 52, 23, 38, 29, 41, 55, 31],
    "Armed": ["Firearm", "Knife", "Unarmed", "Firearm", "Unarmed", "Firearm", "Vehicle", "Knife", "Firearm", "Unarmed"],
}
df = pd.DataFrame(data)


# --------------------------------------------------
#  TODO 1: Incidents per year
# --------------------------------------------------
print("Incidents per year:")
print(df.groupby("Year").size())


# --------------------------------------------------
#  TODO 2: By race: bar chart
# --------------------------------------------------
# sns.countplot(data=df, x="Race", order=df["Race"].value_counts().index)


# --------------------------------------------------
#  TODO 3: Age distribution: histogram + KDE
# --------------------------------------------------
# sns.histplot(df["Age"], kde=True, bins=10)


# --------------------------------------------------
#  TODO 4: Armed status breakdown: pie chart
# --------------------------------------------------
# armed_counts = df["Armed"].value_counts()
# plt.pie(armed_counts.values, labels=armed_counts.index, autopct="%1.1f%%")


# --------------------------------------------------
#  TODO 5: State-level choropleth (plotly)
# --------------------------------------------------
# import plotly.express as px
# state_counts = df["State"].value_counts().reset_index()
# fig = px.choropleth(state_counts, locations="State", locationmode="USA-states",
#                     color="count", scope="usa")
# fig.show()

print("\nArmed status breakdown:")
print(df["Armed"].value_counts())
