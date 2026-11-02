import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="student_db"
)

cur = con.cursor()

sql = "INSERT INTO students VALUES (%s, %s, %s, %s)"

values = (101, "Aman", 21, 85)

cur.execute(sql, values)
con.commit()

print("Student record inserted successfully!")

con.close()