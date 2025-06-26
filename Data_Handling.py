import pandas as pd
import numpy as np

data = {
    "Student": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Math": [85, 70, 92, 60, 75, 88],
    "Science": [90, 65, 95, 58, 80, 85],
    "English": [78, 72, 88, 66, 77, 90]
}

df = pd.DataFrame(data)
print("🎓 Initial Student Data:")
print(df)

# 2️ Calculate Average Score
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

# 3️ Grade with NumPy logic
def assign_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "F"

df["Grade"] = df["Average"].apply(assign_grade)

# 4️ Filter students with grade A or A+
top_students = df[df["Grade"].isin(["A", "A+"])]

# 5️ Sort by Average descending
df_sorted = df.sort_values(by="Average", ascending=False)

print("\n Final Data with Averages & Grades:")
print(df_sorted)

print("\n Top Performing Students (Grade A or A+):")
print(top_students[["Student", "Average", "Grade"]])

# 6️ Save to CSV (optional)
# df_sorted.to_csv("graded_students.csv", index=False)
