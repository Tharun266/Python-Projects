import tkinter as tk
from tkinter import messagebox

class TodoListManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List Manager")
        self.geometry("400x400")

        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
        # Task Entry Frame
        self.entry_frame = tk.Frame(self)
        self.entry_frame.pack(pady=10)

        self.task_label = tk.Label(self.entry_frame, text="Enter Task:", font=("Arial", 12))
        self.task_label.grid(row=0, column=0, padx=10)

        self.task_entry = tk.Entry(self.entry_frame, font=("Arial", 12), width=30)
        self.task_entry.grid(row=0, column=1, padx=10)

        self.add_button = tk.Button(self.entry_frame, text="Add Task", font=("Arial", 12), command=self.add_task)
        self.add_button.grid(row=0, column=2, padx=10)

        # Task List Frame
        self.list_frame = tk.Frame(self)
        self.list_frame.pack(padx=10, pady=10)

        self.task_list_label = tk.Label(self.list_frame, text="Tasks:", font=("Arial", 12))
        self.task_list_label.pack()

        self.task_listbox = tk.Listbox(self.list_frame, font=("Arial", 12), width=50, height=10)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Buttons Frame
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(pady=10)

        self.complete_button = tk.Button(self.button_frame, text="Mark Complete", font=("Arial", 12), command=self.mark_complete)
        self.complete_button.grid(row=0, column=0, padx=10)

        self.remove_button = tk.Button(self.button_frame, text="Remove Task", font=("Arial", 12), command=self.remove_task)
        self.remove_button.grid(row=0, column=1, padx=10)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty")

    def mark_complete(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            task = self.tasks[task_index]
            self.task_listbox.itemconfig(task_index, bg="light green")
        else:
            messagebox.showwarning("Warning", "Select a task to mark as complete")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.task_listbox.delete(task_index)
            del self.tasks[task_index]
        else:
            messagebox.showwarning("Warning", "Select a task to remove")

if __name__ == "__main__":
    app = TodoListManager()
    app.mainloop()
