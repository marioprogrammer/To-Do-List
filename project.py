import tkinter as tk
from tkinter import messagebox, filedialog

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")

def mark_done():
    try:
        selected_task_index = listbox.curselection()[0]
        task = listbox.get(selected_task_index)
        listbox.delete(selected_task_index)
        listbox.insert(tk.END, f"{task} - Done")
    except:
        messagebox.showwarning("Warning", "You must select a task to mark as done.")

def edit_task():
    try:
        selected_task_index = listbox.curselection()[0]
        old_task = listbox.get(selected_task_index)
        new_task = entry.get()
        if new_task != "":
            listbox.delete(selected_task_index)
            listbox.insert(selected_task_index, new_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a new task.")
    except:
        messagebox.showwarning("Warning", "You must select a task to edit.")

def save_tasks():
    try:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                tasks = listbox.get(0, tk.END)
                for task in tasks:
                    file.write(task + '\n')
            messagebox.showinfo("Success", "Tasks saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving tasks: {e}")

def load_tasks():
    try:
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                listbox.delete(0, tk.END)
                for line in file:
                    listbox.insert(tk.END, line.strip())
            messagebox.showinfo("Success", "Tasks loaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while loading tasks: {e}")

# Initialize main window
root = tk.Tk()
root.title("To-Do List")

# Set background color
root.config(bg="#f0f8ff")

# Create UI components
frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=50, height=10, bd=2, font=("Arial", 12), selectmode=tk.SINGLE, bg="#ffffff", fg="#000000")
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(root, width=50, font=("Arial", 12), bg="#ffffff", fg="#000000", bd=2)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=48, command=add_task, bg="#4CAF50", fg="#ffffff", font=("Arial", 12, "bold"))
add_button.pack(pady=5)

done_button = tk.Button(root, text="Mark as Done", width=48, command=mark_done, bg="#FFC107", fg="#000000", font=("Arial", 12, "bold"))
done_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=48, command=delete_task, bg="#F44336", fg="#ffffff", font=("Arial", 12, "bold"))
delete_button.pack(pady=5)

edit_button = tk.Button(root, text="Edit Task", width=48, command=edit_task, bg="#2196F3", fg="#ffffff", font=("Arial", 12, "bold"))
edit_button.pack(pady=5)

save_button = tk.Button(root, text="Save Tasks", width=48, command=save_tasks, bg="#9C27B0", fg="#ffffff", font=("Arial", 12, "bold"))
save_button.pack(pady=5)

load_button = tk.Button(root, text="Load Tasks", width=48, command=load_tasks, bg="#673AB7", fg="#ffffff", font=("Arial", 12, "bold"))
load_button.pack(pady=5)

# Start the main loop
root.mainloop()
