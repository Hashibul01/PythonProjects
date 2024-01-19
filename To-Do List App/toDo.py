import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from ttkbootstrap import Style
import json
from datetime import datetime
from dateutil import parser
from tkinter.simpledialog import askstring

class TodoListApp(tk.Tk):
    def __init__(self):
        super().__init__()

        #App Window configuration
        self.title("Todo List App")
        self.geometry("450x600")
        style = Style(theme='flatly')
        style.configure("Custom.TEntry", foreground = "gray")

        #Dark Mode Flag
        self.dark_mode = tk.BooleanVar(value = False)

        #Input field for adding tasks
        self.task_input = ttk.Entry(self, font= (
            "TkDefaultFont", 16), width=30, style="Custom.TEntry")
        self.task_input.pack(pady=10)

        #Placeholder for input field
        self.task_input.insert(0, "Enter your todo here...")

        #Bind event to clear placeholder when input field is clicked
        self.task_input.bind("<FocusIn>", self.clear_placeholder)

        #Bind event to restore placeholder when input field loses focus
        self.task_input.bind("<FocusOut>", self.restore_placeholder)

        # Dark Mode Button
        ttk.Checkbutton(self, text="Dark Mode", variable=self.dark_mode,
                        command=self.toggle_dark_mode).pack(padx=10, pady=8)

        #Button for adding tasks
        ttk.Button(self, text="Add", command=self.add_task).pack(pady=5)

        # Listbox to display added tasks
        self.task_list = tk.Listbox(self, font = (
            "TkDefaultFont", 16), height=10, selectmode=tk.NONE)
        self.task_list.pack(fill=tk.BOTH, expand=True, padx = 10, pady=10)

        # Filter Button
        ttk.Button(self, text="Filter", style="info.TButton", 
                   command=self.show_filter_dialog).pack(fill=tk.BOTH, padx=80, pady=10)

        # Highlighting tasks for marking as complete or deleting
        ttk.Button(self, text = "Done", style="success.TButton",
                   command=self.mark_done).pack(fill=tk.BOTH, pady=10, padx = 80 )
        ttk.Button(self, text="Delete", style = "danger.TButton",
                  command=self.delete_task).pack(fill=tk.BOTH, pady=10, padx = 80)
        
        # Button to display task statistics
        ttk.Button(self, text="View Stats", style="info.TButton",
                   command = self.view_stats).pack(fill=tk.BOTH, padx = 80, pady = 10)
        
        self.load_tasks()

    def configure_style(self):
        if self.dark_mode.get():
            self.style = Style('darkly')      
        else:
            self.style = Style('flatly')
       
    def toggle_dark_mode(self):
        self.configure_style()

    def view_stats(self):
        done_count = 0
        total_count = self.task_list.size()
        for i in range(total_count):
            if self.task_list.itemcget(i, "fg") == "green":
                done_count += 1
        messagebox.showinfo("Task Statistics", f"Total Tasks: {total_count}\nCompleted Tasks: {done_count}")

    def add_task(self):
        task = self.task_input.get()

        if task != "Enter your todo here...":
            priority = self.ask_priority()
            due_date = self.ask_due_date()
            task_display = f"{priority}: {task} (Due: {due_date})"

            #Update Styling based on priority
            if priority.lower() == "high":
                color = 'red'
            elif priority.lower() == "medium":
                color = 'orange'
            else:
                color = 'yellow'

            self.task_list.insert(tk.END, task_display)
            self.task_list.itemconfig(tk.END, fg=color)
            self.task_input.delete(0, tk.END)
            self.save_tasks()

    def ask_due_date(self):
        due_date = askstring("Due Date", "Enter due date (YYYY-MM-DD):")
        try:
            parsed_due_date = parser.parse(due_date).strftime("%Y-%m-%d")
            return parsed_due_date
        except (TypeError, ValueError):
            return "Not Set"

    def ask_priority(self):
        priority = askstring("Priority", "Enter task priority (high, medium, low):")
        return priority.capitalize() if priority else "Medium"

    def mark_done(self):
        task_index = self.task_list.curselection()
        if task_index:
            self.task_list.itemconfig(task_index, fg="green")
            self.save_tasks()

    def delete_task(self):
        task_index = self.task_list.curselection()
        if task_index:
            self.task_list.delete(task_index)
            self.save_tasks()
    
    def clear_placeholder(self, event):
        if self.task_input.get() == "Enter your todo here...":
            self.task_input.delete(0, tk.END)
            self.task_input.configure(style="Custom.TEntry")

    def restore_placeholder(self, event):
        if self.task_input.get() == "":
            self.task_input.insert(0, "Enter your todo here...")
            self.task_input.configure(style="Custom.TEntry")

    def load_tasks(self):
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
            json.dump(data, f)

    def show_filter_dialog(self):
        filter_options = ["Priority (High to Low)", "Priority (Low to High)", "Clear Filters"]       
        while True:
            selected_filter = simpledialog.askstring("Filter Tasks", "Select Filter Option:", initialvalue=filter_options[0], parent=self)

            if selected_filter in filter_options:
                self.apply_filter(selected_filter)
                break
            elif selected_filter is None:
                # User pressed Cancel
                break
            else:
                messagebox.showwarning("Invalid Filter", "Please select a valid filter option.")

    def apply_filter(self, selected_filter):
        if selected_filter == "Priority (High to Low)":
            self.sort_tasks_by_priority(reverse=True)
        elif selected_filter == "Priority (Low to High)":
            self.sort_tasks_by_priority(reverse=False)
        elif selected_filter == "Clear Filters":
            self.clear_filters()


    def sort_tasks_by_priority(self, reverse=False):
        priority_values = {"Low": 1, "Medium":  2, "High": 3}

        tasks = [(self.task_list.get(i), self.task_list.itemcget(i, "fg")) for i in range(self.task_list.size())]
        sorted_tasks = sorted(tasks, key=lambda x: priority_values[x[0].split(":")[0]], reverse=reverse)
        self.update_task_list(sorted_tasks)

    def sort_tasks_by_due_date(self, reverse=False):
        tasks = [(self.task_list.get(i), self.task_list.itemcget(i, "fg")) for i in range(self.task_list.size())]
        sorted_tasks = sorted(tasks, key=lambda x: self.parse_due_date(x[0]) if "(Due: " in x[0] else datetime.max, reverse=reverse)
        self.update_task_list(sorted_tasks)

    def parse_due_date(self, task_text):
        try:
            return parser.parse(task_text.split("(Due: ")[-1][:-1]).strftime("%Y-%m-%d")
        except (TypeError, ValueError):
            return datetime.max

    def clear_filters(self):
    
        if self.task_list.size() > 0:
            # Clear the current task list
            self.task_list.delete(0, tk.END)
            # Load tasks from the saved state
            self.load_tasks()

    def update_task_list(self, sorted_tasks):
        self.task_list.delete(0, tk.END)
        for task_text, task_color in sorted_tasks:
            self.task_list.insert(tk.END, task_text)
            self.task_list.itemconfig(tk.END, fg=task_color)
        self.save_tasks()

if __name__ == '__main__':
    app = TodoListApp()
    app.mainloop()





        
        

