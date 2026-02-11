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

print(f"Student: {student1.name} School name: {student1.school}")
print(f"Student: {student2.name} School name: {student2.school}")

Student.school = "XYZ School"

print(f"Student: {student1.name} School name: {student1.school}")
print(f"Student: {student2.name} School name: {student2.school}")
