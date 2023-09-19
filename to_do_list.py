import tkinter as tk
from tkinter import messagebox

# Initialize the main application window
root = tk.Tk()
root.title("To-Do List")

# Create a list to store tasks
tasks = []

# Function to add a task to the list and update the GUI
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to delete a selected task and update the GUI
def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Function to update the list of tasks in the GUI
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# Function to search for a task and display the result
def search_task():
    query = search_entry.get().strip().lower()
    if query:
        result = [task for task in tasks if query in task.lower()]
        task_listbox.delete(0, tk.END)
        if result:
            for task in result:
                task_listbox.insert(tk.END, task)
        else:
            task_listbox.insert(tk.END, "No matching tasks found.")
    else:
        messagebox.showwarning("Warning", "Please enter a search query.")

# Create and pack the task entry field
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

# Create and pack the buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
search_button = tk.Button(root, text="Search", command=search_task)
update_button = tk.Button(root, text="Update Task", command=update_task_list)


add_button.pack()
delete_button.pack()
search_button.pack()
update_button.pack()

# Create and pack the task listbox
task_listbox = tk.Listbox(root, height=10, width=40)
task_listbox.pack()

# Create and pack the search entry field
search_entry = tk.Entry(root, width=30)
search_entry.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
