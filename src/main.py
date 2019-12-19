import sqlite3
import redis
from time import sleep
from os import getloadavg
from atexit import register

db = sqlite3.connect('avg.db')
r = redis.Redis('redis')

def closeDb():
    db.close()

register(closeDb)

db.execute('CREATE TABLE IF NOT EXISTS load (ts INTEGER NOT NULL, avg NUMBER NOT NULL)')

while True:
    avg = getloadavg()
    r.publish('avg', str(avg[1]))
    db.execute("INSERT INTO load (ts, avg) VALUES (datetime('now'), ?)", (avg[1],))
    db.commit()
    print ("Load avg 5s: " + str(avg[1]))
    sleep(1)
