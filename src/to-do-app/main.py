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
        
        self.to_do_items = [
            ToDoItem("Workout", "Push-Ups, Pull-Ups, Squats"),
            ToDoItem("House Work", "Clean kitchen, Sweep floors, Do laundry"),
            ToDoItem("Groceries", "Buy bread, milk, eggs"),
        ]
        
        # -Label Text Widget-
        self.label_text = StringVar()
        label = Label(frame, text = "Some label text", textvariable = self.label_text)
        # Configure the styling and sizing of the label text.
        label.configure(text = "New label text", font = ("Courier", 40))
        
        # -Entry Text Display-
        self.entry_text = StringVar()
        entry = Entry(frame, textvariable = self.entry_text)
        entry.grid(column = 2, row = 1)
    
        # -Input Box Button-
        button = Button(frame, text = "Button text", command = self.press_button)
        button.grid(column = 1, row = 2, sticky = (S, E, W))
        button.configure(width = 10, height = 2, font = ("Courier", 12))

        # -Dropdown List Widget-
        list_item_strings = ["Hey", "Hi", "Hello", "Howdy", "Greetings"]
        list_items = StringVar(value = list_item_strings)
        listbox = Listbox(frame, listvariable = list_items)
        listbox["height"] = 3
        listbox.bind("<<ListboxSelect>>", lambda s: self.select_item(listbox.curselection()))
        listbox.grid(column = 2, row = 2)
        
    # Button Press Logic Method
    def press_button(self):
        text = self.entry_text.get()
        self.label_text.set(text)
        
    # Dropdown Select Item Logic Method
    def select_item(self, index):
        selected_item = self.list_item_strings[index[0]]
        print(selected_item)
        
root = Tk()
ToDoListApp(root)
root.mainloop()