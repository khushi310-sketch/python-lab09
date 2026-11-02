students = [
    {"roll_no": 1, "name": "Aman", "marks": 85},
    {"roll_no": 2, "name": "Riya", "marks": 90},
    {"roll_no": 3, "name": "Rahul", "marks": 78}
]

roll = int(input("Enter roll number to delete: "))

found = False

for student in students:
    if student["roll_no"] == roll:
        students.remove(student)
        print("Student deleted successfully!")
        found = True
        break

if not found:
    print("Student not found!")

print("Remaining Records:")
for student in students:
    print(student)