import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="student_db"
)

cur = con.cursor()

roll = int(input("Enter Roll Number: "))

cur.execute(
    "SELECT * FROM students WHERE id = %s",
    (roll,)
)

record = cur.fetchone()

if record:
    print("Student Found:", record)
else:
    print("Student not found!")

con.close()