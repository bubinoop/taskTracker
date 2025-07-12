import datetime

# Task ID ist jeweiliger Index in Liste

task_status =       []
task_createdAt =    []
task_updatedAt =    []
task_description =  []

def Add(taskName):
    task_description.append(taskName)
    task_status.append("todo")
    task_createdAt.append(datetime.datetime.now())
    task_updatedAt.append(datetime.datetime.now())

def Update(updateTask, changeTask):
    task_description[updateTask] = changeTask
    task_updatedAt[updateTask] = datetime.datetime.now()

def Delete(deleteTask):
    task_description.pop(deleteTask)
    task_status.pop(deleteTask)
    task_createdAt.pop(deleteTask)
    task_updatedAt.pop(deleteTask)

def MarkInProgress(markTask):
    task_status[markTask] = "in-progress"

def MarkDone(markTask):
    task_status[markTask] = "done"

def SearchTaskList(searchWord):
    taskIndex = []

    for i in range(len(task_status)):
        if searchWord == task_status[i]: taskIndex.append(i)

    print(">---------<")

    for i in range(len(taskIndex)):
        print(task_description[taskIndex[i]])
        print(task_status[taskIndex[i]])
        print(task_createdAt[taskIndex[i]])
        print(task_updatedAt[taskIndex[i]])
        print(">---------<")

def PrintTasks():
    print(">---------<")

    for i in range(len(task_description)):
        print(task_description[i])
        print(task_status[i])
        print(task_createdAt[i])
        print(task_updatedAt[i])
        print(">---------<")


#|---------------------PROGRAMM-----------------------------|

trackerIsRunning = True

while trackerIsRunning:
    print("|--------------------------------------------|")
    match input("Enter your Command: "):
        case "help":
            print("Commands: 'add', 'update', 'delete', 'mark-in-progress', 'mark-done', 'list done', 'list todo', 'list in-pogress', 'quit'")

        case "add":
            Add(input("Enter Task: "))
            print(task_description)

        case "update":
            updateTask = int(input("Update Task: "))
            Update(updateTask, input(f"{task_description[updateTask]} --> "))
            print(task_description)

        case "delete":
            Delete(int(input("Delete Task: ")))

        case "mark-in-progress":
            MarkInProgress(int(input("Mark Task: ")))

        case "mark-done":
            MarkDone(int(input("Mark Task: ")))

        case "list done":
            SearchTaskList("done")
            
        case "list todo":
            SearchTaskList("todo")

        case "list in-progess":
            SearchTaskList("in-progress")

        case "list all":
            PrintTasks()

        case "quit":
            trackerIsRunning = False