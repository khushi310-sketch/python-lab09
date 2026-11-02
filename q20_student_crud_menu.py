import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD",
        database="student_db"
    )

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Thank you!")
        break

    con = None

    try:
        con = connect_db()
        cur = con.cursor()

        if choice == "1":
            sid = int(input("Enter Roll Number: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            marks = float(input("Enter Marks: "))

            cur.execute(
                "INSERT INTO students VALUES (%s, %s, %s, %s)",
                (sid, name, age, marks)
            )
            con.commit()
            print("Student added successfully!")

        elif choice == "2":
            cur.execute("SELECT * FROM students")

            for row in cur.fetchall():
                print(row)

        elif choice == "3":
            sid = int(input("Enter Roll Number: "))
            marks = float(input("Enter New Marks: "))

            cur.execute(
                "UPDATE students SET marks = %s WHERE id = %s",
                (marks, sid)
            )
            con.commit()
            print("Marks updated!" if cur.rowcount else "Student not found!")

        elif choice == "4":
            sid = int(input("Enter Roll Number: "))

            cur.execute(
                "DELETE FROM students WHERE id = %s",
                (sid,)
            )
            con.commit()
            print("Student deleted!" if cur.rowcount else "Student not found!")

        else:
            print("Invalid choice!")

    except (mysql.connector.Error, ValueError) as e:
        print("Error:", e)

    finally:
        if con is not None and con.is_connected():
            con.close()