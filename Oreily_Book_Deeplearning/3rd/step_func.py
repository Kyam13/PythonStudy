import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0,dtype=np.int)
    #dtypeとは返り値の型であり、ただ、x>0だけだとboolean型が返り値だから

x=np.arange(-5.0,5.0,0.1)
#-5.0から5.0までの範囲を0.1刻みでNumPy配列を生成します。
y=step_function(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)#y軸の範囲の指定
plt.show()
