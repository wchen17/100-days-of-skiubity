# ============================================================
#  DAY 80 — Capstone: Machine Learning
#  PROJECT: Predict House Prices (Multivariable Regression)
# ============================================================
#
#  SKILLS TODAY:
#    - Multivariable regression: multiple input features
#    - Feature engineering: log transform skewed data
#    - Train/test split: from sklearn.model_selection import train_test_split
#    - Evaluating model: RMSE, R²
#    - Underfitting vs overfitting
#    - Data cleaning: handle NaN, outliers
#    - pd.get_dummies() → encode categorical variables
#
#  pip install scikit-learn pandas numpy matplotlib seaborn
#
# ============================================================

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

# Synthetic house price dataset
n = 200
df = pd.DataFrame({
    "Size_sqft":  np.random.randint(500, 4000, n),
    "Bedrooms":   np.random.randint(1, 6, n),
    "Bathrooms":  np.random.randint(1, 4, n),
    "Age_years":  np.random.randint(0, 80, n),
    "Garage":     np.random.choice([0, 1], n),
    "Neighbourhood": np.random.choice(["Downtown", "Suburbs", "Rural"], n),
})
df["Price"] = (
    200 * df["Size_sqft"]
    + 15000 * df["Bedrooms"]
    + 10000 * df["Bathrooms"]
    - 500 * df["Age_years"]
    + 20000 * df["Garage"]
    + np.random.normal(0, 20000, n)
)


# --------------------------------------------------
#  TODO 1: Explore the data
# --------------------------------------------------
print(df.describe())
# Plot correlation heatmap
# sns.heatmap(df.corr(numeric_only=True), annot=True)


# --------------------------------------------------
#  TODO 2: Feature engineering
# --------------------------------------------------
# One-hot encode the Neighbourhood column
df = pd.get_dummies(df, columns=["Neighbourhood"], drop_first=True)

# Log transform Price to reduce skew
df["Log_Price"] = np.log(df["Price"])


# --------------------------------------------------
#  TODO 3: Train/test split
# --------------------------------------------------
features = ["Size_sqft", "Bedrooms", "Bathrooms", "Age_years", "Garage",
            "Neighbourhood_Suburbs", "Neighbourhood_Rural"]
X = df[features]
y = df["Log_Price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# --------------------------------------------------
#  TODO 4: Train model and evaluate
# --------------------------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

train_r2 = model.score(X_train, y_train)
test_r2  = model.score(X_test, y_test)
print(f"Train R²: {train_r2:.3f}")
print(f"Test R²:  {test_r2:.3f}")

# RMSE (in original price space → exponentiate predictions back)
y_pred    = model.predict(X_test)
y_pred_price = np.exp(y_pred)
y_test_price = np.exp(y_test)
rmse = np.sqrt(mean_squared_error(y_test_price, y_pred_price))
print(f"RMSE: ${rmse:,.0f}")


# --------------------------------------------------
#  TODO 5: Predict a specific house
# --------------------------------------------------
# new_house = pd.DataFrame([{
#     "Size_sqft": 1500, "Bedrooms": 3, "Bathrooms": 2,
#     "Age_years": 10, "Garage": 1,
#     "Neighbourhood_Suburbs": 1, "Neighbourhood_Rural": 0
# }])
# log_pred = model.predict(new_house)[0]
# price = np.exp(log_pred)
# print(f"Predicted price: ${price:,.0f}")

# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Try Random Forest instead of Linear Regression:
#     from sklearn.ensemble import RandomForestRegressor
#  2. Use cross-validation: from sklearn.model_selection import cross_val_score
#  3. Download the Ames Housing dataset from Kaggle for 80 real features
# ============================================================
