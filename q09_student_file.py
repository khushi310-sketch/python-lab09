# Save student data
with open("students.txt", "w") as file:
    file.write("101,Aman,85\n")
    file.write("102,Riya,90\n")
    file.write("103,Rahul,78\n")

print("Student data saved successfully!")

# Read student data
print("\nStudent Records:")

with open("students.txt", "r") as file:
    data = file.read()
    print(data)