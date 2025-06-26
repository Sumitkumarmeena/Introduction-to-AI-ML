import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#  Load or simulate data
data = {
    "Student": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Math": [85, 70, 92, 60, 75, 88],
    "Science": [90, 65, 95, 58, 80, 85],
    "English": [78, 72, 88, 66, 77, 90],
    "Gender": ["F", "M", "M", "M", "F", "M"]
}
df = pd.DataFrame(data)

#  Style
sns.set(style="whitegrid")

#  Bar Plot – Average Scores
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)
plt.figure(figsize=(8, 5))
sns.barplot(x="Student", y="Average", data=df, palette="viridis")
plt.title("Average Scores by Student")
plt.show()

# Histogram – Math Scores
plt.figure(figsize=(7, 4))
sns.histplot(df["Math"], bins=5, kde=True, color="blue")
plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.show()

#  Line Plot – Individual Scores
plt.figure(figsize=(9, 5))
for subject in ["Math", "Science", "English"]:
    plt.plot(df["Student"], df[subject], marker='o', label=subject)
plt.title("Student Scores by Subject")
plt.ylabel("Score")
plt.legend()
plt.grid(True)
plt.show()

# Heatmap – Correlation Matrix
plt.figure(figsize=(6, 4))
corr = df[["Math", "Science", "English", "Average"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Subject Score Correlation")
plt.show()
