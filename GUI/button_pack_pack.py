import tkinter as tk

root = tk.Tk()
root.geometry('200x200')

button1 = tk.Button(root, text='ボタン1').place(x=0,y=0)

button2 = tk.Button(root, text='ボタン2').place(x=50,y=50)

button1 = tk.Button(root, text='ボタン3').place(x=100,y=100)

root.mainloop()
