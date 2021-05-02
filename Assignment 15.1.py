import sqlite3
import re

#łączy się z bazą danych - jeśli takiej nie ma tworzy ją
conn = sqlite3.connect('emaildb.sqlite')

#OPEN HANDLE
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = ('mbox.txt')
text = open(fname)

for line in text:
    line = line.rstrip()
    ml = re.findall('^From \S+@(\S+)', line)
    if len(ml) == 0: continue
    mail = str(ml[0])
    
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (mail,))
    row = cur.fetchone()

    if row is None:
        cur.execute('INSERT INTO Counts (org,count) VALUES (?, 1)', (mail,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (mail,))
conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'

for row in cur.execute(sqlstr):
    print(row[0], row[1])

cur.close()