students = [
    {"roll_no": 1, "name": "Aman", "marks": 85},
    {"roll_no": 2, "name": "Riya", "marks": 90},
    {"roll_no": 3, "name": "Rahul", "marks": 78}
]

roll = int(input("Enter roll number: "))
new_marks = int(input("Enter new marks: "))

found = False

for student in students:
    if student["roll_no"] == roll:
        student["marks"] = new_marks
        print("Marks updated successfully!")
        print(student)
        found = True
        break

if not found:
    print("Student not found!")