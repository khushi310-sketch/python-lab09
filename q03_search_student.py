students = [
    {"roll_no": 1, "name": "Aman", "marks": 85},
    {"roll_no": 2, "name": "Riya", "marks": 90},
    {"roll_no": 3, "name": "Rahul", "marks": 78}
]

search_name = input("Enter student name to search: ")

found = False

for student in students:
    if student["name"].lower() == search_name.lower():
        print("Student Found:", student)
        found = True

if not found:
    print("Student not found!")