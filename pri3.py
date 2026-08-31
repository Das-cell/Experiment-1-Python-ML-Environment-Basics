import pandas as pd
data = {
    "Student_Name": ["Rahul", "Pritam", "Anuvab", "Samrat", "Shruti",
                     "Mohak", "Haladar", "Aryan", "Vikram", "Rishi"],
    "Roll_Number": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks": [78, 85, 92, 67, 74, 88, 95, 60, 81, 73],
    "Attendance": [90, 95, 88, 75, 82, 91, 96, 70, 89, 80]
}

df = pd.DataFrame(data)
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

df["Grade"] = df["Marks"].apply(calculate_grade)
print(df)
