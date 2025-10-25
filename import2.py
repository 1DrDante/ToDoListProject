def gettodo():
    task_list = []
    copiable = False
    with open("storage.txt", "r") as file:
        for line in file:
            if line.startswith("*"):
                copiable = True
            if line.startswith("**"):
                copiable = False

            if copiable:
                power = line.strip()
                task_list.append(power)

    return task_list
def gettodo2():
    task_list2 = []
    switch = False
    with open("storage.txt", "r") as file:
        for lines in file:
            if switch:
                gone = lines.strip()
                task_list2.append(gone)
            if lines.startswith("$$"):
                switch = False
            elif lines.startswith("$"):
                switch = True

    return task_list2
print(gettodo2())
