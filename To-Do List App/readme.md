![Dark Mode](https://github.com/Hashibul01/PythonProjects/assets/77710050/0e7064df-8b22-47a1-8e65-4fb4b2ee3b6a)

![Light Mode](https://github.com/Hashibul01/PythonProjects/assets/77710050/996d2981-9758-45ca-a547-aa4944fee61c)

![View Stats](https://github.com/Hashibul01/PythonProjects/assets/77710050/8783d234-1217-4ada-a978-73d8ab9ace8c)

![Filter](https://github.com/Hashibul01/PythonProjects/assets/77710050/15406e2d-a5d7-49ac-8fa4-564ef6109051)


" import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from ttkbootstrap import Style
import json
from datetime import datetime
from dateutil import parser
from tkinter.simpledialog import askstring "

1) tkinter: This is Python's standard GUI (Graphical User Interface) library.
It provides tools to create windows, widgets, and handle events.

2) ttk: A submodule within tkinter that provides access to the Tk themed widget set.
It enhances and extends the capabilities of standard tkinter widgets.

3) messagebox: This module provides a set of functions for creating pop-up message boxes.
I used it to display information (in view stats) and errors (such as date format/ filter) to the user.

4) simpledialog: This module provides a way to create simple dialogs for prompting the user for input.

5) Style: This is from the ttkbootstrap library, which allows me to apply Bootstrap themes to ttk widgets, 
enhancing the visual appearance of the GUI.

6) json: This module is for working with JSON data, allowing the app to encode and decode JSON.

7) datetime: A module for working with dates and times.

8) parser: A module from the dateutil package, used for parsing date strings.

9) askstring: A function from tkinter.simpledialog for asking the user to input a string.
---------------------------------------------------------------------------------------------

"class TodoListApp(tk.Tk):
    def __init__(self):
        # ... (constructor method)
    def configure_style(self):
        # ... (method to configure the app style)
    def toggle_dark_mode(self):
        # ... (method to toggle dark mode)
    def view_stats(self):
        # ... (method to display task statistics)
    def add_task(self):
        # ... (method to add a task)
    def ask_due_date(self):
        # ... (method to ask for due date)
    def ask_priority(self):
        # ... (method to ask for task priority)
    # ... (other methods for various functionalities)"

1) Class Definition: Defines a class named TodoListApp that inherits from tk.Tk, representing the main application window.

2) Constructor Method (__init__): This method initializes the application.
It sets up the window, styles, widgets, and loads existing tasks from a file.

3) Other Methods: Various methods for different functionalities in the application, 
such as adding tasks, toggling dark mode, asking for due dates, asking for priorities, marking tasks as done, deleting tasks, etc.
------------------------------------------------------------------------------------------------------------------------------------

" def __init__(self):
    super().__init__()

 ... (rest of the constructor method) "

1) Super Method: Calls the constructor of the parent class (tk.Tk), initializing the main application window.
-------------------------------------------------------------------------------------------------------------

" style = Style(theme='flatly')
style.configure("Custom.TEntry", foreground="gray") "

1) Style Initialization: Initializes the app with a Bootstrap theme named 'flatly'.

2) Custom Styling: Configures a custom style for Entry widgets with gray foreground. 
This styling is applied to the input field for adding tasks.
------------------------------------------------------------------------------------

" self.task_input = ttk.Entry(self, font=("TkDefaultFont", 16), width=30, style="Custom.TEntry")
self.task_list = tk.Listbox(self, font=("TkDefaultFont", 16), height=10, selectmode=tk.NONE) "

1) Task Input Field: Creates an Entry widget (self.task_input) for entering tasks. Configures its font, width, and style.

2) Task Listbox: Creates a Listbox widget (self.task_list) for displaying tasks. Configures its font and height. 
The selectmode is set to tk.NONE, indicating that users can't select items from the list.

------------------------------------------------------------------------------------------------------------------------

" self.task_input.bind("<FocusIn>", self.clear_placeholder)
self.task_input.bind("<FocusOut>", self.restore_placeholder) "

1) Binding Events: Binds the <FocusIn> event to the clear_placeholder method and the 
<FocusOut> event to the restore_placeholder method. This is used to manage a placeholder text in the task input field.

-----------------------------------------------------------------------------------------------------------------------

" ttk.Checkbutton(self, text="Dark Mode", variable=self.dark_mode, command=self.toggle_dark_mode).pack(padx=10, pady=8)
ttk.Button(self, text="Add", command=self.add_task).pack(pady=5) 
... (other buttons for various actions) "

1) Dark Mode Checkbutton: Creates a Checkbutton for toggling dark mode. 
It's associated with the self.dark_mode variable, and the toggle_dark_mode method is called when it's clicked.

2) Add Task Button: Creates a Button for adding tasks. 
It's associated with the add_task method, which is called when the button is clicked.

------------------------------------------------------------------------------------------------------------------------

" self.load_tasks()
... (other methods: load_tasks and save_tasks) "

1) Loading Tasks: Calls the load_tasks method during the initialization to load tasks from a JSON file.

2) Saving Tasks: Various methods (add_task, mark_done, delete_task, etc.) 
call the save_tasks method to save the current tasks to a JSON file.

--------------------------------------------------------------------------------------------------------

" if __name__ == '__main__':
    app = TodoListApp()
    app.mainloop() "

1) Main Entry Point: Checks if the script is being run as the main module.
If true, creates an instance of TodoListApp and starts the main application loop using mainloop().

--------------------------------------------------------------------------------------------------------


## Frameworks Used: 
a) tkinter: Standard Python GUI Library
b) ttk: sub module within tkinter

## Database Used:
No direct usage of database. Tasks are stored on a JSON File as defined below. Tasks and coor (priority) are saved to the JSON file
and loaded into the listbox from the JSON file. 

" def load_tasks(self):
    try:
        with open("tasks.json", "r") as f:
            data = json.load(f)
            for task in data:
                self.task_list.insert(tk.END, task["text"])
                self.task_list.itemconfig(tk.END, fg=task["color"])

    except FileNotFoundError:
        pass

def save_tasks(self):
    data = []
    for i in range(self.task_list.size()):
        text = self.task_list.get(i)
        color = self.task_list.itemcget(i, "fg")
        data.append({"text": text, "color":color})
    with open("tasks.json","w") as f:
        json.dump(data, f) "
