#This file is to represent the interface on the terminal.
from ExportTXT import changeTask, addTask, deleteTask
from ImportTXT import getTasks, getDone
import datetime

def window():
    print("================================================")
    print(f"|Date: {datetime.datetime.now().strftime("%Y-%m-%d")}|")
    print("================================================")
    print("|1. View ToDo List|")
    print("|2. View Done List|")
    print("|3. Add Task|")
    print("|4. Change Task|")
    print("|5. Delete Task|")
    print("|6. Exit|")
    print("================================================")
    print("Enter your choice: ")
    choice = input()
    return choice

def viewTasks(tasks):
    print("================================================")
    print("|ToDo List|")
    print("================================================")
    for task in tasks:
        print(f"|{task}|")
    print("================================================")

def viewDone(done):
    print("================================================")
    print("|Done List|")
    print("================================================")
    for task in done:
        print(f"|{task}|")
    print("================================================")

def addTask(newTask):
    print("================================================")
    print("|Add Task|")
    print("================================================")
    print("Enter new task: ")
    newTask = input()
    addTask(newTask)

if __name__ == "__main__":
    while True:
        choice = window()
        if choice == "1":
            tasks = getTasks()
            print(tasks)
        elif choice == "2":
            done = getDone()
            print(done)
        elif choice == "3":
            newTask = input("Enter new task: ")
            addTask(newTask)