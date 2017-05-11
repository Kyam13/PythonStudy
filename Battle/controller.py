from responder import *
import random

class Controller:
  def __init__(self):
    self.lucky = LuckyResponder()
    self.draw = DrawResponder()
    self.bad = BadResponder()

  def attack(self, point):
    x=random.randint(0,100)
    if x <= 30:
      self.responder = self.lucky
    elif 31 <= x <=60:
      self.responder = self.draw
    else:
      self.responder = self.bad
    return self.responder.response(point)

"""
プログラムの実行ブロック
"""
if __name__ == '__main__':
  point = 3
  #Controllerにオブジェクト生成　
  ctr = Controller()
  #変動値を設定してresponse()メソッドを実行
  res = ctr.attack(point)
  #応答を表示
  print(res)

