"""1. For-Schleife, die Variable element wird für jeden Eintrag in der Liste[2,4..] verwendet"""
for element in [2,4,6,8,12,44,456,3]:
    print(element)


    
"""2. For-Schleife, die Variable element wird für jedes Zeichen in dem String "Das ist.." verwendet"""    
for element in "Das ist eine neue Beschreibung-1-2-3-4":
    print(element)



"""3. For-Schleife, für das kleine 1x1 """
for a in range(1,5):
    for b in range(1,5):
        print("{} * {} = {}".format(a, b, a*b))