# Week 4: Intro to Machine Learning 
# Linear Regression – Predicting Scores based on Study Hours

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1️ Sample Data
data = {
    "Hours_Studied": [1, 2, 3, 4.5, 5, 6.1, 7.5, 8.2, 9, 10],
    "Exam_Score": [32, 45, 50, 55, 62, 67, 73, 79, 88, 94]
}
df = pd.DataFrame(data)

# 2️ Visualize
plt.scatter(df["Hours_Studied"], df["Exam_Score"], color='blue')
plt.title("Hours Studied vs Exam Score")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.grid(True)
plt.show()

# 3️ Prepare Data
X = df[["Hours_Studied"]]
y = df["Exam_Score"]

# 4️ Train Model
model = LinearRegression()
model.fit(X, y)

# 5️ Predictions
df["Predicted_Score"] = model.predict(X)

# 6️ Plot with Line
plt.scatter(X, y, label="Actual", color="blue")
plt.plot(X, df["Predicted_Score"], label="Predicted", color="red")
plt.title("Linear Regression - Study vs Score")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.legend()
plt.grid(True)
plt.show()

# 7️ Metrics
print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)
print("R2 Score:", r2_score(y, df["Predicted_Score"]))
print("MSE:", mean_squared_error(y, df["Predicted_Score"]))
