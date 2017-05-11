import tkinter as tk
import random

#グローバル変数の定義
response_area = None    #応答エリアのオブジェクトを保持

#明日の予定を決める関数
def wakuwaku():
    play = ['ちっちゃな映画館を探して映画を見にいく',
            'おしゃれなカフェでまったりする',
            '絶叫マシンの遊園地ではしゃぐ',
            'しっとりと神社・仏閣めぐり',
            'シナリオなしの路線バスの旅',
            'モヤモヤする街を散策する',
            'ざわめく待ちの酒場を放浪する'
            ]
    #playリストからランダムに抽出
    tomorrow = random.choice(play)
    #明日の予定をラベルに表示
    response_area.configure(text=tomorrow)

#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
#　図形を描写する関数
#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

def run():
    #グローバル変数を使用するための記述
    global response_area

    #メインウィンドウを作成
    root = tk.Tk()
    #ウィンドウのタイトル
    root.title('明日のデート:')
    #フォントとフォントサイズを指定するためのタプルを用意
    font = ('Helevetica', 14)

    #キャンパスの作成
    canvas = tk.Canvas(
                root,               #親要素のメインウィンドウに設定
                width = 550,
                height = 200,
                relief = tk.RIDGE,  #枠線を表示(土手に設定)
                bd = 2              #枠線の幅を設定(ピクセル単位)
                )
    canvas.pack()   #ウィンドウに配置

    img = tk.PhotoImage(file = 'sakura.gif') #表示するイメージを用意

    canvas.create_image(    #キャンパス上にイメージを配置
        0,                  #x座標
        0,                  #y座標
        image = img,        #配置するイメージを指定
        anchor = tk.NW      #配置の起点となる位置を左上隅に指定
    )

    #応答エリアの作成
    response_area = tk.Label(
                    root,               #親要素をメインウィンドウに設定
                    width=50,
                    height=10,
                    bg='pink',          #背景色を設定
                    font=font,          #フォントを設定
                    relief=tk.RIDGE,
                    bd=2                #枠線の幅を設定
    )
    response_area.pack()#メインウィンドウ上に配置

    #ボタンの作成
    button = tk.Button(
        root,
        font=font,
        text='明日のデートはどーする？',    #ボタンに表示するテキスト
        command = wakuwaku              #クリック時にwakuwaku()を呼ぶ
    )
    button.pack()#メインウィンドウ上に配置

    root.mainloop()

#==========================================
# プログラムの起点
#==========================================
if __name__ == '__main__':
    run()
