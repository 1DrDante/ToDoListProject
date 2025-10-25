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
