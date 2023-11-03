from tkinter import *
import tkinter.messagebox


class Task:
    def __init__(self, title, description, priority, due_date):
        self._title = title
        self._description = description
        self._priority = priority
        self._due_date = due_date


tasks = []


def add_task():
    input_text = ""

    def add():
        input_text = entry_task.get(1.0, "end-1c")
        if input_text == "":
            tkinter.messagebox.showwarning(title="Warning", message="Please enter a valid task")
        else:
            listbox_task.insert(END, input_text)
            secondary_window.destroy()

    secondary_window = Tk()
    secondary_window.title("Add Task")
    entry_task = Text(secondary_window, width=40, height=4)
    entry_task.pack()
    secondary_button = Button(secondary_window, text="Add Task", command=add)
    secondary_button.pack()

    secondary_window.mainloop()


def delete_task():
    selected = listbox_task.curselection()
    listbox_task.delete(selected[0])


def save_task():
    pass


def load_task():
    pass


def mark_task():
    marked = listbox_task.curselection()
    temp = marked[0]
    # Store the text of the selected item in a temporary string
    temp_marked = listbox_task.get(temp)
    # Update
    temp_marked = temp_marked + " Done"
    listbox_task.delete(temp)
    listbox_task.insert(temp, temp_marked)


# Main Window
window = Tk()
window.title("To-Do List")
window.geometry("600x600")
window.resizable(0, 0)

# Frame Widget
frame_task = Frame(window)
frame_task.pack()

# Task listbox
listbox_task = Listbox(frame_task, bg="Black", fg="White", height=15, width=50, font="Helvetica")
listbox_task.pack()

# Scrollbar
scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=RIGHT, fill=Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

# Button widgets
add_button = Button(window, text="Add Task", width=50, command=add_task)
add_button.pack(pady=3)

delete_button = Button(window, text="Delete selected", width=50, command=delete_task)
delete_button.pack(pady=3)

# save_button = Button(window, text="Save selected", width=50, command=save_task)
# save_button.pack(pady=3)

# load_button = Button(window, text="Load task", width=50, command=load_task)
# load_button.pack(pady=3)

mark_finished = Button(window, text="Mark as finished", width=50, command=mark_task)
mark_finished.pack(pady=3)

window.mainloop()
