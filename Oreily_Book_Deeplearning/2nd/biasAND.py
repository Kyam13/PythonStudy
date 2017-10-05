def bAND(x1,x2):
    w1,w2,theta=0.5,0.5,0.7
    b=-0.7
    tmp=b+x1*w1+x2*w2
    if tmp<=0:
        return 0
    else:
        return 1

print(bAND(0,0))
print(bAND(0,1))
print(bAND(1,0))
print(bAND(1,1))
