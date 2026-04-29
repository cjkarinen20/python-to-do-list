from tkinter import * 
import tkinter as tk

# To-Do List Item Object Class
class ToDoItem:

    def __init__(self, name, description):
        self.name = name
        self.description = description

# Main Application Class
class ToDoListApp:
    
    def __init__(self, root):
        
        # -Application Window Title-
        root.title("To-Do List")

        # -Application Window Frame-
        frame = Frame(root, borderwidth = 2, relief = "sunken")
        frame.grid(column = 1, row = 1, sticky = (N, E, S, W))
        root.columnconfigure(1, weight = 1)
        root.rowconfigure(1, weight = 1)

        # -To-Do List Label Text-
        list_label = Label(frame, text = "To Do Items")
        list_label.grid(column = 1, row = 1, sticky = (S, W))
        
        # -To-Do List Items-
        self.to_do_items = [
            ToDoItem("Workout", "Push-Ups, Pull-Ups, Squats"),
            ToDoItem("House Work", "Clean kitchen, Sweep floors, Do laundry"),
            ToDoItem("Groceries", "Buy bread, milk, eggs"),
        ]
        
        # -Get To-Do Item Names-
        self.to_do_names = StringVar(value = list(map(lambda x: x.name, self.to_do_items)))
        
        # -Dropdown List Box-
        items_list = Listbox(frame, listvariable = self.to_do_names)
        items_list.bind("<<ListboxSelect>>", lambda s: self.select_item(items_list.curselection()))
        items_list.grid(column = 1, row = 2, sticky = (E, W))

        # -Selected Description Label-
        self.selected_description = StringVar()
        selected_description_label = Label(frame, textvariable = self.selected_description)
        selected_description_label.grid(column = 1, row = 3, sticky = (E, W))


        # -Label Text-
        self.label_text = StringVar()
        label = Label(frame, text = "Some label text", textvariable = self.label_text)
        
        label.configure(text = "New label text", font = ("Courier", 40))
        
        # -Entry Text Display-
        self.entry_text = StringVar()
        entry = Entry(frame, textvariable = self.entry_text)
        # entry.grid(column = 2, row = 1)
    
        # -Input Box Button-
        button = Button(frame, text = "Button text", command = self.press_button)
        # button.grid(column = 1, row = 2, sticky = (S, E, W))
        # button.configure(width = 10, height = 2, font = ("Courier", 12))
        
    # -Button Press Logic Method-
    def press_button(self):
        text = self.entry_text.get()
        self.label_text.set(text)
        
    # -Dropdown Select Item Logic Method-
    def select_item(self, index):
        selected_item = self.to_do_items[index[0]]
        self.selected_description.set(selected_item.description)
        
root = Tk()
ToDoListApp(root)
root.mainloop()