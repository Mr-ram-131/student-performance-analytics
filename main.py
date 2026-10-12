import pandas as pd
import numpy as np

df = pd.read_csv("students.csv")

print("========== STUDENT RECORDS ==========")
print(df.head())

print("========== DATASET INFORMATION ==========")
print("Total students:", len(df))
print("Number of columns:", len(df.columns))
print("Dataset shape:", df.shape)

print("========== COLUMN NAMES ==========")
print(df.columns.tolist())

print("========== BASIC STATISTICS ==========")
print(df.describe())


subjects = ["Python","Mathematics","Statistics","SQL","Computer_Science"]
df["Total_Marks"] = df[subjects].sum(axis=1)

df["Average_Marks"] = np.mean(df[subjects].to_numpy(), axis=1)

print("========== Student performance ==========")
print(df[["Student_ID","Name","Total_Marks","Average_Marks"]])



def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"



df["Grade"] = df["Average_Marks"].apply(calculate_grade)

print("\n========== STUDENT GRADES ==========")
print(df[["Student_ID", "Name", "Average_Marks", "Grade"]])


def check_result(row):
    for subject in subjects:
        if row[subject] < 35:
            return "Fail"

    if row["Average_Marks"] >= 40:
        return "Pass"
    else:
        return "Fail"


df["Result"] = df.apply(check_result, axis=1)

print("\n========== PASS/FAIL RESULTS ==========")
print(df[["Student_ID", "Name", "Average_Marks", "Grade", "Result"]])


print("\n========== RESULT SUMMARY ==========")
print(df["Result"].value_counts())



highest = df.loc[df["Average_Marks"].idxmax()]

print("\n========== HIGHEST PERFORMER ==========")
print("Name:", highest["Name"])
print("Average Marks:", highest["Average_Marks"])


lowest = df.loc[df["Average_Marks"].idxmin()]

print("\n========== LOWEST PERFORMER ==========")
print("Name:", lowest["Name"])
print("Average Marks:", lowest["Average_Marks"])


print("\n========== SUBJECT-WISE PERFORMANCE ==========")

for subject in subjects:
    average = df[subject].mean()
    print(subject, ":", round(average, 2))



print("\n========== TOP 5 STUDENTS ==========")

top_students = df.sort_values(by="Average_Marks", ascending=False).head(5)

print(top_students[["Student_ID", "Name", "Average_Marks", "Grade"]])