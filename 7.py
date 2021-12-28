population=1
hours=0

while population<=1000000000:
    hours=hours+1
    population=population*2
    if hours!=30:
        continue
    print("-------------------------")
    print("Hours:"+str(hours))
    print("Population:"+str(population))
    print("-------------------------")