from responder import * #responderモジュール全てのクラスをインポートする
import random

class Controller:
  """応答オブジェクトを呼び分けるクラス
  """
  def __init__(self):
    """応答オブジェクトを生成してresponderに格納
    """
    # LuckyResponderを生成してself.luckyに格納
    self.lucky = LuckyResponder()
    # DrawResponderを生成してself.drawに格納
    self.draw = DrawResponder()
    # BadResponderを生成してself.badに格納
    self.bad = BadResponder()

class Responder:
  """　応答のクラスのスーパークラス
  """
  def response(self, point):
    """ オーバーライドを前提としたメソッド

        @param point 変動値
        戻り値　空の文字列
    """
    return ' '

class LuckyResponder(Responder):
  """ モンスターにダメージを与えるサブクラス
  """
  def response(self, point):
    """ @param point 変動値
        戻り値　応答文字列と変動値のリスト
        """
    #応答文字列とpointの値を返す
    return ['モンスターにダメージを与えた!', point]

class DrawResponder(Responder):
  """引き分けに持ち込むサブクラス
  """
  def response(self, point):
    """@param point 変動値
      戻り値　応答文字列と変動値のリスト
    """
    # pointの値を0にして応答文字列と共に返す
    point = 0
    return ['モンスターは身を守っている',point]

class BadResponder(Responder):
  """ プレイヤーにダメージを与えるサブクラス
  """
  def response (self, point):
    """@param point 変値
    戻り値　応答文字列と変動値のリスト
    """
    #pointの値をマイナスにして応答文字列と共に返す
    return ['モンスターが反撃した！',-point]

"""
プログラムの実行ブロック
"""

if __name__ == '__main__':
  point = 3
  responder = LuckyResponder()
  res = responder.response(point)
  print(res)

  responder = DrawResponder()
  res = responder.response(point)
  print(res)
  responder = BadResponder()
  res = responder.response(point)
  print(res)

