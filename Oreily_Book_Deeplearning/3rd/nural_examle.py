import numpy as np

def sigmoid(x):
    #sigmoid関数の定義
    #これも入力層と中間層の活性化関数として、利用されている。
    return 1/(1+np.exp(-x))


def init_network():
    #重みとバイアスの初期化
    network={}
    network['W1']=np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
    network['b1']=np.array([0.1,0.2,0.3])
    network['W2']=np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
    network['b2']=np.array([0.1,0.2])
    network['W3']=np.array([[0.1,0.3],[0.2,0.4]])
    network['b3']=np.array([0.1,0.2])

    return network

def identity_function(x):
    #出力層の活性化関数として利用される
    #恒等関数。。。入力をそのまま出力する関数
    return x

def forward(network,x):
    #入力信号が出力へと変換されるプロセスはまとめて実装
    W1,W2,W3=network['W1'],network['W2'],network['W3']
    b1,b2,b3=network['b1'],network['b2'],network['b3']

    a1=np.dot(x,W1)+b1# 信号伝達
    z1=sigmoid(a1)#h(x)
    a2=np.dot(z1,W2)+b2
    z2=sigmoid(a2)
    a3=np.dot(z2,W3)+b3
    y=identity_function(a3)#σ(x)

    return y

network=init_network()
x=np.array([1.0,0.5])#x１x２を準備
y=forward(network,x)#ニューラルネットワークの実装
print(y)