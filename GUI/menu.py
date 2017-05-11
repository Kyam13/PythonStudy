import tkinter as tk
import tkinter.messagebox #tkinter.messageboxをインポート
#[閉じた]アイテムが選択されたとくに呼ばれる関数
def callback():
  #メッセージボックスの[はい]ボタンクリック時の処理
  if tk.messagebox.askyesno('Quit?','終了する？'):
    root.destroy()
  #[いいえ]ボタンクリックしたらなにもしない

root=tk.Tk()

#[閉じる]ボタンがクリックされたらcallback()関数を呼ぶ
root.protocol('WM_DELETE_WINDOW', callback)


menubar = tk.Menu(root)  #メニューバーのためのMenuオブジェクトを作成

#windowのメニューバーとして登録
root.config(menu=menubar)
#メニーのためのMenuオブジェクトを生成
#引数はメニューバー
filemenu=tk.Menu(menubar)
#ファイルメニューをメニューバーに配置
menubar.add_cascade(label='ファイル',menu=filemenu)
#[閉じる]アイテム配置
filemenu.add_command(label='閉じる',command=callback)

root.mainloop()
