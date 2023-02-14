import sqlite3
conn = sqlite3.connect('sql.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE Pupils (ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL, Name TEXT, Surname TEXT)''')
cur.execute('''INSERT INTO Pupils (ID, Name,Surname) Values (2, 'Максим', 'Суханов')''')
cur.execute('''INSERT INTO Pupils (ID, Name,Surname) Values (3, 'Мария', 'Алтышева')''')
cur.execute('''DELETE FROM Pupils WHERE Surname LIKE "Алтышева" ''')
cur.execute('DROP TABLE Pupils2')
conn.commit()
conn.close()