import tkinter as tk

#チェックボタンに表示する文字列を用意
item = ['腕時計','手帳','預金通帳','傘']
#BooleanVarオブジェクトを格納するための辞書
check = {}

root = tk.Tk()

root.geometry('200x150')

#チェックボタンの作成と配置
#itemリストの要素の数だけ処理を繰り返す
for i in range(len(item)):
  #BooleanVarオブジェクトを作成してリストcheckの要素にする
  check[i] = tk.BooleanVar()
  #チェックボタンの作成と配置
  tk.Checkbutton(root,variable=check[i],text=item[i]).pack(anchor=tk.W)

#チェックボタンの状態を通知する関数
def choice():
  #辞書checkの要素の数だけ繰り返す
  for i in check:
    #checkのキーiのBooleanVarオブジェクトのValue/Faulseを調べる
    if check[i].get() == True:
      print(item[i] +'をお忘れなく')

#ボタンの作成と配置
button = tk.Button(root,text='明日の持ち物',command = choice).pack()

root.mainloop()
