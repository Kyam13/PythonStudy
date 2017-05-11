import tkinter as tk

#ラジオボタンに表示する文字列を用意
item = ['庭の掃除','窓拭き','　車の洗車','庭のワックスがけ']

root = tk.Tk()
root.geometry('200x150')
val = tk.IntVar()         #IntVarオブジェクトを作成して変数に代入

#ラジオボタンの作成と配置
#itemリストの要素の数だけ処理を繰り返す
for i in range(len(item)):
  tk.Radiobutton(root,
                 value=i,
                 variable=val,
                 text=item[i]).pack(anchor=tk.W)

#ラジオボタンの状態を通知する関数
def choice():
  ch = val.get()  #IntVarオブジェクトの値を取得
  #リストitemのインデックスをchに指定して要素を出力
  print('明日は'+item[ch]+'をやりましょう')

#ボタンの作成と配置
button = tk.Button(root,
                   text='明日やること',
                   command = choice).pack()

root.mainloop()
