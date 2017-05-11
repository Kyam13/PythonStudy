from controller import * #controllerモジュールのクラスをインポート
import random         #randomモジュールをインポート
import time

#攻撃方法を洗濯する
def choice():
  return input('[武器を使う(0)/呪文を唱える(1)]')

#武器を選択する
def arm_choice():
  return input('[鋼の劔(0)/英雄の杖(1)/叔父さんの杖(2)]')

#呪文を選択する
def magic_choice():
  return input('[メラメラ(0)/ギラギラ(1)/ベギラママン(2)]')

#リスタートするか選択する
def is_restart():
  return input('もう1回やる(やる(0)/やめる(1))')

def battle():
  """ゲームを実行する関数"""
  #プレイヤーのHPを設定
  hp_brave = 4

  #プレイヤーが0になるまで繰り返す
  while hp_brave > 0:
    #モンスターをランダムに設定して表示する
    monster = random.choice(['スライムン','あばれるうしくん','山賊'])
    print('\n>>>{}が現れた\n'.format(monster))
    #モンスターのHPを設定
    hp_monster =2
    #モンスターのHPが0になるまで繰り返す
    while hp_monster > 0:
      #攻撃は武器か呪文かを選択
      tool = choice()
      #規定値が入力されるまで繰り返す.
      while (True != tool.isdigit()) or (int(tool) > 1):
        tool = choice()

      #武器を選択した場合はどれを使うかを選択する
      tool = int(tool)
      if tool == 0:
        arm = arm_choice()
        while(True != arm.isdigit()) or (int(arm) > 2):
          arm = arm_choice()

      #武器を選択しなかった場合はどの呪文を使うかを選択する
      else:
        arm = magic_choice()
        while (True != arm.isdigit()) or (int(arm)>2):
          arm = arm_choice()

      #攻撃の開始を通知
      print('\n >>> {}の攻撃！！'.format(brave))


      #Controllerクラスのattack()を実行して応答を取得
      #引数はarmに1を足した値、これを変動値とする
      arm = int(arm)
      result = ctr.attack(arm + 1)


      #1秒待機して応答のメッセージを表示する
      time.sleep(1)
      print('>>>' + result[0])

      #プレイヤーのHPとモンスターのHPを増減して、それぞれのHPを表示
      hp_brave += result[1]
      hp_monster -= result[1]
      print('##########################################################') 
      print('{}のHP：{}'.format(brave,hp_brave))
      print('{}のHP：{}'.format('モンスター',hp_monster))
      print('###########################################################\n')

      #プレイヤーのHPが０以下なら内側のwhileブロックを抜ける
      if hp_brave <= 0:
        break
    #プレイヤーのHPが０以下なら外側のwhileを抜ける
    if hp_brave <= 0:
      break

    #モンスターのHPが０になれば内側のwhileをぬけて以下を表示、その後、外側のwhileの先頭に戻る
    print('>>> {}はモンスターをやっつけた！'.format(brave))

  #　プレイヤーのHPが０以下であれば外側のwhileを抜けて以下を表示
  print('>>> {}は死んでしまった・・・\n'.format(brave))

######
#実行するためのプログラム
######
#Controllerクラスのインスタンス化
ctr = Controller()

#プレイヤーの名前を取得する
brave = input('名前を入力　＞')

# ゲームを開始
battle()

#battle()関数が終了したらゲームを再開するか尋ねる
while True:
  # is_restart()関数でプレイヤーの意向を確認
  restart = is_restart()
  #規定値が入力されるまで繰り返す
  while (True != restart.isdigit()) or (int(restart) > 1):
    restart = is_restart()

  #０が入力されたらbattle()関数を実行
  #0以外ならループを抜けてプログラムを終了
  restart = int(restart)
  if restart == 0:
    battle()
  else:
    break


