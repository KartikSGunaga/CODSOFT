class newTask:
    def __init__(self, taskName, dueDate, priority, notes):
        self.taskName = taskName
        self.dueDate = dueDate
        self.priority = priority
        self.notes = notes

class toDo:
    def __init__(self):
        self.taskList = []

    def addTask(self, task):
        self.taskList.append((task))
        print("\nTask added successfully!")
    def displayTasks(self):
        for task in self.taskList:
            print(f"Task: {task.taskName} \n"
                  f"Due: {task.dueDate} \n"
                  f"Priority: {task.priority} \n"
                  f"Additional Notes: {task.notes}")

    def viewTaskByName(self, taskName):
        for task in self.taskList:
            if task.taskName.lower() == taskName.lower():
                print(f"Task: {task.taskName} \n"
                      f"Due: {task.dueDate} \n"
                      f"Priority: {task.priority} \n"
                      f"Additional Notes: {task.notes}")

    def viewTaskByDate(self, date):
        for task in self.taskList:
            if task.dueDate.lower() == date.lower():
                print(f"Task: {task.taskName} \n"
                      f"Due: {task.dueDate} \n"
                      f"Priority: {task.priority} \n"
                      f"Additional Notes: {task.notes}")

    def modifyTask(self, taskName, updatedTaskName,
                   updatedDueDate, updatedPriority, updatedNotes):
        for task in self.taskList:
            if task.taskName.lower() == taskName.lower():
                task.taskName = updatedTaskName
                task.dueDate = updatedDueDate
                task.priority = updatedPriority
                task.notes = updatedNotes
                print("\n ToDo list updated successfully!")

    def deleteTask(self, taskName):
        self.taskList = [task for task in self.taskList
                         if task.taskName.lower() is not taskName]

def createTask(task):

    taskName = input("Enter the task name: ")
    dueDate = input("Enter the due Date of task: ")
    priority = input("Enter the priority (High, Medium, Low): ")
    notes = input("Enter additional notes if any: ")

    todo = newTask(taskName, dueDate, priority, notes)
    task.addTask(todo)

def menu():
    print("\n1. View Menu \n"
          "2. Add Task \n"
          "3. View All Tasks \n"
          "4. View specific task by name: \n"
          "5. View specific task by due date \n"
          "6. Modify existing task \n"
          "7. Delete task \n"
          "8. Exit")
def main():
    print("Welcome to ToDo Interface!")
    task = toDo()

    menu()
    while True:
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            menu()

        elif choice == 2:
            createTask(task)

        elif choice == 3:
            task.displayTasks()

        elif choice == 4:
            taskName = input("Enter the task name: ").lower()
            task.viewTaskByName(taskName)

        elif choice == 5:
            taskDate = input("Enter the task date: ")
            task.viewTaskByDate(taskDate)

        elif choice == 6:
            taskName = input("Enter the task name: ").lower()
            updatedTaskName = input("Enter the new task name: ")
            updatedDueDate = input("Enter the new task due date: ")
            updatedPriority = input("Enter the new task priority: ")
            updatedNotes = input("Enter the new task notes: ")
            
            task.modifyTask(taskName, updatedTaskName, updatedDueDate, updatedPriority, updatedNotes)

        elif choice == 7:
            taskName = input("Enter the task name: ").lower()
            task.deleteTask(taskName)

        elif choice == 8:
            print("Thank you for using the interface")
            break

        else:
            print("Invalid entry. Enter input in range(1-8)")

if __name__ == "__main__":
    main()

