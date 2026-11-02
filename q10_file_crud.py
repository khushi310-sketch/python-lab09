FILE_NAME = "students.txt"

def add_record():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{roll},{name},{marks}\n")

    print("Record added successfully!")

def view_records():
    try:
        with open(FILE_NAME, "r") as file:
            print("\nStudent Records:")
            print(file.read())
    except FileNotFoundError:
        print("File not found!")

def update_record():
    roll = input("Enter Roll Number to update: ")
    updated = False

    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        with open(FILE_NAME, "w") as file:
            for record in records:
                data = record.strip().split(",")

                if data[0] == roll:
                    name = input("Enter New Name: ")
                    marks = input("Enter New Marks: ")
                    file.write(f"{roll},{name},{marks}\n")
                    updated = True
                else:
                    file.write(record)

        print("Record updated!" if updated else "Record not found!")

    except FileNotFoundError:
        print("File not found!")

def delete_record():
    roll = input("Enter Roll Number to delete: ")
    deleted = False

    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        with open(FILE_NAME, "w") as file:
            for record in records:
                if record.split(",")[0] == roll:
                    deleted = True
                else:
                    file.write(record)

        print("Record deleted!" if deleted else "Record not found!")

    except FileNotFoundError:
        print("File not found!")

while True:
    print("\n1. Add Record")
    print("2. View Records")
    print("3. Update Record")
    print("4. Delete Record")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_record()
    elif choice == "2":
        view_records()
    elif choice == "3":
        update_record()
    elif choice == "4":
        delete_record()
    elif choice == "5":
        break
    else:
        print("Invalid choice!")