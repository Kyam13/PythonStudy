import tkinter as tk

root = tk.Tk()
root.geometry('100x100')

buttion1 = tk.Button(
            root,
            text='ボタン１'
         ).pack()

button2 = tk.Button(
    root, text='ボタン2').pack()

button3 = tk.Button(
    root, text = 'ボタン3').pack()

root.mainloop()
