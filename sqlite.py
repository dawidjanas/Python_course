import sqlite3

#łączy się z bazą danych - jeśli takiej nie ma tworzy ją
conn = sqlite3.connect('emaildb2.sqlite')

#OPEN HANDLE
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

fname = ('mbox-short.txt')
text = open(fname)

for line in text:
    if not line.startswith("From: "): continue

    pieces = line.split()
    email = pieces[1]

    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cur.fetchone()

    if row is None:
        cur.execute('INSERT INTO Counts (email,count) VALUES (?, 1)', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    conn.commit()

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(row[0], row[1])

cur.close()