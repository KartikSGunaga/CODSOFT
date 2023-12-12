from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup


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
        self.taskList.append(task)

    def displayTasks(self):
        return "\n".join([f"Task: {task.taskName} \n"
                          f"Due: {task.dueDate} \n"
                          f"Priority: {task.priority} \n"
                          f"Additional Notes: {task.notes}" for task in self.taskList])

    def viewTaskByName(self, taskName):
        return [f"Task: {task.taskName} \n"
                f"Due: {task.dueDate} \n"
                f"Priority: {task.priority} \n"
                f"Additional Notes: {task.notes}" for task in self.taskList if taskName.lower() == task.taskName.lower()]

    def viewTaskByDate(self, date):
        return [f"Task: {task.taskName} \n"
                f"Due: {task.dueDate} \n"
                f"Priority: {task.priority} \n"
                f"Additional Notes: {task.notes}" for task in self.taskList if date.lower() == task.dueDate.lower()]

    def modifyTask(self, taskName, updatedTaskName, updatedDueDate, updatedPriority, updatedNotes):
        for task in self.taskList:
            if task.taskName.lower() == taskName.lower():
                task.taskName = updatedTaskName
                task.dueDate = updatedDueDate
                task.priority = updatedPriority
                task.notes = updatedNotes

    def deleteTask(self, taskName):
        self.taskList = [task for task in self.taskList if task.taskName.lower() != taskName.lower()]


class ToDoApp(App):
    def build(self):
        self.task = toDo()
        self.layout = BoxLayout(orientation='vertical')

        # Widgets
        self.label = Label(text="Welcome to ToDo Interface!", size_hint=(1, 2))
        self.layout.add_widget(self.label)

        # Buttons
        self.buttons = [
            Button(text="View Menu", on_press=self.viewMenu),
            Button(text="Add Task", on_press=self.createTask),
            Button(text="View All Tasks", on_press=self.viewAllTasks),
            Button(text="View Task by Name", on_press=self.viewTaskByName),
            Button(text="View Task by Due Date", on_press=self.viewTaskByDate),
            Button(text="Modify Task", on_press=self.modifyTask),
            Button(text="Delete Task", on_press=self.deleteTask),
            Button(text="Exit", on_press=self.exitApp)
        ]

        for button in self.buttons:
            self.layout.add_widget(button)

        return self.layout

    def viewMenu(self, instance):
        self.displayPopup("View Menu", "1. View Menu\n2. Add Task\n3. View All Tasks\n4. View Task by Name\n"
                                      "5. View Task by Due Date\n6. Modify Task\n7. Delete Task\n8. Exit")

    def createTask(self, instance):
        popup = Popup(title='Add Task', content=BoxLayout(orientation='vertical', spacing=10),
                      size_hint=(None, None), size=(400, 300))

        taskName_input = TextInput(hint_text='Task Name')
        dueDate_input = TextInput(hint_text='Due Date')
        priority_input = TextInput(hint_text='Priority')
        notes_input = TextInput(hint_text='Notes')

        save_button = Button(text='Save', on_press=lambda x: self.saveTask(taskName_input.text, dueDate_input.text,
                                                                           priority_input.text, notes_input.text, popup))

        popup.content.add_widget(taskName_input)
        popup.content.add_widget(dueDate_input)
        popup.content.add_widget(priority_input)
        popup.content.add_widget(notes_input)
        popup.content.add_widget(save_button)

        popup.open()

    def saveTask(self, taskName, dueDate, priority, notes, popup):
        task = newTask(taskName, dueDate, priority, notes)
        self.task.addTask(task)
        popup.dismiss()

    def viewAllTasks(self, instance):
        self.displayPopup("View All Tasks", self.task.displayTasks())

    def viewTaskByName(self, instance):
        popup = Popup(title='View Task by Name', content=BoxLayout(orientation='vertical', spacing=10),
                      size_hint=(None, None), size=(400, 300))

        taskName_input = TextInput(hint_text='Task Name')
        view_button = Button(text='View',
                             on_press=lambda x: self.showSearchResult(self.task.viewTaskByName(taskName_input.text), popup))

        popup.content.add_widget(taskName_input)
        popup.content.add_widget(view_button)

        popup.open()

    def viewTaskByDate(self, instance):
        popup = Popup(title='View Task by Due Date', content=BoxLayout(orientation='vertical', spacing=10),
                      size_hint=(None, None), size=(400, 300))

        date_input = TextInput(hint_text='Due Date')
        view_button = Button(text='View',
                             on_press=lambda x: self.showSearchResult(self.task.viewTaskByDate(date_input.text), popup))

        popup.content.add_widget(date_input)
        popup.content.add_widget(view_button)

        popup.open()

    def modifyTask(self, instance):
        popup = Popup(title='Modify Task', content=BoxLayout(orientation='vertical', spacing=10),
                      size_hint=(None, None), size=(400, 300))

        taskName_input = TextInput(hint_text='Task Name')
        updatedTaskName_input = TextInput(hint_text='Updated Task Name')
        updatedDueDate_input = TextInput(hint_text='Updated Due Date')
        updatedPriority_input = TextInput(hint_text='Updated Priority')
        updatedNotes_input = TextInput(hint_text='Updated Notes')

        update_button = Button(text='Update',
                               on_press=lambda x: self.task.modifyTask(taskName_input.text, updatedTaskName_input.text,
                                                                      updatedDueDate_input.text, updatedPriority_input.text,
                                                                      updatedNotes_input.text))

        popup.content.add_widget(taskName_input)
        popup.content.add_widget(updatedTaskName_input)
        popup.content.add_widget(updatedDueDate_input)
        popup.content.add_widget(updatedPriority_input)
        popup.content.add_widget(updatedNotes_input)
        popup.content.add_widget(update_button)

        popup.open()

    def deleteTask(self, instance):
        popup = Popup(title='Delete Task', content=BoxLayout(orientation='vertical', spacing=10),
                      size_hint=(None, None), size=(400, 300))

        taskName_input = TextInput(hint_text='Task Name')
        delete_button = Button(text='Delete',
                               on_press=lambda x: self.task.deleteTask(taskName_input.text))

        popup.content.add_widget(taskName_input)
        popup.content.add_widget(delete_button)

        popup.open()

    def showSearchResult(self, result, popup):
        if result:
            popup.content = Label(text="\n".join(result))
        else:
            popup.content = Label(text="No matching tasks found.")
        popup.height = 150

    def displayPopup(self, title, content):
        popup = Popup(title=title, content=Label(text=content), size_hint=(None, None), size=(400, 300))
        popup.open()

    def exitApp(self, instance):
        self.stop()


if __name__ == "__main__":
    ToDoApp().run()
