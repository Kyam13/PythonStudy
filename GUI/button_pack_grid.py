import tkinter as tk

root = tk.Tk()
root.geometry('100x100')

button1 = tk.Button(root, text='ボタン1').grid(row=0,column=0)

button2 = tk.Button(root, text='ボタン2').grid(row=0,column=1)

button1 = tk.Button(root, text='ボタン3').grid(row=1,column=1)

root.mainloop()


