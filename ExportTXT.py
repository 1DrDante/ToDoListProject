#This file purpose is to change (add) the to-do list via use input.
def changeTask(deleteTask, changeTask):
    theFile = None
    with open("storage.txt", "r") as file:
        theFile = file.readlines()

    for line in theFile:
        if line.__contains__(deleteTask):
            theFile.remove(line)
            theFile.append(changeTask + "\n")
    
    with open("storage.txt", "w") as file:
        file.appendlines(theFile)

    print("Task changed successfully!")

def addTask(newTask):
    theFile = None
    starBeginningIndex = None
    starEndIndex = None
    with open("storage.txt", "r") as file:
        theFile = file.readlines()

    starBeginningIndex = theFile.index("*")
    starEndIndex = theFile.index("**")

    theFile.insert(starEndIndex, newTask + "\n")
    with open("storage.txt", "w") as file:
        file.appendlines(theFile)

    print("Task added successfully!")

def deleteTask(deleteTask):
    theFile = None
    if(deleteTask == "" or deleteTask == "*" ):
        print("No task to delete!")
        return
    
    with open("storage.txt", "r") as file:
        theFile = file.readlines()

    for line in theFile:
        if line.__contains__(deleteTask):
            theFile.remove(line)

    with open("storage.txt", "w") as file:
        file.appendlines(theFile)

    print("Task added successfully!")

