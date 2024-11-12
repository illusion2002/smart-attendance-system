import mysql.connector

conn = mysql.connector.connect(
    host="localhost", username="root", password="qwerty123", database="bipin"
)
my_cursor = conn.cursor()

conn.commit()
conn.close()

print("Connection successful")
