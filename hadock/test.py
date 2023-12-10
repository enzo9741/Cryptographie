import time
from subprocess import call

for i in range(0, 100):
    call(["python", "tintin.py"])
    time.sleep(1)