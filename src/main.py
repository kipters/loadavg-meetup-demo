from time import sleep
from os import getloadavg

while True:
    avg = getloadavg()
    print ("Load avg 5s: " + str(avg[1]))
    sleep(5)
