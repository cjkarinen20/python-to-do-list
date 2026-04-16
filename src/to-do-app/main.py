from tkinter import * 
import tkinter as tk

class MyApp:
    
    def __init__(self, root):
        root.title("My app")
        root.geometry("500x400")
        root.maxsize(1000, 800)
        
        self.label_text = StringVar()
        label = Label(root, text = "Some label text", textvariable = self.label_text)
        #label.pack(side = tk.LEFT)
        
        #label["text"] = "New label text"
        #label["font"] = ("Courier", 40)
        
        label.configure(text = "New label text", font = ("Courier", 40))
        
        self.entry_text = StringVar()
        entry = Entry(root, textvariable = self.entry_text)
        #entry.pack(side = tk.LEFT)
        entry.place(x = 100, y = 50)
        
        
        #label["textvariable"] = entry_text

        button = Button(root, text = "Button text", command = self.press_button)
        button.pack(side = tk.LEFT)
        
        list_item_strings = ["Hey", "Hi", "Hello", "Howdy", "Greetings"]
        list_items = StringVar(value = list_item_strings)
        listbox = Listbox(root, listvariable = list_items)
        listbox.pack(side = tk.LEFT, padx = 40, pady = 20)
        listbox["height"] = 3
        listbox.bind("<<ListboxSelect>>", lambda s: self.select_item(listbox.curselection()))
        
    def press_button(self):
        text = self.entry_text.get()
        self.label_text.set(text)
    
    def select_item(self, index):
        selected_item = self.list_item_strings[index[0]]
        print(selected_item)
        
root = Tk()
MyApp(root)
root.mainloop()