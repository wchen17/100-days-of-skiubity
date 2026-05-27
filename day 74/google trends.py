# ============================================================
#  DAY 74: Time Series & Google Trends
#  PROJECT: Visualise search trends and spot correlations
# ============================================================
#
#  SKILLS TODAY:
#    - pd.to_datetime()                 → parse date strings
#    - df.resample("M").mean()          → resample to monthly
#    - df.rolling(window=n).mean()      → rolling average (smooth noise)
#    - Correlation: df.corr()           → correlation matrix
#    - Dual-axis charts: ax1 = plt.subplot(), ax2 = ax1.twinx()
#    - fill_between() for shaded areas
#
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Sample time series data (monthly search interest, 0-100)
dates = pd.date_range(start="2020-01-01", periods=36, freq="MS")

data = pd.DataFrame({
    "Month":        dates,
    "Python":       [60, 58, 62, 70, 68, 72, 75, 80, 78, 82, 85, 90,
                     88, 85, 90, 92, 95, 93, 97, 100, 98, 96, 99, 100,
                     95, 97, 100, 98, 96, 94, 97, 99, 100, 98, 97, 100],
    "Unemployment": [3.5, 3.5, 13.0, 14.7, 13.3, 11.1, 10.2, 8.4, 7.9, 6.9, 6.7, 6.7,
                     6.4, 6.2, 6.0, 5.9, 5.8, 5.9, 5.4, 5.2, 4.8, 4.6, 4.2, 3.9,
                     3.7, 3.6, 3.5, 3.7, 3.8, 3.6, 3.5, 3.4, 3.7, 3.9, 4.0, 3.8],
})
data.set_index("Month", inplace=True)


# --------------------------------------------------
#  TODO 1: Plot Python search trend as a line chart
# --------------------------------------------------
# Use plt.figure, plt.plot, date formatting on x-axis

# --------------------------------------------------
#  TODO 2: Plot unemployment rate on a SECOND y-axis
# --------------------------------------------------
# ax1 = plt.gca()
# ax2 = ax1.twinx()
# ax2.plot(data.index, data["Unemployment"], color="red")

# --------------------------------------------------
#  TODO 3: Apply a 3-month rolling average to smooth the lines
# --------------------------------------------------
# data["Python_smooth"] = data["Python"].rolling(3).mean()

# --------------------------------------------------
#  TODO 4: Calculate and print the correlation between the two series
# --------------------------------------------------
# print(data.corr())

# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Download real data from trends.google.com → Download CSV
#  2. Compare "Bitcoin" vs "Tesla" search interest
#  3. Add a shaded recession period using plt.axvspan()
# ============================================================
