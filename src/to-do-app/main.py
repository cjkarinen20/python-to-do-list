from tkinter import * 

class MyApp:
    
    def __init__(self, root):
        root.title("My app")
        root.geometry("500x400")
        root.maxsize(1000, 800)
        
        label = Label(root, text = "Some label text")
        label.pack()
        
        #label["text"] = "New label text"
        #label["font"] = ("Courier", 40)
        label.configure(text = "New label text", font = ("Courier", 40))
    
root = Tk()
MyApp(root)
root.mainloop()