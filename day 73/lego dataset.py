# ============================================================
#  DAY 73: Data Aggregation & Merging
#  PROJECT: LEGO Dataset Analysis
# ============================================================
#
#  SKILLS TODAY:
#    - df.groupby("col").count()        → count by group
#    - df.groupby("col")["col2"].mean() → aggregate
#    - pd.merge(df1, df2, on="col")     → join two DataFrames
#    - df["col"].value_counts()         → frequency count
#    - Pivot tables: df.pivot_table()
#    - Reshaping: df.melt()
#
#  Dataset: LEGO database (rebrickable.com/downloads: free)
#  For practice, use a mini version below.
#
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt

# Mini LEGO dataset
sets = pd.DataFrame({
    "set_num":  ["001-1", "002-1", "003-1", "004-1", "005-1"],
    "name":     ["Classic Space", "Town Square", "Castle Keep", "Pirate Ship", "Farm Set"],
    "year":     [1978, 1980, 1982, 1990, 1991],
    "theme_id": [1,    2,    3,    4,    2],
    "num_parts":[183,  450,  700,  560,  200],
})

themes = pd.DataFrame({
    "theme_id": [1, 2, 3, 4],
    "name":     ["Space", "Town", "Castle", "Pirates"],
})

# --------------------------------------------------
#  TODO 1: Which theme has the most sets?
# --------------------------------------------------
# Merge sets with themes on theme_id
# Group by theme name and count

# --------------------------------------------------
#  TODO 2: Average parts per theme
# --------------------------------------------------
# groupby + mean on num_parts

# --------------------------------------------------
#  TODO 3: How has LEGO set size (num_parts) changed over time?
# --------------------------------------------------
# Group by year, take mean of num_parts, plot as line chart

# --------------------------------------------------
#  TODO 4: Find the biggest set in each theme
# --------------------------------------------------
# df.groupby("theme")["num_parts"].max()
# or: df.sort_values("num_parts").drop_duplicates("theme", keep="last")
