import pandas as pd

data = {
    "Student_Name": ["Rahul", "Pritam", "Samrat", "Shruti", "Anuvab",
                     "Mohak", "Rishi", "Bikram", "Haladhar", "Aryan"],
    "Roll_Number": [1,2,3,4,5,6,7,8,9,10],
    "Marks": [78, 85, 92, 67, 74, 88, 95, 60, 81, 73],
    "Attendance": [90, 95, 88, 75, 82, 91, 96, 70, 89, 80]
}

df = pd.DataFrame(data)

result = df[df["Marks"] > 80]

print(result)
