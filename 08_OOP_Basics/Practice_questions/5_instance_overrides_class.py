# Using the same Student class from the previous question:
# - student1.school = "Private School"
#
# Now print:
# - student1.school
# - student2.school
# - Student.school
#
# 👉 Predict before running.

# Create a class Student with:
# - class variable school = "ABC School"
# - instance variable name
#
# Create two students and print:
# - student1.school
# - student2.school
#
# Then change:
# - Student.school = "XYZ School"
# Print again.

class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

student1 = Student("Loveness")
student2 = Student("Ntshuxeko")

print(student1.school)
print(student2.school,"\n")

Student.school = "XYZ School"

print(student1.school)
print(student2.school,"\n")

student1.school = "Private School" # instance overrides class
print(student1.school)
print(student2.school)
print(Student.school)
