import tkinter as tk

root = tk.Tk()
root.geometry('100x100')

button1 = tk.Button(root, text='ボタン1').pack()

button2 = tk.Button(root, text='ボタン2').pack(side=tk.LEFT)

button1 = tk.Button(root, text='ボタン3').pack(side=tk.RIGHT)

root.mainloop()


