tank_data = [("i",12,3,23),("q",54,23,45),("h",122,32,233),("f",132,12,2),("d",32,2,43)]
#re = [0 for i in range(len(tank_data))]
def evaluate_tankdata(tu):
    return tu[1]+tu[2]+tu[3]

tank_data.sort(key=evaluate_tankdata,reverse=True)
print(tank_data)

"""for i in range(len(tank_data)):
    re[i] = tank_data[i][1]+tank_data[i][2]+tank_data[i][3]
re.sort()
"""
#print(tank_data[0][1])


"""def evaluate_tankdata(tank_data):
    re=[]
    for tank in tank_data:
        for i in range(len(tank_data)):
            re[i] = tank[1]*tank[2]*tank[3]
            print(re)

    return re
"""
#ri = evaluate_tankdata(tank_data)
