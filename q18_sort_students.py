import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="student_db"
)

cur = con.cursor()

cur.execute("SELECT * FROM students ORDER BY name ASC")

for row in cur.fetchall():
    print(row)

con.close()