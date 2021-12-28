import time
import os
i=5
clear  = lambda: os.system('cls')
while i > 0:
    clear()
    print(i)
    time.sleep(1)
    i=i-1
print("KABOOM")