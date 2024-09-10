import sqlite3


conn = sqlite3.connect('testDB.db')


conn.execute("""
CREATE TABLE IF NOT EXISTS STUDENT 
             (ROLLNO INT NOT NULL,
             NAME TEXT NOT NULL,
             AGE INT NOT NULL  
             )
""")


conn.execute("INSERT INTO STUDENT (ROLLNO, NAME, AGE) VALUES (12, 'Rajesh Kumar', 21)")
conn.commit()


result = conn.execute("SELECT * FROM STUDENT")
for row in result:
    print("--------STUDENT DETAILS----------")
    print("Roll Number: ", row[0])
    print("Name:", row[1])
    print("Age:", row[2])
    print("----------------------------------")


conn.close()

