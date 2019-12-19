import sqlite3
import redis
import json
from time import sleep
from os import getloadavg
from atexit import register
from socket import gethostname
from datetime import datetime

hn = gethostname()
db = sqlite3.connect('avg.db')
r = redis.Redis('redis')

def closeDb():
    db.close()

register(closeDb)

db.execute('CREATE TABLE IF NOT EXISTS load (ts INTEGER NOT NULL, avg NUMBER NOT NULL)')

while True:
    avg = getloadavg()

    data = {
        'ts': datetime.now().isoformat(),
        'host': hn,
        'avg': str(avg[1])
    }

    msg = json.dumps(data)

    r.publish('avg', msg)
    db.execute("INSERT INTO load (ts, avg) VALUES (datetime('now'), ?)", (avg[1],))
    db.commit()
    print ("Load avg 5s: " + str(avg[1]))
    sleep(1)
