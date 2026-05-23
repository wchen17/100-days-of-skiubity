# ============================================================
#  DAY 79 — Statistical Testing
#  PROJECT: Dr. Semmelweis Handwashing Discovery (t-test)
# ============================================================
#
#  SKILLS TODAY:
#    - Hypothesis testing: null hypothesis vs alternative
#    - from scipy import stats
#    - stats.ttest_ind(group1, group2)  → independent t-test
#    - p-value interpretation (p < 0.05 = statistically significant)
#    - Confidence intervals
#    - Before/after comparison
#
#  pip install scipy pandas matplotlib
#
# ============================================================

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Dr. Semmelweis found that handwashing dramatically reduced deaths
# Here's monthly death rates (%) before and after mandatory handwashing

before_washing = [10.0, 8.5, 9.2, 11.0, 12.3, 10.8, 9.5, 11.2, 10.1, 9.8, 11.5, 12.0]
after_washing  = [2.1,  1.9,  2.5,  1.8,  2.3,  2.0,  1.7,  2.2,  1.9,  2.1,  2.4,  2.0]

before = np.array(before_washing)
after  = np.array(after_washing)

# --------------------------------------------------
#  TODO 1: Calculate basic statistics for both groups
# --------------------------------------------------
# Print mean, std, and range for before and after

print("Before handwashing:")
print(f"  Mean: {before.mean():.2f}%")
# TODO: print std, min, max

print("\nAfter handwashing:")
# TODO: same


# --------------------------------------------------
#  TODO 2: Visualise the distributions
# --------------------------------------------------
# Plot two overlapping histograms (before = red, after = blue)
# Add vertical lines for the means


# --------------------------------------------------
#  TODO 3: Run an independent t-test
# --------------------------------------------------
# t_stat, p_value = stats.ttest_ind(before, after)
# If p_value < 0.05 → the difference is statistically significant

t_stat, p_value = stats.ttest_ind(before, after)
print(f"\nt-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.6f}")

if p_value < 0.05:
    print("Result: The difference IS statistically significant.")
    print("Handwashing made a measurable difference!")
else:
    print("Result: Cannot rule out chance. More data needed.")


# --------------------------------------------------
#  TODO 4: Calculate a 95% confidence interval for the difference
# --------------------------------------------------
# diff = before.mean() - after.mean()
# se   = stats.sem(before - after)   ← standard error of the mean
# ci   = stats.t.interval(0.95, df=len(before)-1, loc=diff, scale=se)
# print(f"95% CI for difference: {ci}")
