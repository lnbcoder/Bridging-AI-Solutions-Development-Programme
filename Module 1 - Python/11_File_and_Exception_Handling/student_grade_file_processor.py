# File Handling Exercise
# Scenario: Student Grade File Processor
# Goal
#  - Safely read a file containing student grades and calculate the average.
#
# The Setup
# You have a file called grades.txt.
# Each line in the file contains one student’s grade:
# 85, 90, 78, 92
#
# Exercise
# Task
# 1.Use try with 'with open("grades.txt", "r") as file':
# 2.Read all lines from the file.
# 3.Convert each line into an integer.
# 4.Calculate and print the average grade.
# 5.Handle the following errors:
#  - FileNotFoundError → file doesn’t exist
#  - ValueError → a line contains invalid data (e.g. text)
# 6.Print "Grade processing complete." after the try / except block.

try:
    with open("grades.txt", "r") as file:
        marks_sum = 0
        content = file.readlines()
        count_marks = 0

        for mark in content:
            sum += int(mark.strip())
            count_marks += 1

        average = marks_sum / count_marks
        print("Students average:", average)

except FileNotFoundError:
    print("File doesn’t exist")
except:
    print("A line contains invalid data")

print("Grade processing complete.")