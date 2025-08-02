import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create/connect to SQLite database
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS tasks (task TEXT)")
conn.commit()

def add_task():
    task = entry.get()
    if task:
        cursor.execute("INSERT INTO tasks VALUES (?)", (task,))
        conn.commit()
        entry.delete(0, tk.END)
        list_tasks()
    else:
        messagebox.showwarning("Warning", "Enter a task!")

def delete_task():
    try:
        selected = task_listbox.get(task_listbox.curselection())
        cursor.execute("DELETE FROM tasks WHERE task=?", (selected,))
        conn.commit()
        list_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task to delete!")

def list_tasks():
    task_listbox.delete(0, tk.END)
    for row in cursor.execute("SELECT * FROM tasks"):
        task_listbox.insert(tk.END, row[0])

root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

task_listbox = tk.Listbox(root, width=50)
task_listbox.pack(pady=10)

list_tasks()
root.mainloop()