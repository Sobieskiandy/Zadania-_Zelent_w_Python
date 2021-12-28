import time
import random
print("Witaj w losowaniu, za 3 sekundy nastąpi zwolnienie blokady.")
time.sleep(3)
i=0
while(i<=6):
    print(random.randrange(1,50)) 
    time.sleep(1)
    i+=1