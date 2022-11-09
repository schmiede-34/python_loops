"""1. For-Schleife, """
for element in [2,4,6,8,12,44,456,3]:
    print(element)


    
"""2. For-Schleife, """    
for element in "Das ist eine neue Beschreibung-1-2-3-4":
    print(element)



"""3. For-Schleife, für das kleine 1x1 """
for x in range(1,5):
    for y in range(1,5):
        print("{} * {} = {}".format(x, y, x*y))