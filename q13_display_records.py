import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="student_db"
)

cur = con.cursor()

cur.execute("SELECT * FROM students")

records = cur.fetchall()

for row in records:
    print(row)

con.close()