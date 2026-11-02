import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="student_db"
)

cur = con.cursor()

roll = int(input("Enter Roll Number to delete: "))

cur.execute(
    "DELETE FROM students WHERE id = %s",
    (roll,)
)

con.commit()

if cur.rowcount > 0:
    print("Student deleted successfully!")
else:
    print("Student not found!")

con.close()