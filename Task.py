from tkinter import *
import tkinter.messagebox


class Task:
    def __init__(self, title, description, priority, due_date):
        self._title = title
        self._description = description
        self._priority = priority
        self._due_date = due_date


def add_task():
    pass


def delete_task():
    pass


def save_task():
    pass


def load_task():
    pass


def mark_task():
    pass


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

save_button = Button(window, text="Save selected", width=50, command=save_task)
save_button.pack(pady=3)

load_button = Button(window, text="Load task", width=50, command=load_task)
load_button.pack(pady=3)

mark_finished = Button(window, text="Mark as finished", width=50, command=mark_task)
mark_finished.pack(pady=3)

window.mainloop()
