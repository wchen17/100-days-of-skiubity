# ============================================================
#  DAY 75: Interactive Charts with Plotly
#  PROJECT: Android App Store Analysis Dashboard
# ============================================================
#
#  SKILLS TODAY:
#    - import plotly.express as px          → high-level API
#    - import plotly.graph_objects as go    → low-level API
#    - px.scatter(), px.bar(), px.pie(), px.line()
#    - hover_data, color, size, title parameters
#    - fig.show()  → opens in browser (interactive!)
#    - pip install plotly pandas
#
# ============================================================

import plotly.express as px
import pandas as pd

# Sample app store data
data = pd.DataFrame({
    "App":      ["TikTok", "Instagram", "WhatsApp", "YouTube", "Spotify", "Netflix", "Twitter", "Snapchat"],
    "Category": ["Social", "Social",   "Social",   "Video",   "Music",   "Video",   "Social",  "Social"],
    "Rating":   [4.7, 4.6, 4.4, 4.5, 4.8, 4.5, 4.0, 4.2],
    "Reviews":  [15000000, 12000000, 9000000, 11000000, 8000000, 7000000, 4000000, 5000000],
    "Size_MB":  [170, 45, 50, 110, 80, 170, 60, 75],
    "Installs": [3000, 2000, 5000, 8000, 2000, 1000, 500, 1500],
})


# --------------------------------------------------
#  TODO 1: Scatter plot: Rating vs Size
# --------------------------------------------------
# Color by category, size by installs, hover shows app name

# fig = px.scatter(data, x="Size_MB", y="Rating", color="Category",
#                  size="Installs", hover_name="App", title="App Rating vs Size")
# fig.show()


# --------------------------------------------------
#  TODO 2: Bar chart: Average rating by category
# --------------------------------------------------
avg_by_cat = data.groupby("Category")["Rating"].mean().reset_index()
# fig = px.bar(avg_by_cat, x="Category", y="Rating", ...)
# fig.show()


# --------------------------------------------------
#  TODO 3: Pie chart: Installs by category
# --------------------------------------------------
# fig = px.pie(data, values="Installs", names="Category", title="...")
# fig.show()


# --------------------------------------------------
#  TODO 4: Box plot: Rating distribution by category
# --------------------------------------------------
# fig = px.box(data, x="Category", y="Rating", points="all")
# fig.show()

# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Download the real Google Play Store dataset from Kaggle
#  2. Build a Dash app (pip install dash) to show all charts in one page
#  3. Add a sunburst chart: category → app → install count
# ============================================================
