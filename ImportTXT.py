#This file purpose is to import elements from the storage.txt as a list.
def getTasks():
    tasks = []
    goodToCopy = False
    with open("storage.txt", "r") as file:
        for line in file:
            if line.startswith("*"):
                goodToCopy = True
            elif line.startswith("**"):
                goodToCopy = False
                break
            
            if goodToCopy == True:
                element = line.strip()
                tasks.append(element)
    return tasks

def getDone():
    done = []
    goodToCopy = False
    with open("storage.txt", "r") as file:
        for line in file:
            if line.startswith("$"):
                goodToCopy = True
            elif line.startswith("$$"):
                goodToCopy = False
            
            if goodToCopy == True:
                element = line.strip()
                done.append(element)
    return done
        