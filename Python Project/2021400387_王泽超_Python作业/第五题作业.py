import tkinter as tk

root = tk.Tk()
btn = tk.Button(root, text="请点击", command=lambda: print("Hello, World!"))
btn.pack()
root.mainloop()
