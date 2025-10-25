#This file purpose is to import elements from the storage.txt as a list.
tasks = []
goodToCopy = False
with open("storage.txt", "r") as file:
    for line in file:
        if line.startswith("*"):
            goodToCopy = not goodToCopy

            money = 0
        
        if goodToCopy == True:
            element = line.strip()
            tasks.append(element)
        