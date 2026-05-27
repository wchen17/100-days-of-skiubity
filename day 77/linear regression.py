# ============================================================
#  DAY 77: Linear Regression & Seaborn
#  PROJECT: Predict values with a regression line
# ============================================================
#
#  SKILLS TODAY:
#    - import seaborn as sns            → statistical visualisation
#    - sns.regplot(x, y, data=df)       → scatter + regression line
#    - from sklearn.linear_model import LinearRegression
#    - model = LinearRegression()
#    - model.fit(X, y)                  → train the model
#    - model.predict([[value]])         → make a prediction
#    - model.coef_ / model.intercept_   → slope and y-intercept
#    - r² score: model.score(X, y)      → how well the line fits
#    - pip install scikit-learn seaborn matplotlib pandas
#
# ============================================================

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample dataset: study hours vs exam score
np.random.seed(42)
hours = np.random.uniform(1, 10, 50)
scores = 7 * hours + np.random.normal(0, 5, 50) + 30

df = pd.DataFrame({"Study Hours": hours, "Exam Score": scores})


# --------------------------------------------------
#  TODO 1: Plot with seaborn regplot
# --------------------------------------------------
# sns.regplot(x="Study Hours", y="Exam Score", data=df)
# Add title, labels, show


# --------------------------------------------------
#  TODO 2: Fit a LinearRegression model
# --------------------------------------------------
# X = df[["Study Hours"]]   ← must be 2D for sklearn
# y = df["Exam Score"]
# model.fit(X, y)
# Print slope, intercept, r² score

X = df[["Study Hours"]]
y = df["Exam Score"]

model = LinearRegression()
# TODO: fit the model
# print(f"Slope: {model.coef_[0]:.2f}")
# print(f"Intercept: {model.intercept_:.2f}")
# print(f"R² score: {model.score(X, y):.3f}")


# --------------------------------------------------
#  TODO 3: Make predictions
# --------------------------------------------------
# What score would someone who studied 8 hours get?
# prediction = model.predict([[8]])
# print(f"Predicted score for 8 hours study: {prediction[0]:.1f}")


# --------------------------------------------------
#  TODO 4: Residuals analysis
# --------------------------------------------------
# residuals = y - model.predict(X)
# Plot a histogram of residuals: should be roughly normal


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Use multiple regression: add a "Attendance %" feature
#  2. Try polynomial regression for curved relationships
#     from sklearn.preprocessing import PolynomialFeatures
#  3. Split data into train/test sets to evaluate generalisation
#     from sklearn.model_selection import train_test_split
# ============================================================
