import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="student_db"
)

cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    marks FLOAT
)
""")

print("Students table created successfully!")

con.close()