import requests
from bs4 import BeautifulSoup
# BeautifulSoup4 => Beautiful.bs4

xml = requests.get('http://news.yahoo.co.jp/pickup/science/rss.xml')
# get()メソッドを使って RSSページのxmlデータが丸ごとダウンロード

soup = BeautifulSoup(xml.text , 'html.parser')
# BeautifulSoupをインスタンス化 対象のxmlやHTMLのデータを引数に
for news in soup.findAll('item'):
  #findAll()メソッドでスクレイピングを行う。その時スクレイピングしたいタグを引数に
  print(news.title.string)
  #その時欲しいのがtitleのタグなのでそこだけを出力

