import sqlite3
from time import sleep
from os import getloadavg
from atexit import register

db = sqlite3.connect('avg.db')

def closeDb():
    db.close()

register(closeDb)

db.execute('CREATE TABLE IF NOT EXISTS load (ts INTEGER NOT NULL, avg NUMBER NOT NULL)')

while True:
    avg = getloadavg()
    db.execute("INSERT INTO load (ts, avg) VALUES (datetime('now'), ?)", (avg[1],))
    db.commit()
    print ("Load avg 5s: " + str(avg[1]))
    sleep(5)
