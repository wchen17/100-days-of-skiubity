# ============================================================
#  DAY 100 — FINAL CAPSTONE 🎉
#  PROJECT: Choose Your Own — Multivariable Regression or Personal Project
# ============================================================
#
#  OPTION A: Earnings Prediction (Multivariable Regression)
#    - Dataset: Census income data (UCI Machine Learning Repository)
#    - Predict whether someone earns >$50k/year
#    - Features: age, education, occupation, hours per week, etc.
#    - Techniques: logistic regression, decision trees, feature importance
#
#  OPTION B: Your Personal Dream Project
#    - What would you actually use every day?
#    - What problem have you wanted to automate?
#    - Build it. You have all the skills now.
#
#  SKILLS TO DEMONSTRATE ON DAY 100:
#    ✅ Data cleaning and feature engineering
#    ✅ Model training and evaluation
#    ✅ Web interface or CLI
#    ✅ Deployment (optional)
#    ✅ Clean, documented code
#    ✅ README with how to run it
#
# ============================================================

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt

# --------------------------------------------------
#  OPTION A: Census Earnings Classifier
# --------------------------------------------------

# Sample data (the real dataset has ~48,000 rows — download from UCI)
np.random.seed(42)
n = 500
df = pd.DataFrame({
    "age":          np.random.randint(18, 70, n),
    "education_yrs": np.random.randint(8, 18, n),
    "hours_per_week": np.random.randint(10, 80, n),
    "occupation":    np.random.choice(["Tech", "Sales", "Management", "Labour"], n),
    "sex":           np.random.choice(["Male", "Female"], n),
    "income":        np.random.choice([0, 1], n),  # 0 = <=50k, 1 = >50k
})


# --------------------------------------------------
#  TODO 1: Explore and clean the data
# --------------------------------------------------
print(df.head())
print(df.describe())
print("\nMissing values:\n", df.isnull().sum())


# --------------------------------------------------
#  TODO 2: Feature engineering
# --------------------------------------------------
# One-hot encode occupation and sex
# Check for class imbalance

df_encoded = pd.get_dummies(df, columns=["occupation", "sex"], drop_first=True)
print("\nClass balance:")
print(df["income"].value_counts(normalize=True))


# --------------------------------------------------
#  TODO 3: Train/test split and fit LogisticRegression
# --------------------------------------------------
X = df_encoded.drop("income", axis=1)
y = df_encoded["income"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)


# --------------------------------------------------
#  TODO 4: Evaluate
# --------------------------------------------------
y_pred = model.predict(X_test)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion matrix heatmap
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["<=50k", ">50k"], yticklabels=["<=50k", ">50k"])
plt.title("Confusion Matrix")
plt.show()


# --------------------------------------------------
#  TODO 5: Predict for a specific person
# --------------------------------------------------
# new_person = pd.DataFrame([{
#     "age": 35, "education_yrs": 16, "hours_per_week": 45,
#     "occupation_Sales": 0, "occupation_Management": 1, "occupation_Tech": 0,
#     "sex_Male": 1
# }])
# prediction = model.predict(new_person)[0]
# prob = model.predict_proba(new_person)[0]
# print(f"Predicted income: {'> $50k' if prediction else '<= $50k'}")
# print(f"Confidence: {max(prob)*100:.1f}%")


# ============================================================
#  CONGRATULATIONS! YOU'VE COMPLETED 100 DAYS OF CODE! 🎉
# ============================================================
#
#  What you've built over 100 days:
#    ✅ CLI games and tools (hangman, blackjack, calculator)
#    ✅ Turtle graphics games (snake, pong, breakout)
#    ✅ GUI desktop apps (Pomodoro, password manager, flash cards)
#    ✅ Web automation bots (Selenium, BeautifulSoup)
#    ✅ API-powered apps (weather, stocks, flights, Spotify)
#    ✅ Full-stack web apps (Flask + SQLAlchemy + Bootstrap)
#    ✅ User authentication and deployment
#    ✅ Data analysis and visualisation (pandas, matplotlib, plotly)
#    ✅ Machine learning (regression, classification)
#
#  Where to go from here:
#    → Contribute to open source (GitHub)
#    → Build a SaaS product with your Flask skills
#    → Learn FastAPI (faster, modern REST APIs)
#    → Explore Django (larger web framework)
#    → Learn React (pair it with your Flask API)
#    → Dive deeper into ML: TensorFlow, PyTorch
#    → Get certified: AWS, Google Cloud, Azure
#
# ============================================================
