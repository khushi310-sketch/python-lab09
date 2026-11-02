import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="student_db"
)

cur = con.cursor()

cur.execute("SELECT COUNT(*) FROM students")

total = cur.fetchone()

print("Total Student Records:", total[0])

con.close()