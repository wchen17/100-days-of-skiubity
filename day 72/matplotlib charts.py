# ============================================================
#  DAY 72: Data Visualisation with Matplotlib
#  PROJECT: Programming Language Popularity Over Time
# ============================================================
#
#  SKILLS TODAY:
#    - import matplotlib.pyplot as plt
#    - plt.plot(x, y, label="name")    → line chart
#    - plt.bar(x, height)              → bar chart
#    - plt.xlabel() / plt.ylabel() / plt.title()
#    - plt.legend()
#    - plt.show()
#    - plt.figure(figsize=(width, height))
#    - plt.xticks(rotation=45)
#    - Multiple subplots: plt.subplot(rows, cols, index)
#    - Styling: color, linewidth, marker, linestyle
#
#  pip install matplotlib pandas
#
# ============================================================

import matplotlib.pyplot as plt
import pandas as pd

# --------------------------------------------------
#  DEMO: Basic line chart
# --------------------------------------------------
years   = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
python  = [6.4,  7.8,  9.5, 11.0, 12.2, 15.0, 17.3, 19.5, 22.1]
java    = [20.1, 18.5, 17.0, 16.0, 14.8, 13.5, 12.0, 11.2, 10.5]
js      = [14.0, 13.5, 13.2, 12.8, 12.5, 12.0, 11.8, 11.5, 11.2]

plt.figure(figsize=(12, 6))
plt.plot(years, python, label="Python",     color="blue",   linewidth=2, marker="o")
plt.plot(years, java,   label="Java",       color="red",    linewidth=2, marker="s")
plt.plot(years, js,     label="JavaScript", color="yellow", linewidth=2, marker="^")
plt.xlabel("Year")
plt.ylabel("Popularity (%)")
plt.title("Programming Language Popularity 2016-2024")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# --------------------------------------------------
#  TODO 1: Bar chart: starting salaries by language
# --------------------------------------------------
languages = ["Python", "JavaScript", "Java", "C++", "Go", "Rust"]
salaries  = [90000, 82000, 88000, 95000, 105000, 110000]

# Create a horizontal bar chart (plt.barh) sorted by salary
# Add value labels on each bar

# --------------------------------------------------
#  TODO 2: Pie chart: market share of databases
# --------------------------------------------------
dbs    = ["PostgreSQL", "MySQL", "MongoDB", "SQLite", "Redis", "Other"]
shares = [36, 29, 18, 8, 5, 4]

# plt.pie(shares, labels=dbs, autopct="%1.1f%%", startangle=90)

# --------------------------------------------------
#  TODO 3: Subplot grid: 2x2 layout
# --------------------------------------------------
# Show all four chart types in a 2x2 grid:
# Top-left: line, top-right: bar, bottom-left: pie, bottom-right: scatter

# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Download Stack Overflow Developer Survey data and replicate
#     the "Most Loved Languages" chart
#  2. Animate your line chart using FuncAnimation
#  3. Save figures to file: plt.savefig("chart.png", dpi=150)
# ============================================================
