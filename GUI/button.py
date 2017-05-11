import tkinter as tk

def push():
  print('押しましたね')

root = tk.Tk()
root.geometry('100x50')
button = tk.Button(root,text='押してね',command=push).pack()

root.mainloop()
