import sqlite3

conn = sqlite3.connect("jobhunter.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM candidates")

rows = cursor.fetchall()

print(f"Total Records: {len(rows)}\n")

for row in rows:
    print(row)

conn.close()