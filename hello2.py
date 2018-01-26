import tkinter as tk

root = tk.Tk()

button = tk.Button(text='Push Me!', command=root.quit)
button.pack()

root.mainloop()
