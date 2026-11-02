import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="student_db"
)

cur = con.cursor()

roll = int(input("Enter Roll Number: "))
marks = float(input("Enter New Marks: "))

cur.execute(
    "UPDATE students SET marks = %s WHERE id = %s",
    (marks, roll)
)

con.commit()

if cur.rowcount > 0:
    print("Marks updated successfully!")
else:
    print("Student not found!")

con.close()