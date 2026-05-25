# 24 + 25 Mayıs / Python Basics
# Kaynak olarak -> Kaggle Python Basics: https://www.kaggle.com/learn/python




# List example

numbers = [10, 20, 30, 40, 50]

total = sum(numbers)
avg = total / len(numbers)

print("Total:", total)
print("Average:", avg)

# Dictionary example

student_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95
}


for student,grade in student_grades.items():
    print("Name:",student,"| Grade:",grade)

print("Best grade:",max(student_grades.values()),"by",max(student_grades.keys(),key=student_grades.get))
print("Worst grade:",min(student_grades.values()),"by",min(student_grades.keys(),key=student_grades.get))


# Function example

def calculate_avg_grades(student_grades):
    total = 0
    for grade in student_grades.values():
        total += grade
    return total / len(student_grades)

print("Average grade:",calculate_avg_grades(student_grades))

# Exception handling example(Try-Catch(Expect))

def safe_divide(a,b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero!"
    

print(safe_divide(10, 2))
print(safe_divide(10, 0))    


#CSV and JSON file handling example

import pandas as pd

# Reading a CSV file

grades = pd.read_csv("C:\\Projects\\internship-prep\\example-data\\grades.csv")
print("Head:")
print(grades.head())
print("Description:")
print(grades.describe())
print("Info:")
print(grades.info())
print("Shape:")
print(grades.shape)