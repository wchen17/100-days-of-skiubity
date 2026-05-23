# ============================================================
#  DAY 71 — Pandas Data Exploration
#  PROJECT: College Major vs Salary Analysis
# ============================================================
#
#  SKILLS TODAY:
#    - pd.read_csv()
#    - df.shape, df.columns, df.dtypes
#    - df.head(n) / df.tail(n)
#    - df.describe()           → summary statistics
#    - df.sort_values("col", ascending=False)
#    - df["col"].max() / .min() / .mean()
#    - df[ df["col"] > value ] → boolean filtering
#    - NaN handling: df.dropna() / df.fillna(0)
#    - df[ ["col1", "col2"] ]  → select multiple columns
#
#  pip install pandas
#
# ============================================================

import pandas as pd

# --------------------------------------------------
#  Dataset: Post-university salary by major
#  Source: Wall Street Journal / PayScale (available on Kaggle)
#  For practice, create a mini version:
# --------------------------------------------------
data = {
    "Undergraduate Major":     ["Python/CS", "Electrical Engineering", "Philosophy", "Economics", "Biology", "Art"],
    "Starting Median Salary":  [70200, 63900, 42200, 50100, 36900, 32600],
    "Mid-Career Median Salary":[109000, 112000, 76100, 99200, 62000, 50000],
    "% Change":                [55, 75, 80, 98, 68, 53],
    "Mid-Career 90th Percentile Salary": [162000, 178000, 130000, 201000, 120000, 95000],
}
df = pd.DataFrame(data)

print("Shape:", df.shape)
print("\nFirst few rows:")
print(df.head())
print("\nSummary stats:")
print(df.describe())


# --------------------------------------------------
#  TODO 1: Which major has the highest starting salary?
# --------------------------------------------------
# Use df.sort_values() and print the top 3

# --------------------------------------------------
#  TODO 2: Which major has the highest % salary growth?
# --------------------------------------------------
# (highest "% Change")

# --------------------------------------------------
#  TODO 3: Which majors have mid-career salary below 60,000?
# --------------------------------------------------
# Use boolean filtering

# --------------------------------------------------
#  TODO 4: Add a new column "Salary Spread"
# --------------------------------------------------
# Spread = 90th percentile - mid-career median
# df["Salary Spread"] = ...
# Which major has the biggest spread? (means highest earners earn MUCH more than the median)

# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Download the full dataset from Kaggle and redo this analysis
#  2. Group by category (STEM / Business / Arts / Humanities)
#     using df.groupby("Category")["Starting Median Salary"].mean()
#  3. Plot a bar chart using matplotlib (preview of Day 72)
# ============================================================
