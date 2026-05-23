# ============================================================
#  DAY 78 — Multi-library Data Analysis
#  PROJECT: Nobel Prize Winners Dataset
# ============================================================
#
#  SKILLS TODAY:
#    - Combining pandas, matplotlib, seaborn, and plotly
#    - Categorical data analysis
#    - Time series (prizes over decades)
#    - Choropleth map with plotly (prizes by country)
#    - Sunburst / treemap charts
#
#  Dataset: from Kaggle "Nobel Prize" — or use sample below
#
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Mini Nobel dataset
data = pd.DataFrame({
    "Year":     [1901, 1903, 1906, 1921, 1964, 1993, 2015, 2020, 2022],
    "Category": ["Physics","Physics","Chemistry","Physics","Chemistry","Peace","Medicine","Medicine","Physics"],
    "Country":  ["Germany","France","Germany","Germany","UK","South Africa","Japan","USA","France"],
    "Gender":   ["Male","Female","Male","Male","Female","Male","Male","Male","Male"],
    "Name":     ["Röntgen","Curie","Moissan","Einstein","Hodgkin","Mandela","Ōmura","Harvey","Aspect"],
})


# --------------------------------------------------
#  TODO 1: Which category has the most prizes?
# --------------------------------------------------
# data["Category"].value_counts()  → plot as bar chart


# --------------------------------------------------
#  TODO 2: Prizes by decade
# --------------------------------------------------
# data["Decade"] = (data["Year"] // 10) * 10
# Group by decade, count, plot as line chart


# --------------------------------------------------
#  TODO 3: Gender breakdown
# --------------------------------------------------
# How many female laureates per category?
# data[data["Gender"] == "Female"].groupby("Category").count()


# --------------------------------------------------
#  TODO 4: Prize distribution by country (choropleth)
# --------------------------------------------------
# import plotly.express as px
# country_counts = data["Country"].value_counts().reset_index()
# fig = px.choropleth(country_counts, locations="Country",
#                     locationmode="country names",
#                     color="count", title="Nobel Prizes by Country")
# fig.show()


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Download the full dataset from Kaggle (900+ records)
#  2. Find the average age at prize time (birth year vs prize year)
#  3. Build an interactive Dash dashboard for the full analysis
# ============================================================
