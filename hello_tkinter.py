import tkinter as tk

root=tk.Tk()

root.title("Hello,tkinter!")
root.geometry("640x480")

label = tk.Label(text="Hello,World")
label.pack()

root.mainloop()
